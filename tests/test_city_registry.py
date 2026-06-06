import pytest
from pathlib import Path
from src.utils.city_registry import list_cities, load_city, get_city_meta, load_registry


def test_list_cities_returns_sorted():
    cities = list_cities()
    assert cities == sorted(cities)


def test_list_cities_contains_defaults():
    cities = list_cities()
    assert "detroit" in cities
    assert "phoenix" in cities


def test_load_city_detroit():
    neighborhoods = load_city("detroit")
    assert len(neighborhoods) > 0
    names = [n.name for n in neighborhoods]
    assert "West Pullman" in names


def test_load_city_phoenix():
    neighborhoods = load_city("phoenix")
    assert len(neighborhoods) > 0
    names = [n.name for n in neighborhoods]
    assert "Downtown Phoenix" in names


def test_load_city_unknown_raises():
    with pytest.raises(KeyError, match="not found in registry"):
        load_city("atlantis")


def test_load_city_neighborhood_data_types():
    neighborhoods = load_city("detroit")
    for n in neighborhoods:
        assert isinstance(n.lst_mean, float)
        assert isinstance(n.lst_p90, float)
        assert isinstance(n.tree_cover_pct, float)
        assert isinstance(n.population, int)


def test_get_city_meta_detroit():
    meta = get_city_meta("detroit")
    assert meta["name"] == "Detroit"
    assert meta["country"] == "USA"
    assert meta["coordinate_system"] == "wgs84"


def test_get_city_meta_unknown_raises():
    with pytest.raises(KeyError):
        get_city_meta("atlantis")


def test_load_registry_returns_dict():
    registry = load_registry()
    assert isinstance(registry, dict)
    assert "cities" in registry


def test_load_registry_bad_path_raises():
    with pytest.raises(FileNotFoundError):
        load_registry(Path("/nonexistent/registry.yaml"))
