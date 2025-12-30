#!/usr/bin/env python3
import os
import re
import subprocess

def git(args):
    return subprocess.run(["git"] + args, stdout=subprocess.PIPE, text=True).stdout.strip()

def main():
    try:
        # 1. Get the latest RC tag (e.g., v0.1.1-rc.1)
        tag = git(["describe", "--tags", "--match", "v*-rc*", "--abbrev=0"])
        if not tag: return

        # 2. Get commits since that tag
        logs = git(["log", f"{tag}..HEAD", "--pretty=format:%B"])
        
        # 3. Check for BREAKING CHANGES
        # If breaking, we exit and let release-please handle the MAJOR bump logic natively.
        is_breaking = "BREAKING CHANGE" in logs or re.search(r"^[a-z]+(\(.*\))?!:\s", logs, re.MULTILINE)
        if is_breaking: return

        # 4. Check for Features (feat: ...)
        # Note: We exclude 'feat!:' because that is handled by is_breaking above.
        is_feat = re.search(r"^feat(\(.*\))?:\s", logs, re.MULTILINE)

        # 5. Parse Current Version
        # Matches v0.1.1-rc.1 -> major=0, minor=1, patch=1, rc=1
        m = re.match(r"^v(\d+)\.(\d+)\.(\d+)-rc\.(\d+)$", tag)
        if not m: return
        
        major, minor, patch, rc = int(m[1]), int(m[2]), int(m[3]), int(m[4])
        next_ver = ""

        if is_feat:
            if patch > 0:
                # CASE A: We are currently in a Patch candidate (e.g. 0.1.1-rc.1).
                # A new Feature invalidates 0.1.1 and promotes us to the next Minor (0.2.0).
                next_ver = f"{major}.{minor + 1}.0-rc.1"
            else:
                # CASE B: We are already in a Minor/Major candidate (e.g. 0.2.0-rc.1).
                # New features just accumulate in this pending release.
                next_ver = f"{major}.{minor}.{patch}-rc.{rc + 1}"
        else:
            # CASE C: Only Fixes/Chores.
            # Keep the version, just increment RC.
            next_ver = f"{major}.{minor}.{patch}-rc.{rc + 1}"
        
        # 6. Output for GitHub Actions
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"next_version={next_ver}\n")
            
    except Exception as e:
        print(f"Error: {e}")
        pass

if __name__ == "__main__":
    main()
