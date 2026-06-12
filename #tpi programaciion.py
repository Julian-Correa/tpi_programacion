#tpi programaciion
import csv

ARCHIVO_CSV = "paises.csv"


def cargar_paises_desde_csv(nombre_archivo):
    paises = []

    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }

                    if pais["nombre"] and pais["continente"]:
                        paises.append(pais)

                except (ValueError, KeyError):
                    print("Error: se encontró una fila con formato inválido en el CSV.")

    except FileNotFoundError:
        print("Error: no se encontró el archivo CSV.")

    return paises


def mostrar_pais(pais):
    print(f"Nombre: {pais['nombre']}")
    print(f"Población: {pais['poblacion']}")
    print(f"Superficie: {pais['superficie']} km²")
    print(f"Continente: {pais['continente']}")
    print("-" * 40)


def mostrar_lista_paises(paises):
    if not paises:
        print("No hay países para mostrar.")
        return

    for pais in paises:
        mostrar_pais(pais)


def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("Debe ingresar un número entero válido.")


def agregar_pais(paises):
    nombre = input("Ingrese el nombre del país: ").strip()
    continente = input("Ingrese el continente: ").strip()

    if nombre == "" or continente == "":
        print("Error: no se permiten campos vacíos.")
        return

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Error: ese país ya existe.")
            return

    poblacion = pedir_entero("Ingrese la población: ")
    superficie = pedir_entero("Ingrese la superficie en km²: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    print("País agregado correctamente.")


def actualizar_pais(paises):
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("País encontrado.")
            pais["poblacion"] = pedir_entero("Ingrese la nueva población: ")
            pais["superficie"] = pedir_entero("Ingrese la nueva superficie en km²: ")
            print("Datos actualizados correctamente.")
            return

    print("No se encontró un país con ese nombre.")


def buscar_pais(paises):
    busqueda = input("Ingrese el nombre o parte del nombre: ").strip().lower()

    if busqueda == "":
        print("La búsqueda no puede estar vacía.")
        return

    resultados = []

    for pais in paises:
        if busqueda in pais["nombre"].lower():
            resultados.append(pais)

    mostrar_lista_paises(resultados)


def filtrar_por_continente(paises):
    continente = input("Ingrese el continente: ").strip().lower()

    resultados = []

    for pais in paises:
        if pais["continente"].lower() == continente:
            resultados.append(pais)

    mostrar_lista_paises(resultados)


def filtrar_por_rango_poblacion(paises):
    minimo = pedir_entero("Población mínima: ")
    maximo = pedir_entero("Población máxima: ")

    if minimo > maximo:
        print("Error: el mínimo no puede ser mayor que el máximo.")
        return

    resultados = []

    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)

    mostrar_lista_paises(resultados)


def filtrar_por_rango_superficie(paises):
    minimo = pedir_entero("Superficie mínima: ")
    maximo = pedir_entero("Superficie máxima: ")

    if minimo > maximo:
        print("Error: el mínimo no puede ser mayor que el máximo.")
        return

    resultados = []

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)

    mostrar_lista_paises(resultados)


def menu_filtros(paises):
    while True:
        print("\n--- FILTROS ---")
        print("1. Filtrar por continente")
        print("2. Filtrar por rango de población")
        print("3. Filtrar por rango de superficie")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            filtrar_por_continente(paises)
        elif opcion == "2":
            filtrar_por_rango_poblacion(paises)
        elif opcion == "3":
            filtrar_por_rango_superficie(paises)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")


def ordenar_paises(paises):
    print("\n--- ORDENAMIENTO ---")
    print("1. Ordenar por nombre")
    print("2. Ordenar por población")
    print("3. Ordenar por superficie")

    criterio = input("Seleccione criterio: ")

    print("1. Ascendente")
    print("2. Descendente")
    orden = input("Seleccione orden: ")

    descendente = orden == "2"

    if criterio == "1":
        ordenados = sorted(paises, key=lambda pais: pais["nombre"].lower(), reverse=descendente)
    elif criterio == "2":
        ordenados = sorted(paises, key=lambda pais: pais["poblacion"], reverse=descendente)
    elif criterio == "3":
        ordenados = sorted(paises, key=lambda pais: pais["superficie"], reverse=descendente)
    else:
        print("Criterio inválido.")
        return

    mostrar_lista_paises(ordenados)


def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos para calcular estadísticas.")
        return

    pais_mayor_poblacion = max(paises, key=lambda pais: pais["poblacion"])
    pais_menor_poblacion = min(paises, key=lambda pais: pais["poblacion"])

    total_poblacion = 0
    total_superficie = 0
    cantidad_por_continente = {}

    for pais in paises:
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in cantidad_por_continente:
            cantidad_por_continente[continente] += 1
        else:
            cantidad_por_continente[continente] = 1

    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)

    print("\n--- ESTADÍSTICAS ---")
    print(f"País con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']})")
    print(f"País con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km²")

    print("\nCantidad de países por continente:")
    for continente, cantidad in cantidad_por_continente.items():
        print(f"{continente}: {cantidad}")


def mostrar_menu_principal():
    print("\n===== GESTIÓN DE DATOS DE PAÍSES =====")
    print("1. Mostrar todos los países")
    print("2. Agregar país")
    print("3. Actualizar población y superficie")
    print("4. Buscar país por nombre")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Mostrar estadísticas")
    print("0. Salir")


def main():
    paises = cargar_paises_desde_csv(ARCHIVO_CSV)

    if not paises:
        print("El sistema inició sin datos cargados.")

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_lista_paises(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_pais(paises)
        elif opcion == "5":
            menu_filtros(paises)
        elif opcion == "6":
            ordenar_paises(paises)
        elif opcion == "7":
            mostrar_estadisticas(paises)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


main()