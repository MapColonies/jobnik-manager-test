# Event Files for Local Testing with Act

This directory contains event files for testing the GitHub Actions workflow locally using [act](https://github.com/nektos/act).

## Available Event Files

### 1. `push-next.json`
Simulates a push to the `next` branch (developer commit).

**Expected behavior:**
- Environment: `dev`
- Image tag: `next-{sha}`
- Chart tag: `0.0.0-next-{sha}`
- PR labels: `dev, auto-merge`
- Updates: `infra/environments/dev.yaml`

**Usage:**
```bash
act push -e .github/workflows/events/push-next.json -W .github/workflows/build-and-push\ copy.yaml
```

### 2. `release-rc.json`
Simulates a release candidate (RC) being published.

**Expected behavior:**
- Environment: `qa`
- Image tag: `v0.1.2-rc.10`
- Chart tag: `v0.1.2-rc.10`
- PR labels: `qa`
- Updates: `infra/environments/qa.yaml`

**Usage:**
```bash
act release -e .github/workflows/events/release-rc.json -W .github/workflows/build-and-push\ copy.yaml
```

### 3. `release-stable.json`
Simulates a stable release being published.

**Expected behavior:**
- Environment: `prod`
- Image tag: `v0.1.2`
- Chart tag: `v0.1.2`
- PR labels: `prod`
- Updates: `infra/environments/prod.yaml`
- **Plus:** Housekeeping jobs update `qa` and `integration` environments

**Usage:**
```bash
act release -e .github/workflows/events/release-stable.json -W .github/workflows/build-and-push\ copy.yaml
```

## Testing with Act

### Prerequisites
1. Install act: https://github.com/nektos/act#installation
2. Configure secrets in `.secrets` file or use `--secret-file` flag

### Basic Commands

Test specific job:
```bash
act push -e .github/workflows/events/push-next.json -j determine-config
```

Dry run (show what would execute):
```bash
act push -e .github/workflows/events/push-next.json -n
```

List workflows:
```bash
act -l -W .github/workflows/build-and-push\ copy.yaml
```

### Tips
- Use `-v` flag for verbose output
- Use `--container-architecture linux/amd64` if you're on ARM (M1/M2 Mac)
- Use `-P ubuntu-latest=ghcr.io/catthehacker/ubuntu:act-latest` for a better container
