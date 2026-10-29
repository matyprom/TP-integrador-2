import sys
from catalogo import leer_json, crear_resumen, crear_catalogo, obtener_satelites
ruta_json=sys.argv[1]
consulta=sys.argv[2]

janson=leer_json(ruta_json)
catalogo=crear_catalogo(janson)
normalizar=consulta.strip().lower()
print(normalizar)
if normalizar == "resumen":
    print("entre resumen")
    resumen=crear_resumen(catalogo)
    for orbita, datos in resumen.items():
        print(f"Orbita: {orbita}, {datos}")
elif normalizar == "zona":
    print("entre")
    longitud_minima = float(sys.argv[3])
    latitud_minima = float(sys.argv[4])
    longitud_maxima = float(sys.argv[5])
    latitud_maxima = float(sys.argv[6])
    satelites_filtrados=obtener_satelites(catalogo, longitud_minima, latitud_minima, longitud_maxima, latitud_maxima)
    print(f"Cantidad de satélites en la zona: {len(satelites_filtrados)}")
    for sat in satelites_filtrados:
            tipo = sat.tipo_orbita()
            print(sat.resumen_datos(tipo))
