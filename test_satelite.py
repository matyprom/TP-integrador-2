from satelite import Satelite



def test_verificar_nombre_valido():
    sat_valido = Satelite("ISS (ZARYA)", 25544, -10.5, -40.2, 420.0)
    assert sat_valido.verificar_nombre() == True
def test_nombre_invalido():
    sat_invalido = Satelite(" ", 25544, -10.5, -40.2, 420.0)
    assert sat_invalido.verificar_nombre() == False


def test_num_catalogo_valido():
    sat_valido = Satelite("ISS", 25544, 0.0, 0.0, 500.0)
    assert sat_valido.verificar_num_catalogo() == True
def test_num_catalogo_valido():
    sat_valido = Satelite("ISS", 5.2, 0.0, 0.0, 500.0)
    assert sat_valido.verificar_num_catalogo() == False


def test_latitud_valida():
    sat_ok = Satelite("ISS", 25544, 45.0, 0.0, 500.0)
    assert sat_ok.verificar_latitud() == True
def test_latitud_invalido():
    sat_error = Satelite("ISS", 25544, 95.0, 0.0, 500.0)
    assert sat_error.verificar_latitud() == False


def test_longitud_valida():
    sat_ok = Satelite("ISS", 25544, 0.0, -120.0, 500.0)
    assert sat_ok.verificar_longitud() == True
def test_longitud_invalida():
    sat_error = Satelite("ISS", 25544, 0.0, 200.0, 500.0)
    assert sat_error.verificar_longitud() == False


def test_altitud_valida():
    sat_ok = Satelite("ISS", 25544, 0.0, 0.0, 400.0)
    assert sat_ok.verificar_altitud() == True
def test_altitud_inalida():
    sat_error = Satelite("ISS", 25544, 0.0, 0.0, 50.0)
    assert sat_error.verificar_altitud() == False

def test_tipo_orbita():
    leo = Satelite("SatLEO", 1001, 0.0, 0.0, 500.0)
    meo = Satelite("SatMEO", 1002, 0.0, 0.0, 20000.0)
    geo = Satelite("SatGEO", 1003, 0.0, 0.0, 35786.0)
    heo = Satelite("SatHEO", 1004, 0.0, 0.0, 40000.0)

    assert leo.tipo_orbita() == "LEO"
    assert meo.tipo_orbita() == "MEO"
    assert geo.tipo_orbita() == "GEO"
    assert heo.tipo_orbita() == "HEO"


def test_resumen_datos():
    sat = Satelite("HUBBLE", 20580, 10.0, 20.0, 535.0)
    tipo = sat.tipo_orbita()
    assert sat.resumen_datos(tipo) == "HUBBLE | 20580 | LEO | 535.0 km"


def test_dentro_zona_valido():
    sat = Satelite("TestSat", 12345, 10.0, 50.0, 400.0)
    assert sat.dentro_zona(30, -5, 120, 30) == True
def test_dentro_zona_invalido():
    sat = Satelite("TestSat", 12345, 10.0, 50.0, 400.0)
    assert sat.dentro_zona(-100, -5, -10, 30) == False