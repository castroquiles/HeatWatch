from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from src.analysis.vulnerability import NeighborhoodData

REGISTRY_PATH = Path(__file__).parent.parent.parent / "data" / "cities" / "registry.yaml"


def load_registry(path: Path = REGISTRY_PATH) -> dict[str, Any]:
    """Load the city registry YAML file.

    Args:
        path: Path to registry.yaml. Defaults to data/cities/registry.yaml.

    Returns:
        Parsed registry as a dictionary.

    Raises:
        FileNotFoundError: If the registry file does not exist.
        yaml.YAMLError: If the file is not valid YAML.
    """
    if not path.exists():
        raise FileNotFoundError(f"City registry not found at {path}")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def list_cities(path: Path = REGISTRY_PATH) -> list[str]:
    """Return sorted list of city IDs from the registry.

    Args:
        path: Path to registry.yaml.

    Returns:
        Sorted list of city ID strings.
    """
    registry = load_registry(path)
    return sorted(registry.get("cities", {}).keys())


def load_city(city_id: str, path: Path = REGISTRY_PATH) -> list[NeighborhoodData]:
    """Load neighborhood data for a city from the registry.

    Args:
        city_id: City identifier string (e.g. 'detroit', 'phoenix').
        path: Path to registry.yaml.

    Returns:
        List of NeighborhoodData objects ready for scoring.

    Raises:
        KeyError: If city_id is not found in the registry.
        FileNotFoundError: If the registry file does not exist.
    """
    registry = load_registry(path)
    cities = registry.get("cities", {})

    if city_id not in cities:
        available = sorted(cities.keys())
        raise KeyError(
            f"City '{city_id}' not found in registry. "
            f"Available cities: {', '.join(available)}"
        )

    city_data = cities[city_id]
    neighborhoods = []

    for n in city_data.get("neighborhoods", []):
        neighborhoods.append(
            NeighborhoodData(
                name=n["name"],
                lst_mean=float(n["lst_mean"]),
                lst_p90=float(n["lst_p90"]),
                tree_cover_pct=float(n["tree_cover_pct"]),
                pct_elderly=float(n.get("pct_elderly", 0.0)),
                pct_no_ac=float(n.get("pct_no_ac", 0.0)),
                population=int(n.get("population", 0)),
                geometry_id=n.get("id", ""),
            )
        )

    return neighborhoods


def get_city_meta(city_id: str, path: Path = REGISTRY_PATH) -> dict[str, Any]:
    """Return metadata for a city from the registry.

    Args:
        city_id: City identifier string.
        path: Path to registry.yaml.

    Returns:
        Dictionary with city metadata (name, country, region, coordinate_system).

    Raises:
        KeyError: If city_id is not found in the registry.
    """
    registry = load_registry(path)
    cities = registry.get("cities", {})
    if city_id not in cities:
        raise KeyError(f"City '{city_id}' not found in registry.")
    data = cities[city_id]
    return {
        "id": city_id,
        "name": data.get("name", city_id),
        "country": data.get("country", ""),
        "region": data.get("region", ""),
        "coordinate_system": data.get("coordinate_system", "wgs84"),
        "geojson": data.get("geojson", ""),
    }
