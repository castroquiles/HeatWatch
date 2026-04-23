from __future__ import annotations
import numpy as np

NDVI_MODERATE_THRESHOLD = 0.4

def compute_ndvi(red_band: np.ndarray, nir_band: np.ndarray) -> np.ndarray:
    denominator = nir_band + red_band
    with np.errstate(invalid="ignore", divide="ignore"):
        ndvi = np.where(
            denominator == 0,
            0.0,
            (nir_band - red_band) / denominator,
        )
    ndvi = np.where(np.isnan(red_band) | np.isnan(nir_band), np.nan, ndvi)
    return ndvi.astype(np.float32)

def compute_tree_cover_percent(ndvi: np.ndarray, mask: np.ndarray | None = None) -> float:
    if mask is not None:
        ndvi_area = ndvi[mask]
    else:
        ndvi_area = ndvi.ravel()
    valid = ndvi_area[~np.isnan(ndvi_area)]
    if len(valid) == 0:
        return 0.0
    return float(np.sum(valid > NDVI_MODERATE_THRESHOLD) / len(valid) * 100)
