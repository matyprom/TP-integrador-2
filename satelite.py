class Satelite:
    def __init__(self, nombre, num_catalogo, latitud, longitud, altitud):
        self.nombre = nombre
        self.num_catalogo = num_catalogo
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

    def verificar_nombre(self):
        if self.nombre != " ":
            return True
        return False
    def verificar_num_catalogo(self):
        if int(self.num_catalogo):
            return True
        return False
    def verificar_latitud(self):
        if self.latitud<=90 and self.latitud>=-90:
            return True
        return False
    def verificar_longitud(self):
        if self.longitud<=180 and self.longitud>=-180:
            return True
        return False

    def verificar_altitud(self):
        if self.altitud>=100:
            return True
        return False
    def tipo_orbita(self):
        if self.altitud<2000:
            return "LEO"
        if self.altitud>=2000 and self.altitud<34000(self):
            return "MEO"
        if self.altitud>=34000 and self.altitud<=37000(self):
            return "GEO"
        if self.altitud>37000:
            return "HEO"
    def resumen_datos(self, tipo):
        return f"{self.nombre} | {self.num_catalogo} | {tipo} | {self.altitud} km"
    def dentro_zona(self, longitud_mínima, latitud_mínima, longitud_máxima, latitud_máxima):
        if self.longitud>=longitud_mínima and self.longitud<=longitud_máxima:
            if self.latitud>=latitud_mínima and self.latitud<=latitud_máxima:
                return True
        return False

    
    