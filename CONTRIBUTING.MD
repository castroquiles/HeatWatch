# Contributing to HeatWatch 

Thank you for your interest in contributing! HeatWatch is built by volunteers from around the world. Whether you're a student writing your first open-source PR or an experienced engineer, there's a place for you here.

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

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/). Be kind, be patient, be constructive. We are a climate-positive community — we try to model that in how we treat each other too.

---

## Getting Started

1. **Star the repo** ⭐ (helps others find it)
2. **Read the README** to understand what HeatWatch does
3. **Browse [open issues](https://github.com/your-org/heatwatch/issues)**
4. **Introduce yourself** in [GitHub Discussions](https://github.com/your-org/heatwatch/discussions) (optional but welcome!)

---

## Development Setup

### Requirements

- Python 3.10 or higher
- Git
- A virtual environment tool (built-in `venv` is fine)

### Steps

```bash
# Fork the repo on GitHub, then clone YOUR fork
git clone https://github.com/YOUR_USERNAME/heatwatch.git
cd heatwatch

# Add the upstream remote so you can pull updates
git remote add upstream https://github.com/your-org/heatwatch.git

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate       # macOS/Linux
# venv\Scripts\activate        # Windows

# Install the package in editable mode with dev dependencies
pip install -e ".[dev]"

# Copy the environment template
cp .env.example .env
# (For most contributions, you don't need real NASA credentials —
#  the sample data in data/sample/ works without them)

# Verify your setup
pytest tests/ -v
```

If you see all tests passing, you're ready to contribute!

---

## How to Pick an Issue

### For First-Time Contributors

Look for issues tagged **`good first issue`**. These are:
- Well-scoped with clear acceptance criteria
- Don't require deep domain knowledge
- Have pointers to the relevant code

### For Returning Contributors

Look for **`help wanted`** or **`enhancement`** tags. These may require more context — feel free to ask questions in the issue before starting.

### Claiming an Issue

1. Comment on the issue: *"I'd like to work on this"*
2. A maintainer will assign it to you (usually within 48 hours)
3. If you don't hear back in 3 days, ping us in Discussions

**Please don't open a PR for an issue that hasn't been assigned to you** — it can create duplicate work.

---

## Coding Standards

### Style

- We use **[Black](https://black.readthedocs.io/)** for formatting (line length: 88)
- We use **[Ruff](https://docs.astral.sh/ruff/)** for linting
- We use **[mypy](https://mypy.readthedocs.io/)** for type checking (optional for now, encouraged)

Run all checks at once:
```bash
black src/ tests/
ruff check src/ tests/
pytest tests/ -v
```

Or use the pre-commit hooks (recommended):
```bash
pip install pre-commit
pre-commit install
# Hooks now run automatically on git commit
```

### Code Principles

- **Keep functions small** — one function, one job
- **Write docstrings** for every public function (Google style)
- **Add type hints** to function signatures
- **No magic numbers** — use named constants with comments explaining units
- **Comment the "why"**, not the "what" — the code shows what, comments explain why

### Example of Good Code Style

```python
# src/analysis/ndvi.py

# NDVI ranges from -1 (water/bare soil) to +1 (dense vegetation)
NDVI_VEGETATION_THRESHOLD = 0.3  # Values above this indicate meaningful tree cover

def compute_ndvi(red_band: np.ndarray, nir_band: np.ndarray) -> np.ndarray:
    """
    Compute the Normalized Difference Vegetation Index (NDVI).

    NDVI = (NIR - Red) / (NIR + Red)
    Higher values indicate denser, healthier vegetation.

    Args:
        red_band: Red spectral band array (Landsat Band 4).
        nir_band: Near-infrared band array (Landsat Band 5).

    Returns:
        NDVI array with values in range [-1, 1].
    """
    # Avoid division by zero where both bands are zero
    denominator = nir_band + red_band
    ndvi = np.where(denominator == 0, 0, (nir_band - red_band) / denominator)
    return ndvi.astype(np.float32)
```

### Testing

- Every new function should have at least one test
- Tests go in `tests/` mirroring the `src/` structure
- Use the sample data in `data/sample/` for tests (no NASA credentials needed)
- Run `pytest tests/ -v` before submitting your PR

---

## Pull Request Process

1. **Create a branch** from `main`:
   ```bash
   git checkout main
   git pull upstream main
   git checkout -b feature/your-feature-name
   # or: fix/issue-123-describe-fix
   ```

2. **Make your changes** — small, focused commits are better than one giant commit

3. **Run tests and linting** before pushing:
   ```bash
   black src/ tests/
   ruff check src/ tests/
   pytest tests/ -v
   ```

4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request** on GitHub:
   - Link the issue it closes: `Closes #42`
   - Describe *what* you changed and *why*
   - Add screenshots for any visual changes
   - Keep PRs focused — one issue per PR

6. **Respond to review feedback** — maintainers try to review within 5 business days

7. **Squash and merge** — maintainers will handle this

### PR Checklist

- [ ] Tests pass locally
- [ ] New code has tests
- [ ] Docstrings added/updated
- [ ] `CHANGELOG.md` updated (for user-facing changes)
- [ ] Issue linked in PR description

---

## Commit Message Format

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short description>

[optional body]

[optional footer]
```

**Types:** `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `style`

**Examples:**
```
feat(ndvi): add NDVI computation from Landsat 9 bands
fix(lst): handle missing data in temperature raster
docs(contributing): add Windows setup instructions
test(vulnerability): add tests for edge cases with no census data
```

---

## Getting Help

Stuck? Not sure where to start? That's completely normal!

- **GitHub Discussions** — best place for questions, ideas, and introductions
- **Issue comments** — ask clarifying questions directly on the issue
- **Email** — heatwatch@yourdomain.org for anything else

We are a friendly community. There are no dumb questions. 🌍
