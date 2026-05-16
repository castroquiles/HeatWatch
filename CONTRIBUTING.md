# Contributing to HeatWatch

Thank you for your interest in improving HeatWatch! This guide will help you get the development environment running on your machine.

---

## Quick Start (macOS / Linux)

```bash
git clone https://github.com/castroquiles/HeatWatch.git
cd HeatWatch

python -m venv venv
source venv/bin/activate

pip install -e ".[dev]"

pytest
```

---

## Windows Setup

This section covers Windows-specific steps and common gotchas.

### Prerequisites

* **Python 3.10+** — Download from [python.org](https://www.python.org/downloads/). During installation, check **“Add Python to PATH”**.
* **Git** — Download from [git-scm.com](https://git-scm.com/download/win).
* **GDAL / rasterio dependencies** — These can be tricky on Windows. The easiest route is using **conda**.

### Step 1: Install Miniconda

1. Download Miniconda from [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
2. Run the installer and accept the defaults
3. Open **Anaconda Prompt** (or Windows Terminal with PowerShell)

### Step 2: Create and activate a conda environment

```powershell
conda create -n heatwatch python=3.11
conda activate heatwatch
```

> **Gotcha:** If `conda activate heatwatch` fails with “CommandNotFoundError”, run:
> ```powershell
> conda init powershell
> ```
> Then **restart your terminal**.

### Step 3: Install GDAL and spatial libraries

```powershell
conda install -c conda-forge gdal rasterio fiona shapely pyproj
```

> **Gotcha:** Do **not** use `pip install rasterio` on Windows without first installing GDAL via conda. You will get missing DLL errors.

### Step 4: Clone and install HeatWatch

```powershell
git clone https://github.com/castroquiles/HeatWatch.git
cd HeatWatch

pip install -e ".[dev]"
```

### Step 5: Verify the installation

```powershell
pytest
heatwatch --help
```

If both commands run without errors, you're ready to contribute!

---

## Common Windows Gotchas

| Problem | Cause | Solution |
|---------|-------|----------|
| `ImportError: DLL load failed` | GDAL not installed or not on PATH | Install GDAL via `conda install -c conda-forge gdal` |
| `conda activate` does nothing | Shell not initialized for conda | Run `conda init powershell` and restart terminal |
| `pip install rasterio` fails | Missing C++ build tools / GDAL headers | Use `conda install -c conda-forge rasterio` instead |
| Long path errors during clone | Windows default path limit (260 chars) | Enable long paths: `git config --global core.longpaths true` |
| Slow test execution | Anti-virus scanning Python bytecode | Add your project folder to AV exclusions temporarily |

---

## Submitting Changes

1. **Fork** the repository
2. **Create a branch**: `git checkout -b feat/your-feature-name`
3. **Make your changes** and add tests if applicable
4. **Run tests**: `pytest`
5. **Commit**: `git commit -m "feat: describe your change"`
6. **Push**: `git push origin feat/your-feature-name`
7. **Open a Pull Request** against `main`

---

## Code Style

* Follow PEP 8
* Use meaningful variable names
* Add docstrings to public functions
* Keep functions small and focused

---

## Need Help?

* Open an [Issue](https://github.com/castroquiles/HeatWatch/issues)
* Start a [Discussion](https://github.com/castroquiles/HeatWatch/discussions)
* Comment on the issue you're working on
