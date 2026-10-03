import pytest
import calificaciones as c


@pytest.fixture(autouse=True)
def limpiar():
    c.alumnos.clear()


# CP-01 / RF1 validar calificación
def test_cp01_calificacion_valida():
    assert c.validar_calificacion(8.5) == 8.5

def test_cp02_limites_validos():
    assert c.validar_calificacion(0) == 0 and c.validar_calificacion(10) == 10

def test_cp03_fuera_de_rango():
    with pytest.raises(ValueError):
        c.validar_calificacion(10.1)
    with pytest.raises(ValueError):
        c.validar_calificacion(-1)

def test_cp04_tipo_invalido():
    with pytest.raises(TypeError):
        c.validar_calificacion("diez")

def test_cp05_booleano_no_es_calificacion():
    with pytest.raises(TypeError):
        c.validar_calificacion(True)

# RF2 registrar alumno
def test_cp06_registrar_alumno():
    assert c.registrar_alumno("  Ana ") == "Ana"

def test_cp07_nombre_vacio():
    with pytest.raises(ValueError):
        c.registrar_alumno("   ")

def test_cp08_alumno_duplicado():
    c.registrar_alumno("Ana")
    with pytest.raises(ValueError):
        c.registrar_alumno("Ana")

# RF3 agregar calificación
def test_cp09_agregar_a_alumno_inexistente():
    with pytest.raises(KeyError):
        c.agregar_calificacion("Luis", 8)

# RF4 promedio
def test_cp10_promedio_normal():
    c.registrar_alumno("Ana"); c.agregar_calificacion("Ana", 8); c.agregar_calificacion("Ana", 9)
    assert c.calcular_promedio("Ana") == 8.5

def test_cp11_promedio_sin_calificaciones():
    c.registrar_alumno("Ana")
    assert c.calcular_promedio("Ana") == 0.0

# RF5 estado
def test_cp12_aprobado_en_limite():
    c.registrar_alumno("Ana"); c.agregar_calificacion("Ana", 6)
    assert c.obtener_estado("Ana") == "Aprobado"

def test_cp13_reprobado():
    c.registrar_alumno("Ana"); c.agregar_calificacion("Ana", 5.9)
    assert c.obtener_estado("Ana") == "Reprobado"

# RF6 mejor alumno
def test_cp14_mejor_alumno():
    for n, v in (("Ana", 7), ("Beto", 9)):
        c.registrar_alumno(n); c.agregar_calificacion(n, v)
    assert c.mejor_alumno() == ("Beto", 9.0)

def test_cp15_mejor_alumno_sin_datos():
    assert c.mejor_alumno() is None
