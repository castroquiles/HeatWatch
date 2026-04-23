# HeatWatch Roadmap 

This document outlines HeatWatch's development trajectory across three phases.
It is a living document — community input shapes priorities.

---

## Phase 1 — MVP (Current)

**Goal:** A working CLI tool that produces meaningful heat analysis output for any major US city using free satellite data.

### Milestones

- [x] Project structure and contribution setup
- [ ] Landsat data download via NASA Earthdata API
- [ ] Land Surface Temperature (LST) calculation
- [ ] NDVI (vegetation index) calculation
- [ ] Neighborhood boundary overlay (GeoJSON)
- [ ] Basic vulnerability scoring (LST + tree cover)
- [ ] Interactive HTML map output (folium)
- [ ] CSV export of neighborhood scores
- [ ] Sample data for Detroit, MI (no credentials needed)
- [ ] FastAPI endpoint: `/analyze` (POST)
- [ ] CI pipeline (GitHub Actions)
- [ ] 80%+ test coverage on core analysis functions
- [ ] Docs: architecture, data sources, API reference

**Target:** 6–8 weeks from first commit

---

## Phase 2 — Expansion

**Goal:** Broaden city coverage, add intervention modeling, and launch a simple web UI.

### Features Planned

- ** Global city support** — Expand beyond US to EU, Southeast Asia, Sub-Saharan Africa
- ** Intervention simulator** — Model temperature reduction from tree planting, cool roofs, parks (scenario modeling)
- ** Web UI** — Simple React dashboard for non-technical users (upload boundary → view map)
- ** Multi-year time series** — Year-over-year heat trend analysis per neighborhood
- ** Alert integration** — Flag neighborhoods exceeding heatwave risk thresholds
- ** Docker support** — One-command setup for all platforms
- ** Internationalization** — README and docs in Spanish, French, Arabic

### Infrastructure

- Automated data refresh pipeline (weekly Landsat pulls for subscribed cities)
- Public REST API with rate limiting for external apps
- Community city registry (crowdsourced boundary files)

---

## Phase 3 — Scale & IEEE Integration

**Goal:** Production-grade tool used by city governments and aligned with IEEE Planet Positive 2030 SDG targets.

### Features Planned

- ** ML heat prediction** — Train models to predict future LST from urban morphology features
- ** Sentinel-2 integration** — 10m resolution (vs 30m Landsat) for higher precision
- ** Policy dashboard** — Reports formatted for city council decision-making
- ** OpenStreetMap integration** — Automated building, road, and park data for intervention modeling
- ** IEEE SDG API** — Publish city scores to IEEE Planet Positive data commons
- ** Mobile-friendly PWA** — Field tool for community advocates
- ** Real-time weather fusion** — Merge satellite data with ground station readings

### Community Goals

- 50+ cities analyzed and published
- 100+ contributors from 20+ countries
- Peer-reviewed methodology paper (target: Nature Cities or similar)
- Partnerships with 3+ municipal governments

---

## How to Influence the Roadmap

Open a [GitHub Discussion](https://github.com/your-org/heatwatch/discussions) tagged `roadmap` and make your case. Priorities are set by maintainers with input from the community. Feature requests with volunteer implementers jump the queue.
