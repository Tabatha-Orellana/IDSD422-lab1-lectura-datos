# leer_csv.py — Cargar el reporte CSV del ERP (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_csv.py

# TODO 1: importa pandas y carga data/ventas.csv en un DataFrame
# TODO 2: imprime las dimensiones (filas, columnas) del DataFrame
# TODO 3: imprime las primeras filas para revisar las columnas
import pandas as pd

# TODO 1: Cargar el archivo CSV en un DataFrame
ventas = pd.read_csv("data/ventas.csv")

# TODO 2: Imprimir las dimensiones
print("--- DIMENSIONES DEL CSV ---")
print(ventas.shape)

# TODO 3: Mostrar las primeras filas
print("\n--- PRIMERAS FILAS DEL CSV ---")
print(ventas.head())