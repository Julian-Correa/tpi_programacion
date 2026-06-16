# Gestión de Datos de Países en Python

## Trabajo Práctico Integrador – Programación 1

### Integrantes

* Julián Correa
* Agustin Fassola

### Descripción

Este proyecto consiste en una aplicación desarrollada en Python que permite gestionar información de países mediante el uso de listas, diccionarios, funciones, estructuras condicionales y repetitivas, archivos CSV, filtros, ordenamientos y estadísticas.

Los datos son cargados desde un archivo CSV y almacenados en memoria para su procesamiento.

---

## Tecnologías utilizadas

* Python 3.x
* Archivo CSV
* Listas
* Diccionarios
* Funciones
* Estructuras condicionales
* Estructuras repetitivas

---

## Estructura del proyecto

```
tpi_paises_python/
│
├── main.py
├── paises.csv
├── README.md
└── informe_tpi.pdf
```

---

## Dataset

Cada país contiene la siguiente información:

* Nombre
* Población
* Superficie (km²)
* Continente

Ejemplo:

```
nombre,poblacion,superficie,continente
Argentonia,45000000,2780000,América
Brasilia,210000000,8510000,América
```

---

## Funcionalidades

El sistema permite:

1. Mostrar todos los países.
2. Agregar un nuevo país.
3. Actualizar población y superficie.
4. Buscar países por nombre.
5. Filtrar países por:

   * Continente
   * Rango de población
   * Rango de superficie
6. Ordenar países por:

   * Nombre
   * Población
   * Superficie
7. Mostrar estadísticas:

   * País con mayor población.
   * País con menor población.
   * Promedio de población.
   * Promedio de superficie.
   * Cantidad de países por continente.

---

## Ejecución

1. Descargar el repositorio.
2. Verificar que el archivo `paises.csv` se encuentre en la misma carpeta que `main.py`.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar:

```bash
python main.py
```

---

## Ejemplo de uso

```
===== GESTIÓN DE DATOS DE PAÍSES =====

1. Mostrar todos los países
2. Agregar país
3. Actualizar población y superficie
4. Buscar país por nombre
5. Filtrar países
6. Ordenar países
7. Mostrar estadísticas
0. Salir
```

---

## Video demostración

Link al video:

https://www.youtube.com/watch?v=J4RMf-k-IeI

---

## Documentación PDF

Link al informe:

https://docs.google.com/document/d/11Pakv8uQ7MDLrUc0R07dOpd6gdpfj7VW1YPuB3lbutk/edit?usp=sharing
