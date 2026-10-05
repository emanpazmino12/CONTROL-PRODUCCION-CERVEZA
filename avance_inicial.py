"""Paso 1: primer avance; registro y consulta en memoria."""
lotes = []
while True:
    print("\n1. Registrar lote\n2. Consultar lotes\n3. Salir")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        codigo = input("Código: ").strip().upper()
        estilo = input("Estilo: ").strip()
        try:
            litros = float(input("Litros: "))
            if not codigo or not estilo or not 0 < litros < float("inf"):
                raise ValueError
            if any(l["codigo"] == codigo for l in lotes):
                print("Código repetido.")
            else:
                lotes.append(dict(codigo=codigo, estilo=estilo, litros=litros))
                print("Lote registrado.")
        except ValueError:
            print("Datos inválidos.")
    elif opcion == "2":
        if not lotes:
            print("No hay lotes.")
        for lote in lotes:
            print(lote)
    elif opcion == "3":
        break
    else:
        print("Opción inválida.")
