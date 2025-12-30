#!/usr/bin/env python3
"""
Release Candidate Alignment Tool
Forces specific RC version bumps in CI pipelines to workaround history issues.
"""

import logging
import os
import re
import subprocess
import sys
from typing import List, NamedTuple, Optional

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Constants
BOT_NAME = "github-actions[bot]"
BOT_EMAIL = "github-actions[bot]@users.noreply.github.com"
TAG_PATTERN = re.compile(r"^v(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)-rc\.(?P<rc>\d+)$")

class Version(NamedTuple):
    major: int
    minor: int
    patch: int
    rc: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}-rc.{self.rc}"

class GitError(Exception):
    """Custom exception for Git failures."""
    pass

class Git:
    """Wrapper for Git subprocess calls."""

    @staticmethod
    def run(args: List[str], hide_output: bool = False) -> str:
        """Runs a git command and returns the stdout."""
        try:
            result = subprocess.run(
                ["git", *args],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            # If hiding output (e.g. secrets), don't log stderr
            error_msg = e.stderr.strip() if not hide_output else "[HIDDEN]"
            raise GitError(f"Command 'git {' '.join(args)}' failed: {error_msg}")

    @classmethod
    def get_latest_rc_tag(cls) -> Optional[str]:
        try:
            # --abbrev=0 suppresses the suffix, giving just the tag name
            return cls.run(["describe", "--tags", "--match", "v*-rc*", "--abbrev=0"])
        except GitError:
            return None

    @classmethod
    def get_commit_logs(cls, tag: str) -> str:
        # %B gets raw body, needed for footer parsing
        return cls.run(["log", f"{tag}..HEAD", "--pretty=format:%B"])

    @classmethod
    def configure_bot_identity(cls):
        cls.run(["config", "user.name", BOT_NAME])
        cls.run(["config", "user.email", BOT_EMAIL])

    @classmethod
    def last_commit_message(cls) -> str:
        return cls.run(["log", "-1", "--pretty=%B"])

    @classmethod
    def commit_empty(cls, message: str, description: str):
        cls.run(["commit", "--allow-empty", "-m", message, "-m", description])

    @classmethod
    def push(cls, token: Optional[str], repo: Optional[str]):
        """Configures remote and pushes HEAD to origin."""
        if token and repo:
            # Securely set the URL without printing it to logs
            url = f"https://x-access-token:{token}@github.com/{repo}.git"
            try:
                # We do not use cls.run here to ensure we control error logging closely
                subprocess.run(
                    ["git", "remote", "set-url", "origin", url],
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.PIPE
                )
            except subprocess.CalledProcessError:
                raise GitError("Failed to set remote URL (token invalid?).")

        cls.run(["push", "origin", "HEAD"])


class VersionLogic:
    """Business logic for calculating versions."""

    @staticmethod
    def parse_tag(tag: str) -> Optional[Version]:
        match = TAG_PATTERN.match(tag)
        if not match:
            return None
        return Version(
            major=int(match.group("major")),
            minor=int(match.group("minor")),
            patch=int(match.group("patch")),
            rc=int(match.group("rc"))
        )

    @staticmethod
    def detect_breaking(logs: str) -> bool:
        # 1. Check for "BREAKING CHANGE:" footer
        if "BREAKING CHANGE" in logs:
            return True
        # 2. Check for "type!:" or "type(scope)!:" in header
        # Regex explanation: Start of line, word chars, optional scope, !, colon
        return bool(re.search(r"^[a-z]+(\([a-z0-9-]+\))?!:\s", logs, re.MULTILINE))

    @staticmethod
    def detect_feat(logs: str) -> bool:
        # Regex: Start of line, 'feat', optional scope, optional !, colon
        return bool(re.search(r"^feat(\([a-z0-9-]+\))?!?:\s", logs, re.MULTILINE))

def set_github_output(key: str, value: str):
    """Writes to the GITHUB_OUTPUT environment file."""
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(f"{key}={value}\n")
    else:
        logger.warning("GITHUB_OUTPUT env var not found. Output not written.")

def command_calc() -> int:
    """Calculates the next version based on logic."""
    latest_tag = Git.get_latest_rc_tag()
    if not latest_tag:
        logger.info("No RC tag found. Letting Release Please handle initialization.")
        return 0

    logger.info(f"Found latest tag: {latest_tag}")
    
    logs = Git.get_commit_logs(latest_tag)

    if VersionLogic.detect_breaking(logs):
        logger.info("Detected BREAKING CHANGE. Exiting to allow standard Major bump.")
        return 0

    if VersionLogic.detect_feat(logs):
        logger.info("Detected FEATURE commit. Exiting to allow standard Minor/Patch bump.")
        return 0

    # Only Fixes/Chores detected
    current_version = VersionLogic.parse_tag(latest_tag)
    if not current_version:
        logger.error(f"Could not parse tag format: {latest_tag}")
        return 1

    # Increment RC
    next_version = Version(
        current_version.major,
        current_version.minor,
        current_version.patch,
        current_version.rc + 1
    )

    full_version_string = f"v{next_version}"
    logger.info(f"Detected only fixes. Forcing RC increment: {full_version_string}")
    
    set_github_output("next_version", full_version_string)
    return 0

def command_inject(target_ver: Optional[str]) -> int:
    """Injects the empty commit to force the version."""
    if not target_ver:
        logger.warning("No target version provided for injection.")
        return 0

    try:
        last_msg = Git.last_commit_message()
    except GitError as e:
        logger.error(f"Failed to read git log: {e}")
        return 1

    footer_marker = f"Release-As: {target_ver}"
    if footer_marker in last_msg:
        logger.info(f"Footer '{footer_marker}' already present. Skipping.")
        return 0

    logger.info(f"Injecting footer: {footer_marker}")

    try:
        Git.configure_bot_identity()
        Git.commit_empty(
            message="chore: enforce correct rc version",
            description=footer_marker
        )
        
        token = os.environ.get("GITHUB_TOKEN")
        repo = os.environ.get("GITHUB_REPOSITORY")
        Git.push(token, repo)
        
        logger.info("Successfully pushed Release-As override.")
    except GitError as e:
        logger.error(f"Git operation failed: {e}")
        return 1

    return 0

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: script.py [calc|inject] [version?]", file=sys.stderr)
        return 1

    command = sys.argv[1]

    if command == "calc":
        return command_calc()
    elif command == "inject":
        target_ver = sys.argv[2] if len(sys.argv) > 2 else None
        return command_inject(target_ver)
    else:
        logger.error(f"Unknown command: {command}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
