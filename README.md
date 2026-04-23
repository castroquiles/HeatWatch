HeatWatch

Open-source urban heat island analysis for climate adaptation
Helps cities identify heat risk, vulnerable communities, and cooling interventions using satellite data

MIT License · Python 3.10+ · Contributions welcome

Problem

Urban Heat Islands make cities 2–10°C hotter than surrounding areas, increasing heat-related deaths and inequality.

Most cities lack accessible tools to:

* Map heat at neighborhood scale
* Identify vulnerable populations
* Measure cooling impact of green infrastructure

HeatWatch provides a reproducible way to analyze urban heat using satellite and census data.

What It Does

HeatWatch converts geospatial data into climate intelligence:

* Satellite-based heat mapping (Landsat Land Surface Temperature)
* Neighborhood vulnerability scoring (demographics + heat exposure)
* Vegetation analysis (NDVI for tree cover and cooling potential)
* Multi-year change detection
* Export-ready outputs (GeoJSON, CSV, PNG)

Quick Start

```bash id="g9k3xz"
git clone https://github.com/your-org/heatwatch.git
cd heatwatch

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -e ".[dev]"

heatwatch analyze --sample-city detroit
```

Example Output

```text id="m2v8qp"
Hottest neighborhood:  West Pullman   (42.1°C)
Coolest neighborhood:  Lincoln Park   (31.8°C)
Most vulnerable:       Englewood      (high heat + low tree cover)

Saved to:
./results/detroit/
```

Tech Stack

* Python 3.10+
* rasterio
* geopandas
* NASA Earthdata / USGS Landsat
* FastAPI
* folium
* pytest

Key Features

* Urban heat island mapping from satellite data
* Climate vulnerability scoring
* Vegetation and cooling analysis (NDVI)
* Multi-year heat trend tracking
* GIS-ready exports

Project Structure

```text id="q7d1mn"
heatwatch/
├── src/
│   ├── analysis/
│   ├── api/
│   └── utils/
├── data/
│   ├── sample/
├── tests/
├── docs/
└── ROADMAP.md
```

Roadmap

* MVP: LST + NDVI + CLI tool
* Phase 2: Web dashboard + multi-city support
* Phase 3: Global dataset + ML-based forecasting

Contributing

We welcome contributions across engineering, geospatial analysis, and climate science.

Start here:

1. Find a Good First Issue
2. Fork the repository
3. Create a feature branch
4. Submit a pull request

Areas needing help:

* New city data sources
* Performance optimization
* Visualization improvements
* Documentation
* Testing

Why This Matters

HeatWatch supports:

* Climate resilience planning
* Public health protection
* Equitable urban design
* Open climate research

License

MIT License — free to use, modify, and distribute

Contact

Issues: [https://github.com/your-org/heatwatch/issues](https://github.com/your-org/heatwatch/issues)
Discussions: [https://github.com/your-org/heatwatch/discussions](https://github.com/your-org/heatwatch/discussions)
