# 🎓 Sistema Multifacultad de Gestión Académica

Aplicación de escritorio con **interfaz gráfica (Tkinter)** para generar, consultar y exportar registros académicos de estudiantes de distintas facultades. No usa la consola para interactuar con el usuario: todo se hace mediante botones, listas desplegables, tablas y ventanas de diálogo.

---

## 📋 Características

- **Generación aleatoria de estudiantes** (de 1 a 9000) con nombre, código, facultad, semestre, edad, género y notas.
- **Consulta gráfica** filtrando por facultad y semestre, con tabla ordenada y barra de estado.
- **Detalle de notas**: doble clic en un estudiante para ver todas sus asignaturas.
- **Listado por cursos**: estudiantes agrupados por asignatura con su nota definitiva.
- **Consulta por código** de estudiante.
- **Estadísticas generales** y **estadísticas demográficas por facultad**.
- **Exportación a TXT** de informes individuales y de registros por facultad.

---

## 🏛️ Facultades y mallas curriculares

Cada facultad cuenta con una malla de **10 semestres**:

| Código | Facultad |
|--------|----------|
| `ING` | Ingeniería de Sistemas y Computación |
| `MED` | Medicina |
| `DER` | Derecho |
| `ADM` | Administración de Empresas |
| `EDU` | Educación |

---

## 🧮 Reglas de calificación

Cada asignatura tiene tres notas en escala de **1.0 a 5.0**:

| Nota | Peso |
|------|------|
| N1 | 30 % |
| N2 | 30 % |
| N3 | 40 % |

```
Definitiva = N1 × 0.3 + N2 × 0.3 + N3 × 0.4
```

- Una asignatura se considera **aprobada** con definitiva **≥ 3.0**.
- El **promedio del estudiante** es el promedio de las definitivas de sus asignaturas.

---

## 🧾 Datos generados por estudiante

| Campo | Descripción |
|-------|-------------|
| Código | Número único de 4 dígitos (1000–9999) |
| Nombre | Nombre y dos apellidos, sin repetirse |
| Facultad | Una de las 5 facultades |
| Semestre | Entre 1 y 10 |
| Edad | Entre 17 y 45 años |
| Género | `M` o `F`, según el primer nombre |
| Asignaturas | Entre 3 materias y todas las de su semestre, con N1, N2, N3 y definitiva |

> Por el formato de código de 4 dígitos, el máximo es **9000 estudiantes** por generación.

---

## 🖥️ Funciones de la interfaz

### Botones de acciones

| # | Botón | Descripción |
|---|-------|-------------|
| 1 | Generar estudiantes | Pide la cantidad y crea registros aleatorios (reemplaza los anteriores) |
| 2 | Listado por cursos | Muestra cada asignatura con sus estudiantes y notas definitivas |
| 3 | Consultar por código | Busca un estudiante y muestra sus notas |
| 4 | Estadísticas generales | Total de estudiantes, promedio general, facultad con más estudiantes y % de asignaturas aprobadas |
| 5 | Informe individual TXT | Guarda en un `.txt` el informe de un estudiante |
| 6 | Exportar por facultad TXT | Guarda en un `.txt` todos los registros agrupados por facultad |
| 7 | Estadísticas por facultad | Promedio de edad, distribución de género, mayor y menor edad por facultad |

### Consulta gráfica

- Selecciona una **facultad** y/o un **semestre** en las listas desplegables; la tabla se actualiza automáticamente.
- **Consultar** aplica los filtros y **Limpiar** los restablece.
- **Doble clic** sobre una fila abre una ventana con las notas completas del estudiante.

---

## ⚙️ Requisitos

- **Python 3.8 o superior**
- **Tkinter** (incluido con Python en Windows y macOS)
- No requiere instalar librerías externas: solo usa la biblioteca estándar (`random`, `tkinter`, `collections`).

> En algunas distribuciones de Linux hay que instalar Tkinter aparte:
> ```bash
> sudo apt install python3-tk
> ```

---

## ▶️ Ejecución

```bash
python registro_academico.py
```

*(Reemplaza `registro_academico.py` por el nombre real de tu archivo.)*

Al abrirse la ventana, pulsa **«1. Generar estudiantes»** para crear datos y comenzar a consultar.

---

## 🗂️ Estructura del código

| Elemento | Función |
|----------|---------|
| `MALLAS_FACULTADES` | Diccionario con las facultades y sus materias por semestre |
| `NOMBRES`, `APELLIDOS` | Listas para la generación aleatoria de nombres |
| `NOMBRES_MASCULINOS` / `NOMBRES_FEMENINOS` | Conjuntos usados para asignar el género |
| `generar_estudiantes()` | Lógica de generación, independiente de la interfaz |
| `promedio_estudiante()` / `texto_estudiante()` | Cálculo de promedio y formato del reporte |
| `consultar_filtros()` | Actualiza la tabla según los filtros |
| `mostrar_texto()` | Ventana de texto con scroll para reportes |
| `_guardar_txt()` | Diálogo de guardado y escritura de archivos |
| `crear_interfaz()` / `main()` | Construcción de la ventana y arranque de la aplicación |

---

## ⚠️ Limitaciones

- Los datos son **aleatorios y temporales**: se conservan solo mientras la aplicación está abierta.
- Cada nueva generación **reemplaza** los estudiantes existentes.
- El género se asigna por el primer nombre; si no está en las listas, se elige al azar.
- Los informes se exportan únicamente en formato **TXT**.

---

## 🚀 Posibles mejoras

- Guardar y cargar datos desde archivos (JSON/CSV) o una base de datos.
- Registro manual de estudiantes y edición de notas.
- Exportación a PDF o Excel.
- Gráficas de estadísticas.

---

## 📄 Licencia

Proyecto de uso académico y educativo.
