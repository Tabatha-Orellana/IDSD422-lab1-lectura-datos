# leer_json.py — Cargar el reporte JSON de la API (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_json.py

# TODO 1: importa json y pandas
# TODO 2: carga data/ventas.json con json.load
# TODO 3: convierte la lista de diccionarios en un DataFrame
#         (recuerda del cap. 2: el JSON no llega como tabla directa)
# TODO 4: imprime las dimensiones y las primeras filas

# leer_json.py — Cargar el reporte JSON de la API (Python)

import json
import pandas as pd

# TODO 1: Abrir y leer el archivo JSON
with open("data/ventas.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

# TODO 2: Convertir los datos en un DataFrame
ventas = pd.DataFrame(datos)

# TODO 3: Imprimir las dimensiones
print("--- DIMENSIONES DEL JSON ---")
print(ventas.shape)

# TODO 4: Mostrar las primeras filas
print("\n--- PRIMERAS FILAS DEL JSON ---")
print(ventas.head())
