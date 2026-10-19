# leer_json.R — Cargar el reporte JSON de la API (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/leer_json.R

# TODO 1: carga data/ventas.json con jsonlite::fromJSON
# TODO 2: convierte el resultado en data.frame si hace falta
# TODO 3: imprime las dimensiones (dim) y las primeras filas (head)


# TODO 1: Cargar los datos desde JSON
datos <- jsonlite::fromJSON("data/ventas.json")

# TODO 2: Convertir a data.frame
ventas <- as.data.frame(datos)

# TODO 3: Imprimir dimensiones
cat("--- DIMENSIONES DEL JSON ---\n")
print(dim(ventas))

# TODO 4: Mostrar las primeras filas
cat("\n--- PRIMERAS FILAS DEL JSON ---\n")
print(head(ventas))
