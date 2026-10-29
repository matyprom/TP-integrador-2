import json
from funciones_base import obtener_posicion
from satelite import Satelite 
def leer_json(archivo):
    with open(archivo, 'r') as archivo:
        registros = json.load(archivo)
    return registros

def crear_catalogo(registros):
    lista_satelites=[]
    
    for registro in registros:
        lat, lon, alt =obtener_posicion(registro)
        sat = Satelite(
            nombre=registro["OBJECT_NAME"],
            num_catalogo=registro["NORAD_CAT_ID"],
            latitud=lat,
            longitud=lon,
            altitud=alt
        )
        lista_satelites.append(sat)

    return lista_satelites
        
def crear_resumen(catalogo):
    resumen={}
    grupo={}
    
    for sat in catalogo:
        tipo = sat.tipo_orbita()
        if tipo not in grupo:
            grupo[tipo] = []
        grupo[tipo].append(sat.altitud)
    # print(grupo)
    for tipo, lista_altitud in grupo.items():
        suma=0
        if tipo not in resumen:
            resumen[tipo]={}
        minimo=lista_altitud[0]
        maximo =lista_altitud[0]
        for altitud in lista_altitud:
            if altitud < minimo:
                minimo = altitud
            if altitud > maximo:
                maximo = altitud
            suma+=altitud
        cantidad=len(lista_altitud)
        promedio=suma/cantidad
        resumen[tipo]={
            "cantidad": cantidad,
            "minimo": minimo,
            "maximo": maximo,
            "promedio": promedio
        }
    return resumen
def obtener_satelites(lista_satelites, longitud_mínima, latitud_mínima, longitud_máxima, latitud_máxima):
    dentro=[]
    for satelites in lista_satelites:
        if satelites.dentro_zona(longitud_mínima, latitud_mínima, longitud_máxima, latitud_máxima):
            dentro.append(satelites)
    return dentro


# janson=leer_json("datos/satelites.json")
# catalogo=crear_catalogo(janson)
# resumen=crear_resumen(catalogo)
# satelites=obtener_satelites(catalogo, 30, -5, 120, 30)

# for zona in satelites:
#     print(zona.latitud, zona.longitud)