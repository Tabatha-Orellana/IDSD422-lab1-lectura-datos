# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

# TODO 1: carga data/ventas.csv
# TODO 2: imprime los tipos (dtypes) de cada columna
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total

# inspeccion.py — Inspeccion e indicadores (Python)

import pandas as pd

# TODO 1: Cargar los datos CSV
ventas = pd.read_csv("data/ventas.csv")

# TODO 2: Mostrar los tipos de datos
print("--- TIPOS DE DATOS ---")
print(ventas.dtypes)

# TODO 3: Crear la columna ticket
ventas["ticket"] = ventas["ventas"] / ventas["clientes"]

print("\n--- DATOS CON TICKET ---")
print(ventas.head())

# TODO 4: Calcular indicadores

# Venta promedio por sucursal
print("\n--- VENTA PROMEDIO POR SUCURSAL ---")
promedio_sucursal = ventas.groupby("sucursal")["ventas"].mean()
print(promedio_sucursal)

# Ticket promedio general
print("\n--- TICKET PROMEDIO GENERAL ---")
ticket_promedio = ventas["ventas"].sum() / ventas["clientes"].sum()
print(round(ticket_promedio, 2))

# Ventas totales por sucursal
ventas_sucursal = ventas.groupby("sucursal")["ventas"].sum()

# Sucursal con mayor venta
print("\n--- SUCURSAL CON MAYOR VENTA ---")
print(ventas_sucursal.idxmax())
print(ventas_sucursal.max())

# Sucursal con menor venta
print("\n--- SUCURSAL CON MENOR VENTA ---")
print(ventas_sucursal.idxmin())
print(ventas_sucursal.min())

# Region con mayor venta
ventas_region = ventas.groupby("region")["ventas"].sum()

print("\n--- REGION CON MAYOR VENTA ---")
print(ventas_region.idxmax())
print(ventas_region.max())
