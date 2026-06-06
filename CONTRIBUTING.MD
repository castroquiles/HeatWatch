# Contributing to HeatWatch

Thank you for your interest in contributing! HeatWatch is built by volunteers from around the world.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Pick an Issue](#how-to-pick-an-issue)
- [Coding Standards](#coding-standards)
- [Pull Request Process](#pull-request-process)
- [Commit Message Format](#commit-message-format)
- [Getting Help](#getting-help)

---

## Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/). Be kind, be patient, be constructive. We are a climate-positive community.

---

## Getting Started

1. Star the repo
2. Read the README to understand what HeatWatch does
3. Browse open issues: https://github.com/castroquiles/HeatWatch/issues
4. Introduce yourself in Discussions (optional but welcome)

---

## Development Setup

### macOS / Linux

```bash
git clone https://github.com/YOUR_USERNAME/HeatWatch.git
cd HeatWatch
git remote add upstream https://github.com/castroquiles/HeatWatch.git
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
pytest tests/ -v
```

---

### Windows

GDAL and rasterio have native dependencies that are difficult to build on Windows with plain pip. Use conda to handle binaries first, then pip-install the project.

#### Prerequisites

- Git: https://git-scm.com/download/win
- Miniconda: https://conda.io/miniconda

#### Step 1 - Initialize conda for your shell (first time only)

If conda activate gives you a CommandNotFoundError, run this once and restart your terminal:

```powershell
conda init powershell
```

#### Step 2 - Create a conda environment

```powershell
conda create -n heatwatch python=3.11
conda activate heatwatch
```

#### Step 3 - Install GDAL and spatial libraries via conda

Do this before running pip install. Installing rasterio with pip on Windows without GDAL pre-installed will fail with missing DLL errors.

```powershell
conda install -c conda-forge gdal rasterio fiona shapely pyproj
```

#### Step 4 - Clone and install HeatWatch

```powershell
git clone https://github.com/YOUR_USERNAME/HeatWatch.git
cd HeatWatch
git remote add upstream https://github.com/castroquiles/HeatWatch.git
pip install -e ".[dev]"
```

#### Step 5 - Verify

```powershell
pytest tests/ -v
heatwatch --help
```

#### Common Windows Gotchas

| Problem | Cause | Solution |
|---------|-------|----------|
| ImportError: DLL load failed | GDAL not on PATH | conda install -c conda-forge gdal |
| conda activate does nothing | Shell not initialized | conda init powershell, restart terminal |
| pip install rasterio fails | Missing GDAL headers | conda install -c conda-forge rasterio |
| Long path errors during clone | Windows 260-char path limit | git config --global core.longpaths true |
| Slow test execution | Anti-virus scanning bytecode | Add project folder to AV exclusions |

---

### Docker (any platform)

```bash
docker build -t heatwatch .
docker run --rm -it heatwatch pytest tests/ -v
```

Requires Docker Desktop: https://www.docker.com/products/docker-desktop/

---

## How to Pick an Issue

For first-time contributors, look for issues tagged `good first issue`. For returning contributors, look for `help wanted` or `enhancement`.

Comment "I'd like to work on this" to claim an issue. Do not open a PR for an unassigned issue.

---

## Coding Standards

- Black for formatting (line length 88)
- Ruff for linting
- mypy for type checking (encouraged)

```bash
black src/ tests/
ruff check src/ tests/
pytest tests/ -v
```

Pre-commit hooks (recommended):

```bash
pip install pre-commit
pre-commit install
```

- Keep functions small, one job each
- Docstrings on every public function (Google style)
- Type hints on all function signatures
- No magic numbers, use named constants
- Comment the why, not the what

---

## Pull Request Process

1. Branch from main:

```bash
git checkout main
git pull upstream main
git checkout -b feature/your-feature-name
```

2. Make changes with small focused commits
3. Run tests and linting before pushing
4. Push to your fork and open a PR
5. Link the issue with "Closes #N"
6. Respond to review feedback

PR checklist:
- Tests pass locally
- New code has tests
- Docstrings added or updated
- CHANGELOG.md updated for user-facing changes
- Issue linked in PR description

---

## Commit Message Format

We follow Conventional Commits: https://www.conventionalcommits.org/
