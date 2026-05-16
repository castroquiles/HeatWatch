# HeatWatch

> Inteligencia de islas de calor urbano de código abierto para la adaptación al clima
> Mapea el riesgo térmico, comunidades vulnerables y potencial de enfriamiento usando datos satelitales

Licencia MIT · Python 3.10+ · Datos de la NASA

---

## Por qué existe

Las ciudades están calentándose. Las Islas de Calor Urbano aumentan las temperaturas entre **2–10°C**, incrementando la mortalidad y la desigualdad.

La mayoría de las ciudades aún carecen de:

* Mapas de calor de alta resolución
* Datos de vulnerabilidad a nivel de vecindario
* Herramientas para evaluar intervenciones de enfriamiento

HeatWatch hace esto accesible usando datos satelitales abiertos + datos censales.

---

## Qué hace

* Genera mapas de Temperatura de Superficie Terrestre (LST) a partir de datos Landsat
* Calcula la cobertura vegetal (NDVI) para estimar la capacidad de enfriamiento
* Puntúa la vulnerabilidad térmica a nivel de vecindario
* Rastrea el cambio de calor a lo largo del tiempo
* Exporta resultados listos para GIS (GeoJSON, CSV, PNG)

---

## Inicio rápido

```bash
git clone https://github.com/your-org/heatwatch.git
cd heatwatch

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -e ".[dev]"

heatwatch analyze --sample-city detroit
```

---

## Salida de ejemplo

```text
Hottest:  West Pullman   (42.1°C)
Coolest:  Lincoln Park   (31.8°C)
Risk:     Englewood      (high heat + low tree cover)

Saved → ./results/detroit/
```

---

## Características

* Mapeo térmico basado en satélite (Landsat)
* Puntuación de vulnerabilidad (población + exposición al calor)
* Análisis de vegetación (NDVI)
* Comparaciones multi-anuales
* Exportaciones listas para GIS

---

## Stack tecnológico

* Python 3.10+
* rasterio, geopandas
* NASA Earthdata / USGS APIs
* FastAPI
* folium
* pytest

---

## Estructura del proyecto

```text
heatwatch/
├── src/
├── data/
├── tests/
├── docs/
└── ROADMAP.md
```

---

## Docker (configuración en 1 comando)

Ejecuta todo el proyecto sin instalar Python ni dependencias:

```bash
docker build -t heatwatch .
docker run --rm -it heatwatch heatwatch analyze --sample-city detroit
```

---

## Hoja de ruta

* MVP: LST + NDVI + CLI
* Fase 2: Panel web + más ciudades
* Fase 3: Conjunto de datos global + predicción basada en ML

---

## Contribuir

Empieza aquí:

1. Elige un “good first issue”
2. Haz fork del repositorio
3. Crea una rama
4. Envía un PR

Especialmente necesitamos ayuda con:

* Soporte para datos de nuevas ciudades
* Mejoras de visualización
* Optimización de rendimiento
* Tests y documentación

---

## Licencia

MIT — libre de usar, modificar y distribuir.

---

## Contacto

Issues: [https://github.com/your-org/heatwatch/issues](https://github.com/your-org/heatwatch/issues)
Discussions: [https://github.com/your-org/heatwatch/discussions](https://github.com/your-org/heatwatch/discussions)
