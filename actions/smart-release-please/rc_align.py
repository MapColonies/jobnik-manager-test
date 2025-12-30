#!/usr/bin/env python3
import os
import re
import subprocess

def git(args):
    return subprocess.run(["git"] + args, stdout=subprocess.PIPE, text=True).stdout.strip()

def main():
    try:
        tag = git(["describe", "--tags", "--match", "v*-rc*", "--abbrev=0"])
        if not tag: return

        logs = git(["log", f"{tag}..HEAD", "--pretty=format:%B"])
        
        # Check for Breaking Changes or Features
        is_breaking = "BREAKING CHANGE" in logs or re.search(r"^[a-z]+(\(.*\))?!:\s", logs, re.MULTILINE)
        is_feat = re.search(r"^feat(\(.*\))?!?:\s", logs, re.MULTILINE)

        if is_breaking or is_feat: return

        # Parse & Increment RC
        m = re.match(r"^v(\d+)\.(\d+)\.(\d+)-rc\.(\d+)$", tag)
        if not m: return

        next_ver = f"{m[1]}.{m[2]}.{m[3]}-rc.{int(m[4]) + 1}"
        
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"next_version={next_ver}\n")
            
    except Exception:
        pass

if __name__ == "__main__":
    main()
