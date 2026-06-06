import numpy as np
import pytest
from src.analysis.lst import brightness_temperature, compute_lst_stats, K1_CONSTANT, K2_CONSTANT


def test_brightness_temperature_known_value():
    radiance = np.array([[10.0]], dtype=np.float32)
    bt = brightness_temperature(radiance)
    expected = K2_CONSTANT / np.log(K1_CONSTANT / 10.0 + 1) - 273.15
    assert abs(bt[0, 0] - expected) < 0.01


def test_brightness_temperature_zero_radiance():
    radiance = np.array([[0.0]], dtype=np.float32)
    bt = brightness_temperature(radiance)
    assert np.isnan(bt[0, 0])


def test_brightness_temperature_negative_radiance():
    radiance = np.array([[-1.0]], dtype=np.float32)
    bt = brightness_temperature(radiance)
    assert np.isnan(bt[0, 0])


def test_brightness_temperature_output_shape():
    radiance = np.ones((10, 10), dtype=np.float32) * 5.0
    bt = brightness_temperature(radiance)
    assert bt.shape == (10, 10)


def test_brightness_temperature_higher_radiance_means_higher_temp():
    # Temperature should increase monotonically with radiance
    radiances = np.array([[3.0, 5.0, 8.0, 12.0]], dtype=np.float32)
    bt = brightness_temperature(radiances)
    assert bt[0, 0] < bt[0, 1] < bt[0, 2] < bt[0, 3]


def test_brightness_temperature_typical_landsat_range():
    # Radiance ~6-12 W/m2/sr/um is typical for Landsat Band 10 over urban areas
    radiance = np.array([[6.0, 8.0, 10.0, 12.0]], dtype=np.float32)
    bt = brightness_temperature(radiance)
    assert np.all(bt > -10)
    assert np.all(bt < 70)


def test_lst_stats_basic():
    bt = np.array([[30.0, 35.0, 40.0, 45.0]], dtype=np.float32)
    stats = compute_lst_stats(bt)
    assert abs(stats["mean"] - 37.5) < 0.01
    assert abs(stats["min"] - 30.0) < 0.01
    assert abs(stats["max"] - 45.0) < 0.01
    assert abs(stats["p50"] - 37.5) < 0.5


def test_lst_stats_ignores_nan():
    bt = np.array([[30.0, np.nan, 40.0]], dtype=np.float32)
    stats = compute_lst_stats(bt)
    assert abs(stats["mean"] - 35.0) < 0.01


def test_lst_stats_all_nan():
    bt = np.full((3, 3), np.nan, dtype=np.float32)
    stats = compute_lst_stats(bt)
    assert np.isnan(stats["mean"])
    assert np.isnan(stats["p90"])


def test_lst_stats_keys():
    bt = np.array([[35.0]], dtype=np.float32)
    stats = compute_lst_stats(bt)
    assert set(stats.keys()) == {"mean", "std", "p10", "p50", "p90", "min", "max"}
