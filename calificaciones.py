"""Gestor de Calificaciones - app pequeña para practicar pruebas de software."""

APROBATORIA = 6.0
alumnos = {}  # nombre -> lista de calificaciones


def validar_calificacion(valor):
    """RF1: acepta números de 0 a 10."""
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise TypeError("La calificación debe ser numérica")
    if valor < 0 or valor > 10:
        raise ValueError("La calificación debe estar entre 0 y 10")
    return valor


def registrar_alumno(nombre):
    """RF2: registra un alumno nuevo."""
    nombre = nombre.strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacío")
    if nombre in alumnos:
        raise ValueError("El alumno ya existe")
    alumnos[nombre] = []
    return nombre


def agregar_calificacion(nombre, valor):
    """RF3: agrega una calificación a un alumno existente."""
    if nombre not in alumnos:
        raise KeyError("Alumno no encontrado")
    alumnos[nombre].append(validar_calificacion(valor))


def calcular_promedio(nombre):
    """RF4: promedio de un alumno (0 si no tiene calificaciones)."""
    califs = alumnos[nombre]
    if not califs:
        return 0.0
    return round(sum(califs) / len(califs), 2)


def obtener_estado(nombre):
    """RF5: 'Aprobado' si promedio >= 6, si no 'Reprobado'."""
    return "Aprobado" if calcular_promedio(nombre) >= APROBATORIA else "Reprobado"


def mejor_alumno():
    """RF6: devuelve (nombre, promedio) del mejor promedio."""
    if not alumnos:
        return None
    mejor = max(alumnos, key=calcular_promedio)
    return mejor, calcular_promedio(mejor)


def menu():
    while True:
        op = input("\n1) Registrar alumno  2) Agregar calificación  3) Ver estado  4) Mejor alumno  5) Salir: ")
        try:
            if op == "1":
                registrar_alumno(input("Nombre: "))
            elif op == "2":
                agregar_calificacion(input("Nombre: "), float(input("Calificación: ")))
            elif op == "3":
                n = input("Nombre: ")
                print(n, calcular_promedio(n), obtener_estado(n))
            elif op == "4":
                print(mejor_alumno())
            elif op == "5":
                break
        except (ValueError, TypeError, KeyError) as e:
            print("Error:", e)


if __name__ == "__main__":
    menu()
