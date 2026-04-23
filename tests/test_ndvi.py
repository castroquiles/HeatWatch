import numpy as np
from src.analysis.ndvi import compute_ndvi, compute_tree_cover_percent

def test_ndvi_range():
    red = np.array([[0.1, 0.3], [0.5, 0.0]], dtype=np.float32)
    nir = np.array([[0.4, 0.2], [0.6, 0.0]], dtype=np.float32)
    ndvi = compute_ndvi(red, nir)
    assert np.all(ndvi >= -1.0)
    assert np.all(ndvi <= 1.0)

def test_ndvi_known_value():
    red = np.array([[0.1]], dtype=np.float32)
    nir = np.array([[0.5]], dtype=np.float32)
    ndvi = compute_ndvi(red, nir)
    assert abs(ndvi[0, 0] - 0.667) < 0.01

def test_ndvi_zero_denominator():
    red = np.array([[0.0]], dtype=np.float32)
    nir = np.array([[0.0]], dtype=np.float32)
    ndvi = compute_ndvi(red, nir)
    assert ndvi[0, 0] == 0.0

def test_tree_cover_all_vegetation():
    ndvi = np.full((5, 5), 0.8, dtype=np.float32)
    assert compute_tree_cover_percent(ndvi) == 100.0

def test_tree_cover_no_vegetation():
    ndvi = np.full((5, 5), 0.05, dtype=np.float32)
    assert compute_tree_cover_percent(ndvi) == 0.0
