# Laboratorio 1: Consolidación de reportes de ventas

**Asignatura:** IDSD422 — Estadística y Programación para Ciencia de Datos I  
**Período académico:** 2026-B  
**Caso:** RetailAndina S.A.  
**Entorno utilizado:** Visual Studio Code (Windows, terminal PowerShell)  
**Lenguajes:** Python y R

## Contexto del caso

RetailAndina S.A. es una cadena ecuatoriana de tiendas de consumo masivo con sucursales en Quito, Guayaquil y Cuenca. Su equipo de Business Intelligence (BI) recibe un reporte semanal de ventas desde tres sistemas: el ERP de sucursales (`ventas.csv`), la API de fidelización (`ventas.json`) y el consolidado de Finanzas (`ventas.xlsx`).

El objetivo es leer los tres archivos, verificar si representan los mismos registros, inspeccionar filas, columnas y tipos de datos, y calcular indicadores útiles para la gerencia.

## Objetivos del laboratorio

- Leer CSV, JSON y Excel utilizando Python y R.
- Comparar dimensiones, estructura y contenido de los archivos.
- Inspeccionar los tipos de las variables `sucursal`, `region`, `ventas` y `clientes`.
- Calcular venta promedio por sucursal, ticket promedio, sucursal con mayor y menor venta y región con mayor venta total.
- Documentar los resultados y registrar el trabajo en GitHub mediante commits.

## Estructura del repositorio

```text
IDSD422-lab1-lectura-datos/
├── data/
│   ├── ventas.csv
│   ├── ventas.json
│   └── ventas.xlsx
├── scripts/
│   ├── leer_csv.py
│   ├── leer_json.py
│   ├── leer_excel.py
│   ├── inspeccion.py
│   ├── leer_csv.R
│   ├── leer_json.R
│   ├── leer_excel.R
│   └── inspeccion.R
├── informes/                 # Se agrega aquí el PDF final
├── README.md
├── informe.md
└── EVALUACION.md
```

## Requisitos

- Visual Studio Code y Git.
- Python 3.9 o superior, con `pandas` y `openpyxl`.
- R 4.x, con `readr`, `jsonlite` y `readxl`.

Instalación de bibliotecas de Python (PowerShell):

```powershell
python -m pip install pandas openpyxl
```

Instalación de paquetes de R (PowerShell, cuando `Rscript` ya esté reconocido):

```powershell
Rscript -e "install.packages(c('readr','jsonlite','readxl'), repos='https://cloud.r-project.org')"
```

> En Windows, si R no está en el PATH o la biblioteca del sistema está protegida, configura la ubicación de `Rscript.exe` y una biblioteca personal antes de instalar los paquetes. No es necesario instalar Google Colab ni Posit Cloud para trabajar en VS Code.

## Cómo ejecutar los programas

**Todos los comandos se ejecutan desde la raíz del repositorio**, donde están las carpetas `data/` y `scripts/`.

### Python

```powershell
python scripts/leer_csv.py
python scripts/leer_json.py
python scripts/leer_excel.py
python scripts/inspeccion.py
```

### R

```powershell
Rscript scripts/leer_csv.R
Rscript scripts/leer_json.R
Rscript scripts/leer_excel.R
Rscript scripts/inspeccion.R
```

Los scripts de lectura presentan las dimensiones y los primeros registros. Los scripts de inspección muestran la estructura y calculan indicadores.

## Resultados del conjunto de datos

Los tres archivos contienen **5 filas y 4 columnas** con los mismos registros y valores. Las variables originales son `sucursal`, `region`, `ventas` y `clientes`.

| Indicador | Resultado |
|---|---:|
| Ventas totales | 60.040 |
| Clientes totales | 1.577 |
| Ticket promedio general (`sum(ventas) / sum(clientes)`) | 38,07 |
| Sucursal con mayor venta | Guayaquil Centro: 15.200 |
| Sucursal con menor venta | Cuenca: 8.540 |
| Región con mayor venta | Sierra: 30.860 |

### Ventas por sucursal

| Sucursal | Venta promedio por registro |
|---|---:|
| Quito Norte | 12.450 |
| Quito Sur | 9.870 |
| Guayaquil Centro | 15.200 |
| Guayaquil Norte | 13.980 |
| Cuenca | 8.540 |

Cada sucursal tiene un registro en los archivos de este laboratorio; por ello, la venta promedio por sucursal coincide con su venta registrada. Los resultados se refieren solo al conjunto de datos proporcionado.

## Documentación y entrega

- `informe.md`: informe técnico con comparación, resultados, respuestas y conclusiones.
- `EVALUACION.md`: rúbrica específica del laboratorio.
- `informes/`: carpeta donde se guarda el PDF final basado en la plantilla del curso, con capturas reales de ejecución.

La entrega en el aula virtual requiere el PDF y el enlace público de este fork. Los commits separados de Python, R y documentación registran el avance del trabajo.

## Fuentes técnicas

- pandas development team. *pandas.read_csv*. https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
- pandas development team. *pandas.read_excel*. https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
- Wickham, H., Hester, J. y Bryan, J. *readr*. https://readr.tidyverse.org/
- Ooms, J. *jsonlite*. https://cran.r-project.org/package=jsonlite
- Wickham, H. y Bryan, J. *readxl*. https://readxl.tidyverse.org/

**Origen de los datos:** archivos `data/` suministrados con el repositorio del laboratorio de IDSD422.
