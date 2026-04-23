import numpy as np
import pytest

@pytest.fixture
def sample_ndvi():
    rng = np.random.default_rng(42)
    return rng.uniform(-0.1, 0.8, size=(10, 10)).astype(np.float32)

@pytest.fixture
def sample_lst():
    rng = np.random.default_rng(42)
    return rng.uniform(28.0, 48.0, size=(10, 10)).astype(np.float32)
