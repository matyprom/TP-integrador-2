from satelite import Satelite 
from catalogo import crear_catalogo, crear_resumen
import pytest


def test_catalogo():
    satelite_valido=[{
    "OBJECT_NAME": "CALSPHERE 1",
    "OBJECT_ID": "1964-063C",
    "EPOCH": "2026-10-14T14:21:25.466688",
    "MEAN_MOTION": 13.76730837,
    "ECCENTRICITY": 0.00243553,
    "INCLINATION": 90.2208,
    "RA_OF_ASC_NODE": 74.5342,
    "ARG_OF_PERICENTER": 291.4443,
    "MEAN_ANOMALY": 198.023,
    "EPHEMERIS_TYPE": 0,
    "CLASSIFICATION_TYPE": "U",
    "NORAD_CAT_ID": 900,
    "ELEMENT_SET_NO": 999,
    "REV_AT_EPOCH": 8785,
    "BSTAR": 0.00056429819,
    "MEAN_MOTION_DOT": 5.64e-06,
    "MEAN_MOTION_DDOT": 0}]
    satelite=crear_catalogo(satelite_valido)
    assert len(satelite) == 1
    assert satelite[0].nombre == "CALSPHERE 1"
    assert satelite[0].num_catalogo == 900

def test_crear_resumen():
    satelites = [
        Satelite("1", 25544, 0, 0, 400),
        Satelite("2", 25545, 0, 0, 600),
        Satelite("3", 25546, 0, 0, 10000)
    ]

    resultado = crear_resumen(satelites)

    assert resultado["LEO"]["cantidad"] == 2
    assert resultado["LEO"]["minimo"] == 400
    assert resultado["LEO"]["maximo"] == 600
    assert resultado["LEO"]["promedio"] == 500

    assert resultado["MEO"]["cantidad"] == 1