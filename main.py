#tpi programaciion
import csv
import os

# Obtener el directorio donde está el script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_CSV = os.path.join(SCRIPT_DIR, "paises.csv")

#funciones

def cargar_paises_desde_csv(nombre_archivo):
    paises = []

    try:
        #abrimos el archivo csv en modo lectura
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            #guardamos la información de cada país por separado en el arreglo paises
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }

                    #lo agregamos después de verificar que el país tenga nombre y continente
                    if pais["nombre"] and pais["continente"]:
                        paises.append(pais)

                except (ValueError, KeyError):
                    print("\nError: se encontró una fila con formato inválido en el CSV.")

    except FileNotFoundError:
        print("\nError: no se encontró el archivo CSV.")

    return paises


def mostrar_pais(pais):
    #Mostramos la información del país en cada print
    print(f"Nombre: {pais['nombre']}")
    print(f"Población: {pais['poblacion']}")
    print(f"Superficie: {pais['superficie']} km²")
    print(f"Continente: {pais['continente']}")
    print("-" * 40)


def mostrar_lista_paises(paises):
    #En caso de que no haya paises
    if not paises:
        print("\nNo hay países para mostrar.")
        return

    #por cada país en paises llamamos a otra función para hacer esa tarea
    for pais in paises:
        mostrar_pais(pais)


def pedir_entero(mensaje):
    #Lo usamos para validar que no se ingrese un número negativo. 
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("\nEl valor no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("\nDebe ingresar un número entero válido.")


def agregar_pais(paises):
    #Agregamos un nuevo país con tus datos y validamos que los datos ingresados sean los correspondientes
    nombre = input("Ingrese el nombre del país: ").strip()
    continente = input("Ingrese el continente: ").strip()

    if nombre == "" or continente == "":
        print("\nError: no se permiten campos vacíos.")
        return

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Error: ese país ya existe.")
            return

    poblacion = pedir_entero("Ingrese la población: ")
    superficie = pedir_entero("Ingrese la superficie en km²: ")

    #guardamos los datos validados 
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    #Agregamos el nuevo país al final del arreglo de paises.
    paises.append(nuevo_pais)
    print("\nPaís agregado correctamente.")


def actualizar_pais(paises):
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()

    for pais in paises:
        #Cuando el nombre del país ingresado coincida con uno de los paises, se lo modifica
        if pais["nombre"].lower() == nombre.lower():
            print("País encontrado.")
            pais["poblacion"] = pedir_entero("Ingrese la nueva población: ")
            pais["superficie"] = pedir_entero("Ingrese la nueva superficie en km²: ")
            print("Datos actualizados correctamente.")
            return

    print("\nNo se encontró un país con ese nombre.")


def buscar_pais(paises):
    busqueda = input("Ingrese el nombre o parte del nombre: ").strip().lower()

    if busqueda == "":
        print("\nLa búsqueda no puede estar vacía.")
        return

    #Creamos otro arreglo vacío para mostrar los resultados de la búsqueda
    resultados = []

    for pais in paises:
        #En caso de que alguna parte del nombre coincida con algún país lo agregamos en el arreglo nuevo
        if busqueda in pais["nombre"].lower():
            resultados.append(pais)

    mostrar_lista_paises(resultados) #mostramos los países que coinciden


def filtrar_por_continente(paises):
    continente = input("Ingrese el continente: ").strip().lower()
    #igual que buscar por pais pero en este caso por continente
    resultados = []

    for pais in paises:
        if pais["continente"].lower() == continente:
            resultados.append(pais)

    mostrar_lista_paises(resultados)


def filtrar_por_rango_poblacion(paises):
    #Guardamos los límites del rango
    minimo = pedir_entero("Población mínima: ")
    maximo = pedir_entero("Población máxima: ")

    if minimo > maximo:
        print("\nError: el mínimo no puede ser mayor que el máximo.")
        return

    #guardamos los paises que esten dentro del rango de población
    resultados = []

    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)

    mostrar_lista_paises(resultados)


