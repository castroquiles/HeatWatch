# Data Sources

This document explains where HeatWatch satellite data comes from and how to access it.

---

## NASA Earthdata

HeatWatch uses **NASA Earthdata** as its primary source for Landsat satellite imagery.

### What is NASA Earthdata?

NASA Earthdata is a free, open portal providing access to NASA's Earth observation data. It hosts petabytes of satellite imagery, climate records, and environmental datasets.

### How to get a free account

1. Go to [https://urs.earthdata.nasa.gov](https://urs.earthdata.nasa.gov)
2. Click **“Register”** in the top-right corner
3. Fill in your name, email, and affiliation (you can use “Individual / Researcher”)
4. Verify your email address
5. Log in and accept the terms of use for Landsat data

> **Tip:** Keep your username and password handy. The HeatWatch CLI will prompt for them when downloading scenes.

---

## Landsat Bands Used

HeatWatch processes the following Landsat Collection 2 Level-2 bands:

| Band | Name | Wavelength | Purpose in HeatWatch |
|------|------|------------|----------------------|
| B10 | Thermal Infrared (TIRS 1) | 10.6 – 11.2 μm | Land Surface Temperature (LST) |
| B4 | Red | 0.64 – 0.67 μm | NDVI (vegetation detection) |
| B5 | Near Infrared (NIR) | 0.85 – 0.88 μm | NDVI (vegetation detection) |

### How LST is derived

1. Download the Landsat scene (`.tif` files) via Earthdata
2. Convert Band 10 Digital Numbers (DN) to Top-of-Atmosphere (TOA) radiance
3. Apply atmospheric correction using metadata
4. Convert radiance to brightness temperature (Kelvin)
5. Apply emissivity correction using NDVI-derived land-cover values
6. Output: per-pixel Land Surface Temperature in °C

---

## USGS APIs

In addition to manual downloads, HeatWatch can query the **USGS M2M API** (Machine-to-Machine) to:

* Search for scenes by date range and bounding box
* Filter by cloud cover percentage
* Download directly without using the web interface

### API Endpoint

```text
https://m2m.cr.usgs.gov/api/api/json/stable/
```

### Authentication

The M2M API uses the same Earthdata credentials (username + app token). You can generate an app token from your Earthdata profile page.

---

## Census Data

Vulnerability scoring combines heat exposure with socioeconomic data:

* **Source:** US Census Bureau American Community Survey (ACS) 5-Year Estimates
* **Variables used:** population density, age distribution, income, housing quality
* **Access:** [https://data.census.gov](https://data.census.gov) (no account required for bulk download)

---

## Data Pipeline Overview

```text
├── Landsat scene search (Earthdata / USGS M2M API)
├── Download B4, B5, B10
├── Pre-process: reproject, clip to city boundary
├── Compute NDVI from B4+B5
├── Compute LST from B10
├── Overlay census tract boundaries
└── Export: GeoJSON, CSV, PNG
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| “Unauthorized” error | Double-check Earthdata credentials; reset password if needed |
| Slow downloads | Use the M2M API instead of the web interface; download during off-peak hours |
| Missing scenes | Landsat has a 16-day repeat cycle; check adjacent dates |
| Cloudy imagery | Filter by `cloud_cover < 10` in the search query |

---

## Further Reading

* [NASA Earthdata Login Help](https://urs.earthdata.nasa.gov/documentation)
* [Landsat Collection 2 Level-2 Science Product Guide](https://www.usgs.gov/landsat-missions/landsat-collection-2-level-2-science-products)
* [USGS M2M API Documentation](https://m2m.cr.usgs.gov/)
