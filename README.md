# Trabajo Práctico Integrador 2 - Satélites

**Estudiante:** [Matias Ramirez]

## Descripción del Proyecto

Este proyecto consiste en un programa de línea de comandos (CLI) desarrollado en Python para procesar, validar y consultar información sobre satélites activos a partir de datos en formato JSON.
El sistema calcula la posición geográfica actual (latitud, longitud y altitud) de cada satélite mediante la librería `skyfield`, representa cada entidad como un objeto de la clase `Satelite`, valida la integridad de sus atributos y permite realizar dos tipos principales de consultas:
- **Resumen:** Estadísticas generales de satélites agrupados por tipo de órbita (LEO, MEO, GEO, HEO).
- **Zona:** Filtrado de satélites ubicados dentro de una región geográfica delimitada por un rectángulo de coordenadas.

---

## Estructura del Repositorio

```text
tpi2-satelites/
├── README.md
├── requirements.txt
├── .gitignore
├── funciones_base.py          
├── consultar_satelites.py    
├── satelite.py               
├── catalogo.py               
├── datos/
│   └── satelites.json         
├── test_satelite.py         
└── test_catalogo.py           
```
#### Consultar el resumen

```bash
python consultar_satelites.py datos/satelites.json resumen
```

### Consultar satélites por zona

```bash
python consultar_satelites.py datos/satelites.json zona <long_min> <lat_min> <long_max> <lat_max>
```