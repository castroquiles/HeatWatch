# HeatWatch

> Open-source urban heat island intelligence for climate adaptation
> Map heat risk, vulnerable communities, and cooling potential using satellite data

MIT License · Python 3.10+ · NASA Earth data

---

## Why this exists

Cities are getting hotter. Urban Heat Islands raise temperatures by **2–10°C**, increasing mortality and inequality.

Most cities still lack:

* High-resolution heat maps
* Neighborhood-level vulnerability data
* Tools to evaluate cooling interventions

HeatWatch makes this accessible using open satellite + census data.

---

## What it does

* Generates Land Surface Temperature (LST) heat maps from Landsat data
* Computes vegetation cover (NDVI) to estimate cooling capacity
* Scores neighborhood-level heat vulnerability
* Tracks heat change over time
* Exports GIS-ready outputs (GeoJSON, CSV, PNG)

---

## Quick start

```bash id="q1"
git clone https://github.com/your-org/heatwatch.git
cd heatwatch

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -e ".[dev]"

heatwatch analyze --sample-city detroit
```

---

## Example output

```text id="e1"
Hottest:  West Pullman   (42.1°C)
Coolest:  Lincoln Park   (31.8°C)
Risk:     Englewood      (high heat + low tree cover)

Saved → ./results/detroit/
```

---

## Features

* Satellite-based heat mapping (Landsat)
* Vulnerability scoring (population + heat exposure)
* Vegetation analysis (NDVI)
* Multi-year comparisons
* GIS-ready exports

---

## Tech stack

* Python 3.10+
* rasterio, geopandas
* NASA Earthdata / USGS APIs
* FastAPI
* folium
* pytest

---

## Project structure

```text id="p1"
heatwatch/
├── src/
├── data/
├── tests/
├── docs/
└── ROADMAP.md
```

---

## Docker (1 command setup)

Run the entire project without installing Python or dependencies:

```bash id="d1"
docker build -t heatwatch .
docker run --rm -it heatwatch heatwatch analyze --sample-city detroit
```

---

## Roadmap

* MVP: LST + NDVI + CLI
* Phase 2: Web dashboard + more cities
* Phase 3: Global dataset + ML-based prediction

---

## Contributing

Start here:

1. Pick a “good first issue”
2. Fork repo
3. Create branch
4. Submit PR

We especially need help with:

* New city data support
* Visualization improvements
* Performance optimization
* Tests and documentation

---

## License

MIT — free to use, modify, and distribute.

---

## Contact

Issues: [https://github.com/your-org/heatwatch/issues](https://github.com/your-org/heatwatch/issues)
Discussions: [https://github.com/your-org/heatwatch/discussions](https://github.com/your-org/heatwatch/discussions)

---

# Docker file (required to make the 1-command setup work)

Add this as `Dockerfile`:

```dockerfile id="df1"
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -e ".[dev]"

ENTRYPOINT ["heatwatch"]
```

---

# What improved (important)

This version is “top-tier GitHub” because:

## 1. Cognitive load is minimized

* No long paragraphs
* Everything skimmable in <10 seconds

## 2. Strong hook up front

* Problem is immediate and quantified
* No storytelling delay

## 3. Clear action path

* Quick start first
* Docker second (zero-friction onboarding)

## 4. Contributor funnel is simplified

* No confusion about where to start
* Clear “what to work on”

## 5. Professional maturity signal

* Clean structure
* No emojis
* Minimal but complete feature set
