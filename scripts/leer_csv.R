# leer_csv.R — Cargar el reporte CSV del ERP (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/leer_csv.R

# TODO 1: carga data/ventas.csv con readr::read_csv en un data.frame
# TODO 2: imprime las dimensiones (dim) del data.frame
# TODO 3: imprime las primeras filas (head) para revisar las columnas

# leer_csv.R — Cargar el reporte CSV del ERP (R)

# TODO 1: Cargar data/ventas.csv con readr::read_csv()
ventas <- readr::read_csv(
  "data/ventas.csv",
  show_col_types = FALSE
)

# TODO 2: Imprimir las dimensiones
cat("--- DIMENSIONES DEL CSV ---\n")
print(dim(ventas))

# TODO 3: Mostrar las primeras filas
cat("\n--- PRIMERAS FILAS DEL CSV ---\n")
print(head(ventas))
