from __future__ import annotations

import numpy as np

# Landsat Collection 2 thermal constants for Band 10
# Source: USGS Landsat Collection 2 Level-2 Science Product Guide
K1_CONSTANT = 774.8853  # Watts / (m^2 * sr * um)
K2_CONSTANT = 1321.0789  # Kelvin

KELVIN_TO_CELSIUS = 273.15


def brightness_temperature(
    thermal_band: np.ndarray,
    k1: float = K1_CONSTANT,
    k2: float = K2_CONSTANT,
) -> np.ndarray:
    """Convert a Landsat thermal band (radiance) to brightness temperature in Celsius.

    Uses the standard inverse Planck function:
        BT = K2 / ln((K1 / radiance) + 1) - 273.15

    Args:
        thermal_band: 2-D array of at-sensor radiance values (W / m^2 sr um).
        k1: Planck constant K1 for the sensor band. Defaults to Landsat 8/9 Band 10.
        k2: Planck constant K2 for the sensor band. Defaults to Landsat 8/9 Band 10.

    Returns:
        Array of brightness temperature values in degrees Celsius, same shape as input.
        Pixels where radiance <= 0 are set to NaN.
    """
    radiance = thermal_band.astype(np.float64)
    with np.errstate(invalid="ignore", divide="ignore"):
        bt_kelvin = np.where(
            radiance > 0,
            k2 / np.log((k1 / radiance) + 1),
            np.nan,
        )
    return (bt_kelvin - KELVIN_TO_CELSIUS).astype(np.float32)


def compute_lst_stats(bt: np.ndarray) -> dict[str, float]:
    """Compute summary statistics for a brightness temperature array.

    Args:
        bt: 2-D array of brightness temperature values in Celsius.

    Returns:
        Dictionary with keys: mean, std, p10, p50, p90, min, max.
        All values in degrees Celsius. Returns NaN for all stats if array is empty.
    """
    valid = bt[~np.isnan(bt)]
    if len(valid) == 0:
        nan = float("nan")
        return dict(mean=nan, std=nan, p10=nan, p50=nan, p90=nan, min=nan, max=nan)
    return {
        "mean": float(np.mean(valid)),
        "std": float(np.std(valid)),
        "p10": float(np.percentile(valid, 10)),
        "p50": float(np.percentile(valid, 50)),
        "p90": float(np.percentile(valid, 90)),
        "min": float(np.min(valid)),
        "max": float(np.max(valid)),
    }
