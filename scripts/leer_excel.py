# leer_excel.py — Cargar el consolidado Excel de finanzas (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_excel.py

# TODO 1: importa pandas
# TODO 2: carga data/ventas.xlsx indicando la hoja correcta
# TODO 3: imprime las dimensiones y las primeras filas


import pandas as pd

# TODO 1: Leer el archivo Excel
# TODO 2: Indicar la hoja "ventas"
ventas = pd.read_excel(
    "data/ventas.xlsx",
    sheet_name="ventas"
)

# TODO 3: Mostrar dimensiones
print("--- DIMENSIONES DEL EXCEL ---")
print(ventas.shape)

# TODO 4: Mostrar primeras filas
print("\n--- PRIMERAS FILAS DEL EXCEL ---")
print(ventas.head())
