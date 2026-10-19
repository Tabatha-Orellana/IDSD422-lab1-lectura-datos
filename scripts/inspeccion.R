# inspeccion.R — Tipos, columna derivada e indicadores (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/inspeccion.R

# TODO 1: carga data/ventas.csv
# TODO 2: imprime la estructura (str) para ver los tipos
#         (fija si region llegó como character o factor)
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal (aggregate o dplyr)
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total

# inspeccion.R — Inspección e indicadores comerciales (R)

# TODO 1: Cargar los datos
ventas <- readr::read_csv(
  "data/ventas.csv",
  show_col_types = FALSE
)

# TODO 2: Inspeccionar estructura y tipos
cat("--- ESTRUCTURA Y TIPOS DE DATOS ---\n")
str(ventas)

# TODO 3: Crear la columna ticket
ventas$ticket <- ventas$ventas / ventas$clientes

cat("\n--- DATOS CON TICKET ---\n")
print(head(ventas))

# TODO 4: Calcular los indicadores

# Venta promedio por sucursal
cat("\n--- VENTA PROMEDIO POR SUCURSAL ---\n")
promedio_sucursal <- aggregate(
  ventas$ventas,
  by = list(sucursal = ventas$sucursal),
  FUN = mean
)
names(promedio_sucursal)[2] <- "venta_promedio"
print(promedio_sucursal)

# Ticket promedio general
cat("\n--- TICKET PROMEDIO GENERAL ---\n")
ticket_promedio <- sum(ventas$ventas) / sum(ventas$clientes)
print(round(ticket_promedio, 2))

# Ventas totales por sucursal
ventas_sucursal <- aggregate(
  ventas$ventas,
  by = list(sucursal = ventas$sucursal),
  FUN = sum
)
names(ventas_sucursal)[2] <- "venta_total"

# Sucursal con mayor venta
cat("\n--- SUCURSAL CON MAYOR VENTA ---\n")
mayor <- ventas_sucursal[
  which.max(ventas_sucursal$venta_total),
]
print(mayor)

# Sucursal con menor venta
cat("\n--- SUCURSAL CON MENOR VENTA ---\n")
menor <- ventas_sucursal[
  which.min(ventas_sucursal$venta_total),
]
print(menor)

# Ventas totales por region
ventas_region <- aggregate(
  ventas$ventas,
  by = list(region = ventas$region),
  FUN = sum
)
names(ventas_region)[2] <- "venta_total"

# Region con mayor venta
cat("\n--- REGION CON MAYOR VENTA ---\n")
region_mayor <- ventas_region[
  which.max(ventas_region$venta_total),
]
print(region_mayor)