def filtrar_por_rango_superficie(paises):
    #Guardamos los límites del rango 
    minimo = pedir_entero("Superficie mínima: ")
    maximo = pedir_entero("Superficie máxima: ")

    if minimo > maximo:
        print("\nError: el mínimo no puede ser mayor que el máximo.")
        return

    #guardamos los paises que esten dentro del rango de superficie
    resultados = []

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)

    mostrar_lista_paises(resultados)


def menu_filtros(paises):
    #Generamos un menu para elegir el filtro a usar y llamamos a la función corresondiente
    while True:
        print("\n--- FILTROS ---")
        print("1. Filtrar por continente")
        print("2. Filtrar por rango de población")
        print("3. Filtrar por rango de superficie")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1": filtrar_por_continente(paises)
        elif opcion == "2": filtrar_por_rango_poblacion(paises)
        elif opcion == "3": filtrar_por_rango_superficie(paises)
        elif opcion == "0":
            break
        else:
            print("\nOpción inválida.")


def ordenar_paises(paises):
    #Generamos un menu para elegir la forma de ordenar 

    print("\n--- ORDENAMIENTO ---")
    print("1. Ordenar por nombre")
    print("2. Ordenar por población")
    print("3. Ordenar por superficie")

    criterio = input("\nSeleccione criterio: ")

    print("1. Ascendente")
    print("2. Descendente")
    orden = input("\nSeleccione orden: ")

    #En caso de elegir la opción 2 la variable queda en True
    descendente = orden == "2"

    #Creamos una nueva lista ordenada según nombre, población o pais, sin modificar la original
    #Solo ordena de forma descendente cuando dicha variable sea True
    if criterio == "1":
        ordenados = sorted(paises, key=lambda pais: pais["nombre"].lower(), reverse=descendente)
    elif criterio == "2":
        ordenados = sorted(paises, key=lambda pais: pais["poblacion"], reverse=descendente)
    elif criterio == "3":
        ordenados = sorted(paises, key=lambda pais: pais["superficie"], reverse=descendente)
    else:
        print("\nCriterio inválido.")
        return

    mostrar_lista_paises(ordenados)


def mostrar_estadisticas(paises):
    if not paises:
        print("\nNo hay datos para calcular estadísticas.")
        return

    #Guardamos el pais con mayor y menor población
    pais_mayor_poblacion = max(paises, key=lambda pais: pais["poblacion"])
    pais_menor_poblacion = min(paises, key=lambda pais: pais["poblacion"])

    total_poblacion = 0
    total_superficie = 0

    #Creamos un nuevo arreglo con la cantidad de paises según su continente
    cantidad_por_continente = {}

    for pais in paises:

        #Sumamos la población y la superficie para calcular los promedios
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

        continente = pais["continente"]

        #Vamos sumando la cantidad de país por continente
        if continente in cantidad_por_continente:
            cantidad_por_continente[continente] += 1
        else:
            cantidad_por_continente[continente] = 1

    #Calculamos los promedios
    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)


    #Mostramos los resultados
    print("\n--- ESTADÍSTICAS ---")
    print(f"País con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']})")
    print(f"País con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km²")

    print("\nCantidad de países por continente:")
    for continente, cantidad in cantidad_por_continente.items():
        print(f"{continente}: {cantidad}")


def mostrar_menu_principal():
    #mostramos por pantalla el menú
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
    #Llamamos a la función para leer el archivo csv y obtener los paises

    paises = cargar_paises_desde_csv(ARCHIVO_CSV)

    if not paises:
        print("\nEl sistema inició sin datos cargados.")

    while True:
        #Llamamos a la función que muestra el menú por pantalla
        mostrar_menu_principal()

        #Según la opción elegida llamamos a la función correspondiente
        opcion = input("Seleccione una opción: ")

        if opcion == "1": mostrar_lista_paises(paises)
        elif opcion == "2": agregar_pais(paises)
        elif opcion == "3": actualizar_pais(paises)
        elif opcion == "4": buscar_pais(paises)
        elif opcion == "5": menu_filtros(paises)
        elif opcion == "6": ordenar_paises(paises)
        elif opcion == "7": mostrar_estadisticas(paises)
        elif opcion == "0":
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")

#iniciamos llamando a la función principal main
main()