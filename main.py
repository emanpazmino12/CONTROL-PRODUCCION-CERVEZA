"""Control de producción de cerveza: proyecto académico de consola."""
import json
import math
from datetime import date
from pathlib import Path

ARCHIVO = Path(__file__).with_name("lotes.json")
ESTADOS = ("Elaboración", "Fermentación", "Maduración", "Envasado")

def cargar():
    if not ARCHIVO.exists():
        return []
    # No sobrescribir datos cuando el archivo está dañado.
    datos = json.loads(ARCHIVO.read_text(encoding="utf-8"))
    if not isinstance(datos, list) or any(
        not isinstance(l, dict) or not {"codigo", "estilo", "litros", "fecha", "estado"} <= l.keys()
        or not isinstance(l["litros"], (int, float)) or not math.isfinite(l["litros"])
        or l["litros"] <= 0 or l["estado"] not in ESTADOS for l in datos
    ):
        raise ValueError("Estructura de datos inválida")
    return datos

def guardar(lotes):
    # Reemplazar el archivo solo después de escribir los datos completos.
    temporal = ARCHIVO.with_suffix(".tmp")
    temporal.write_text(json.dumps(lotes, ensure_ascii=False, indent=2), encoding="utf-8")
    temporal.replace(ARCHIVO)

def texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Este campo no puede estar vacío.")

def registrar(lotes):
    codigo = texto("Código del lote: ").upper()
    if any(l["codigo"] == codigo for l in lotes):
        print("Ya existe un lote con ese código.")
        return
    estilo = texto("Estilo de cerveza: ")
    while True:
        try:
            litros = float(input("Litros producidos: ").replace(",", "."))
            if not math.isfinite(litros) or litros <= 0:
                raise ValueError
            break
        except ValueError:
            print("Ingresa un número mayor que cero.")
    while True:
        fecha = texto("Fecha de elaboración (AAAA-MM-DD): ")
        try:
            if date.fromisoformat(fecha).isoformat() != fecha:
                raise ValueError
            break
        except ValueError:
            print("Ingresa una fecha válida, por ejemplo 2026-10-05.")
    nuevos = lotes + [dict(codigo=codigo, estilo=estilo, litros=litros,
                           fecha=fecha, estado=ESTADOS[0])]
    guardar(nuevos)
    lotes[:] = nuevos
    print("Lote registrado y guardado.")

def consultar(lotes):
    if not lotes:
        print("No hay lotes registrados.")
        return
    for lote in lotes:
        print(f"{lote['codigo']} | {lote['estilo']} | {lote['litros']:g} L | "
              f"{lote['fecha']} | {lote['estado']}")

def actualizar(lotes):
    codigo = texto("Código del lote a actualizar: ").upper()
    for indice, lote in enumerate(lotes):
        if lote["codigo"] == codigo:
            for numero, estado in enumerate(ESTADOS, 1):
                print(f"{numero}. {estado}")
            opcion = input("Selecciona el estado: ").strip()
            if opcion not in ("1", "2", "3", "4"):
                print("Estado inválido; no se realizaron cambios.")
                return
            nuevos = [dict(l) for l in lotes]
            nuevos[indice]["estado"] = ESTADOS[int(opcion) - 1]
            guardar(nuevos)
            lotes[:] = nuevos
            print("Estado actualizado y guardado.")
            return
    print("No se encontró el lote.")

def resumen(lotes):
    print(f"Lotes registrados: {len(lotes)}")
    print(f"Litros registrados: {sum(l['litros'] for l in lotes):g} L")
    for estado in ESTADOS:
        cantidad = sum(1 for l in lotes if l["estado"] == estado)
        print(f"{estado}: {cantidad} lotes")

def main():
    try:
        lotes = cargar()
    except (OSError, ValueError):
        print("No se pudieron cargar los datos. Revisa lotes.json antes de continuar.")
        return
    # El while mantiene activo el menú hasta que el usuario selecciona salir.
    while True:
        print("\nCONTROL DE PRODUCCIÓN DE CERVEZA")
        print("1. Registrar lote\n2. Consultar lotes\n3. Actualizar estado\n4. Resumen\n5. Salir")
        opcion = input("Selecciona una opción: ").strip()
        try:
            if opcion == "1":
                registrar(lotes)
            elif opcion == "2":
                consultar(lotes)
            elif opcion == "3":
                actualizar(lotes)
            elif opcion == "4":
                resumen(lotes)
            elif opcion == "5":
                print("Programa finalizado.")
                break
            else:
                print("Opción inválida.")
        except OSError:
            print("No se pudo guardar. Comprueba los permisos y el espacio disponible.")

if __name__ == "__main__":
    main()
