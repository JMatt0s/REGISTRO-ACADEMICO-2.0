import random
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
from collections import defaultdict

# Mallas curriculares originales de ren_2_5
MALLAS_FACULTADES = {
    "ING": {"nombre": "Ingeniería de Sistemas y Computación", "semestres": {
        1: ["Cálculo Diferencial", "Introducción a la Ing. de Sistemas", "Programación Básica", "Álgebra Lineal", "Competencias Comunicativas"],
        2: ["Cálculo Integral", "Programación Orientada a Objetos", "Matemáticas Discretas", "Física Mecánica", "Circuitos Digitales"],
        3: ["Cálculo Vectorial", "Estructuras de Datos", "Teoría de Grafos", "Física de Campos", "Arquitectura de Computadores"],
        4: ["Probabilidad y Estadística", "Algoritmos y Complejidad", "Sistemas Operativos", "Bases de Datos I", "Ingeniería de Software I"],
        5: ["Métodos Numéricos", "Redes de Computadores", "Bases de Datos II", "Ingeniería de Software II", "Interacción Humano-Computador"],
        6: ["Investigación de Operaciones", "Seguridad Informática", "Gestión de Proyectos TI", "Arquitectura de Software", "Electiva Sociohumanística"],
        7: ["Inteligencia Artificial", "Cloud Computing y DevOps", "Auditoría de Sistemas", "Seminario de Investigación I", "Electiva Profesional I"],
        8: ["Machine Learning", "Desarrollo Web y Móvil", "Minería de Datos", "Seminario de Investigación II", "Electiva Profesional II"],
        9: ["Big Data y Analítica", "Internet de las Cosas (IoT)", "Gerencia Informática", "Trabajo de Grado I", "Ética Profesional"],
        10: ["Blockchain y Criptografía", "Computación Cuántica", "Trabajo de Grado II", "Práctica Profesional"]}},
    "MED": {"nombre": "Medicina", "semestres": {
        1: ["Biología Celular y Molecular", "Anatomía Humana I", "Bioquímica", "Histología", "Introducción a la Medicina"],
        2: ["Anatomía Humana II", "Fisiología Humana I", "Embriología", "Genética Médica", "Salud Pública I"],
        3: ["Fisiología Humana II", "Microbiología y Parasitología", "Inmunología", "Patología General", "Semiología I"],
        4: ["Farmacología I", "Semiología II", "Fisiopatología", "Epidemiología", "Psicología Médica"],
        5: ["Farmacología II", "Medicina Interna I", "Cirugía General I", "Pediatría I", "Obstetricia y Ginecología I"],
        6: ["Medicina Interna II", "Cirugía General II", "Pediatría II", "Obstetricia y Ginecología II", "Imagenología"],
        7: ["Psiquiatría", "Ortopedia y Traumatología", "Oftalmología", "Otorrinolaringología", "Medicina Legal"],
        8: ["Urología", "Dermatología", "Neurología Clínica", "Geriatría", "Salud Pública II"],
        9: ["Rotación Clínica I - Internado Rotatorio", "Urgencias Médicas", "Bioética Médica"],
        10: ["Rotación Clínica II - Internado Rotatorio", "Gestión en Salud", "Trabajo de Grado / Tesis"]}},
    "DER": {"nombre": "Derecho", "semestres": {
        1: ["Introducción al Derecho", "Derecho Romano", "Sociología Jurídica", "Constitucional General", "Ciencia Política"],
        2: ["Derecho Civil I (Personas)", "Constitucional Colombiano", "Teoría General del Proceso", "Economía Política", "Hermenéutica Jurídica"],
        3: ["Derecho Civil II (Bienes)", "Penal General", "Administrativo General", "Obligaciones I", "Derecho Internacional Público"],
        4: ["Derecho Civil III (Obligaciones)", "Penal Especial", "Administrativo Colombiano", "Contratos I", "Laboral Individual"],
        5: ["Derecho Civil IV (Contratos)", "Procesal Civil I", "Procesal Penal", "Derecho Comercial I (Sociedades)", "Laboral Colectivo"],
        6: ["Familia y Sucesiones", "Procesal Civil II", "Procesal Administrativo", "Derecho Comercial II (Títulos Valor)", "Derecho Tributario"],
        7: ["Derecho Internacional Privado", "Mecanismos Alternativos de Solución de Conflictos", "Derecho Ambiental", "Consultorio Jurídico I", "Electiva Sociojurídica I"],
        8: ["Derecho Financiero y Bursátil", "Derecho de la Competencia", "Derecho Probatorio", "Consultorio Jurídico II", "Electiva Sociojurídica II"],
        9: ["Derecho Constitucional Procesal", "Filosofía del Derecho", "Consultorio Jurídico III", "Trabajo de Grado I"],
        10: ["Derecho de las Tecnologías", "Derecho del Consumidor", "Consultorio Jurídico IV", "Trabajo de Grado II", "Práctica Forense"]}},
    "ADM": {"nombre": "Administración de Empresas", "semestres": {
        1: ["Matemáticas para la Gestión", "Introducción a la Administración", "Contabilidad Financiera I", "Competencias Comunicativas", "Entorno Económico"],
        2: ["Estadística Descriptiva", "Teoría de las Organizaciones", "Contabilidad Financiera II", "Microeconomía", "Informática para Negocios"],
        3: ["Estadística Inferencial", "Gestión del Talento Humano", "Costos y Presupuestos", "Macroeconomía", "Derecho Comercial"],
        4: ["Investigación de Operaciones", "Comportamiento Organizacional", "Finanzas Corporativas I", "Marketing I", "Derecho Laboral"],
        5: ["Gerencia de Producción y Operaciones", "Gestión Estratégica", "Finanzas Corporativas II", "Marketing II", "Metodología de la Investigación"],
        6: ["Gerencia de la Cadena de Suministro", "Formulación y Evaluación de Proyectos", "Electiva de Negocios I", "Emprendimiento e Innovación", "Ética Empresarial"],
        7: ["Negocios Internacionales", "Gerencia de Ventas", "Sistemas de Información Gerencial", "Gestión de la Calidad", "Electiva de Negocios II"],
        8: ["Gerencia Estratégica Avanzada", "Gobierno Corporativo", "Responsabilidad Social Empresarial", "Simulador de Negocios", "Electiva Profesional I"],
        9: ["Consultoría Empresarial", "Liderazgo y Habilidades Directivas", "Finanzas Internacionales", "Seminario de Grado I"],
        10: ["Práctica Profesional / Empresarial", "Trabajo de Grado / Tesis", "Seminario de Grado II"]}},
    "EDU": {"nombre": "Educación", "semestres": {
        1: ["Pedagogía General", "Historia de la Educación", "Epistemología y Educación", "Comprensión y Producción de Textos", "Sociología de la Educación"],
        2: ["Didáctica General", "Psicología del Desarrollo Evolutivo", "Filosofía de la Educación", "Antropología Educativa", "Tecnologías de la Información y Comunicación Educativa"],
        3: ["Currículo y Planeación Educativa", "Psicología del Aprendizaje", "Evaluación Educativa", "Investigación Educativa I", "Legislación Educativa"],
        4: ["Didácticas Específicas I", "Educación Inclusiva y Diversidad", "Investigación Educativa II", "Diseño de Materiales Didácticos", "Gestión Educativa"],
        5: ["Didácticas Específicas II", "Orientación Educativa y Vocacional", "Práctica Pedagógica I (Observación)", "Prácticas de Convivencia Escolar", "Neuroeducación"],
        6: ["Innovación Educativa", "Práctica Pedagógica II (Ayudantía)", "Educación y Cultura Digital", "Seminario de Inclusión Social", "Diseño Curricular por Competencias"],
        7: ["Bilingüismo y Educación", "Práctica Pedagógica III (Intervención)", "Educación para la Paz y Derechos Humanos", "Taller de Tesis I", "Electiva Pedagógica I"],
        8: ["Liderazgo Educativo y Comunitario", "Práctica Pedagógica IV (Práctica Profesional Dirigida)", "Evaluación de Instituciones Educativas", "Taller de Tesis II", "Electiva Pedagógica II"],
        9: ["Educación de Adultos y Lifelong Learning", "Práctica Profesional Externa", "Seminario de Profundización I"],
        10: ["Trabajo de Grado / Tesis Final", "Práctica Docente Avanzada"]}}
}

NOMBRES = [
    "Juan", "María", "Carlos", "Ana", "Luis", "Sofía", "Pedro", "Laura", "Diego", "Valentina",
    "Andrés", "Camila", "Mateo", "Lucía", "Sebastián", "Daniel", "Isabella", "Samuel", "Gabriela", "Nicolás",
    "Daniela", "Alejandro", "Mariana", "Santiago", "Paula", "Felipe", "Natalia", "David", "Juliana", "Tomás",
    "Manuela", "Miguel", "Sara", "Julián", "Catalina", "Esteban", "Victoria", "Emmanuel", "Adriana", "Jorge",
    "Carolina", "Cristian", "Valeria", "Kevin", "Diana", "Óscar", "Tatiana", "Martín", "Elena", "Ricardo"
]

APELLIDOS = [
    "Rodríguez", "Gómez", "González", "Martínez", "García", "López", "Hernández", "Pérez", "Sánchez", "Ramírez",
    "Torres", "Díaz", "Vargas", "Castro", "Rojas", "Moreno", "Muñoz", "Jiménez", "Ruiz", "Álvarez",
    "Romero", "Herrera", "Suárez", "Mendoza", "Aguilar", "Ortiz", "Medina", "Castillo", "Cárdenas", "Navarro",
    "Restrepo", "Ospina", "Quintero", "Montoya", "Cardona", "Valencia", "Mejía", "Pineda", "Arias", "Salazar",
    "Peña", "Bermúdez", "Cabrera", "Vélez", "Pardo", "Correa", "Acosta", "Parra", "Serrano", "Beltrán"
]

NOMBRES_MASCULINOS = {
    "Juan", "Carlos", "Luis", "Pedro", "Diego", "Andrés", "Mateo", "Sebastián",
    "Daniel", "Samuel", "Nicolás", "Alejandro", "Santiago", "Felipe", "David",
    "Tomás", "Miguel", "Julián", "Esteban", "Emmanuel", "Jorge", "Cristian",
    "Kevin", "Óscar", "Martín", "Ricardo"
}

NOMBRES_FEMENINOS = {
    "María", "Ana", "Sofía", "Laura", "Valentina", "Camila", "Lucía", "Isabella",
    "Gabriela", "Daniela", "Mariana", "Paula", "Natalia", "Juliana", "Manuela",
    "Sara", "Catalina", "Victoria", "Adriana", "Carolina", "Valeria", "Diana",
    "Tatiana", "Elena"
}

# Variables globales para el manejo de estado en la aplicación procedural
estudiantes = {}
root = None
tabla = None
facultad_var = None
semestre_var = None
estado = None
facultad_combo = None
semestre_combo = None

def genero_por_nombre(nombre_completo):
    """Asigna M/F según el primer nombre de las listas del programa."""
    primer_nombre = nombre_completo.split()[0]
    if primer_nombre in NOMBRES_MASCULINOS:
        return "M"
    if primer_nombre in NOMBRES_FEMENINOS:
        return "F"
    return random.choice(["M", "F"])


def generar_estudiantes(cantidad):
    """Devuelve estudiantes aleatorios sin depender de la interfaz."""
    if not isinstance(cantidad, int) or cantidad < 1:
        raise ValueError("La cantidad debe ser un entero mayor que cero.")
    if cantidad > 9000:
        raise ValueError("El máximo es 9000 estudiantes porque los códigos tienen cuatro dígitos.")
    estudiantes_gen = {}
    nombres_usados = set()
    codigos = random.sample(range(1000, 10000), cantidad)
    for codigo_num in codigos:
        while True:
            nombre_completo = f"{random.choice(NOMBRES)} {random.choice(APELLIDOS)} {random.choice(APELLIDOS)}"
            if nombre_completo not in nombres_usados:
                nombres_usados.add(nombre_completo)
                break
        codigo = str(codigo_num)
        fac = random.choice(list(MALLAS_FACULTADES))
        semestre = random.randint(1, 10)
        materias = MALLAS_FACULTADES[fac]["semestres"][semestre]
        elegidas = random.sample(materias, random.randint(min(3, len(materias)), len(materias)))
        asignaturas = []
        for materia in elegidas:
            n1, n2, n3 = (round(random.uniform(1, 5), 1) for _ in range(3))
            asignaturas.append({"nombre": materia, "n1": n1, "n2": n2, "n3": n3,
                                "definitiva": round(n1 * .3 + n2 * .3 + n3 * .4, 2)})
        estudiantes_gen[codigo] = {
            "codigo": codigo, "nombre": nombre_completo, "facultad": fac,
            "semestre": semestre, "edad": random.randint(17, 45),
            "genero": genero_por_nombre(nombre_completo), "asignaturas": asignaturas
        }
    return estudiantes_gen


def promedio_estudiante(est):
    notas = [a["definitiva"] for a in est["asignaturas"]]
    return sum(notas) / len(notas) if notas else 0


def texto_estudiante(est):
    facultad = MALLAS_FACULTADES[est["facultad"]]["nombre"]
    lineas = [
        f"ESTUDIANTE: {est['nombre']} | Código: {est['codigo']}",
        f"Facultad: {facultad} | Semestre: {est['semestre']} | Edad: {est['edad']} | Género: {est['genero']}",
        "-" * 100,
        f"{'Asignatura':48} {'N1 (30%)':>9} {'N2 (30%)':>9} {'N3 (40%)':>9} {'Def.':>8}",
        "-" * 100
    ]
    for a in est["asignaturas"]:
        lineas.append(f"{a['nombre'][:48]:48} {a['n1']:>9.2f} {a['n2']:>9.2f} {a['n3']:>9.2f} {a['definitiva']:>8.2f}")
    lineas += ["-" * 100, f"Promedio del estudiante: {promedio_estudiante(est):.2f}", ""]
    return "\n".join(lineas)


def aviso_sin_datos():
    if not estudiantes:
        messagebox.showinfo("Sin datos", "Primero utiliza «Generar estudiantes» para crear registros aleatorios.")
        return True
    return False


def generar():
    global estudiantes
    cantidad = simpledialog.askinteger("Generar estudiantes", "¿Cuántos estudiantes deseas generar?", parent=root, minvalue=1, maxvalue=9000)
    if cantidad is None:
        return
    try:
        nuevos = generar_estudiantes(cantidad)
        estudiantes = nuevos
        consultar_filtros()
        estado.set(f"Se generaron {len(estudiantes)} estudiantes aleatorios. Los registros solo se conservan durante esta sesión.")
        messagebox.showinfo("Generación completada", f"Se generaron {cantidad} estudiantes correctamente.")
    except (ValueError, MemoryError) as exc:
        messagebox.showerror("No se pudo generar", str(exc))


def consultar_filtros():
    for item in tabla.get_children():
        tabla.delete(item)
    if not estudiantes:
        estado.set("No hay estudiantes cargados.")
        return
    fac_valor = facultad_var.get().split(" - ", 1)[0]
    sem_valor = semestre_var.get()
    encontrados = []
    for est in estudiantes.values():
        if fac_valor != "Todas" and est["facultad"] != fac_valor:
            continue
        if sem_valor != "Todos" and est["semestre"] != int(sem_valor):
            continue
        encontrados.append(est)
    for est in sorted(encontrados, key=lambda e: (e["facultad"], e["semestre"], e["nombre"], e["codigo"])):
        tabla.insert("", "end", iid=est["codigo"], values=(
            est["codigo"], est["nombre"], MALLAS_FACULTADES[est["facultad"]]["nombre"],
            est["semestre"], est["edad"], est["genero"], f"{promedio_estudiante(est):.2f}"))
    estado.set(f"Resultados: {len(encontrados)} estudiante(s). Doble clic en una fila para consultar todas sus notas.")


def limpiar_filtros():
    facultad_var.set("Todas")
    semestre_var.set("Todos")
    consultar_filtros()


def mostrar_texto(titulo, contenido):
    ventana = tk.Toplevel(root)
    ventana.title(titulo)
    ventana.geometry("900x580")
    marco = ttk.Frame(ventana, padding=10)
    marco.pack(fill="both", expand=True)
    texto = tk.Text(marco, wrap="none", font=("Consolas", 10), undo=False)
    sy = ttk.Scrollbar(marco, orient="vertical", command=texto.yview)
    sx = ttk.Scrollbar(marco, orient="horizontal", command=texto.xview)
    texto.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)
    texto.grid(row=0, column=0, sticky="nsew")
    sy.grid(row=0, column=1, sticky="ns")
    sx.grid(row=1, column=0, sticky="ew")
    marco.rowconfigure(0, weight=1)
    marco.columnconfigure(0, weight=1)
    texto.insert("1.0", contenido)
    texto.configure(state="disabled")
    ttk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=(0, 8))


def detalle_seleccionado(_evento=None):
    seleccion = tabla.selection()
    if not seleccion:
        return
    est = estudiantes.get(seleccion[0])
    if est:
        mostrar_texto("Notas del estudiante", texto_estudiante(est))


def consultar_codigo():
    if aviso_sin_datos():
        return
    codigo = simpledialog.askstring("Consultar estudiante", "Introduce el código del estudiante:", parent=root)
    if codigo is None:
        return
    est = estudiantes.get(codigo.strip())
    if not est:
        messagebox.showwarning("No encontrado", "No existe un estudiante con ese código.")
        return
    mostrar_texto("Notas del estudiante", texto_estudiante(est))


def listado_cursos():
    if aviso_sin_datos():
        return
    cursos = defaultdict(list)
    for est in estudiantes.values():
        for a in est["asignaturas"]:
            cursos[a["nombre"]].append((est, a))
    lineas = ["LISTADO DE ESTUDIANTES AGRUPADOS POR ASIGNATURA", "=" * 110]
    for curso, registros in sorted(cursos.items()):
        lineas += ["", f"ASIGNATURA: {curso}", "-" * 110,
                   f"{'Código':<10} {'Estudiante':<24} {'Facultad':<42} {'Sem.':<6} {'Definitiva':>10}"]
        for est, a in sorted(registros, key=lambda x: x[0]["nombre"]):
            lineas.append(f"{est['codigo']:<10} {est['nombre']:<24} {MALLAS_FACULTADES[est['facultad']]['nombre'][:42]:<42} {est['semestre']:<6} {a['definitiva']:>10.2f}")
    mostrar_texto("Listado por cursos", "\n".join(lineas))


def estadisticas_generales():
    if aviso_sin_datos():
        return
    notas = [a["definitiva"] for e in estudiantes.values() for a in e["asignaturas"]]
    conteo = {fac: sum(e["facultad"] == fac for e in estudiantes.values()) for fac in MALLAS_FACULTADES}
    fac_max = max(conteo, key=conteo.get)
    aprobadas = sum(n >= 3 for n in notas)
    texto = ["ESTADÍSTICAS GENERALES", "=" * 65,
             f"Total de estudiantes: {len(estudiantes)}",
             f"Promedio general de definitivas: {sum(notas) / len(notas):.2f}" if notas else "No hay calificaciones.",
             f"Facultad con más estudiantes: {MALLAS_FACULTADES[fac_max]['nombre']} ({conteo[fac_max]} estudiantes)",
             f"Asignaturas aprobadas (definitiva >= 3.0): {aprobadas}/{len(notas)} ({aprobadas / len(notas) * 100:.1f}%)" if notas else "Porcentaje de aprobadas: no disponible"]
    mostrar_texto("Estadísticas generales", "\n".join(texto))


def _informe_individual(est):
    lineas = ["INFORME ACADÉMICO INDIVIDUAL", "=" * 75, texto_estudiante(est)]
    return "\n".join(lineas)


def _guardar_txt(nombre_sugerido, contenido):
    ruta = filedialog.asksaveasfilename(parent=root, title="Guardar informe", initialfile=nombre_sugerido,
                                        defaultextension=".txt", filetypes=[("Archivo de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if not ruta:
        return
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
        messagebox.showinfo("Archivo guardado", f"Informe guardado correctamente:\n{ruta}")
    except OSError as exc:
        messagebox.showerror("Error al guardar", f"No se pudo guardar el archivo:\n{exc}")


def informe_individual():
    if aviso_sin_datos():
        return
    codigo = simpledialog.askstring("Informe individual", "Código del estudiante:", parent=root)
    if codigo is None:
        return
    est = estudiantes.get(codigo.strip())
    if not est:
        messagebox.showwarning("No encontrado", "No existe un estudiante con ese código.")
        return
    _guardar_txt(f"informe_estudiante_{est['codigo']}.txt", _informe_individual(est))


def exportar_facultad():
    if aviso_sin_datos():
        return
    grupos = defaultdict(list)
    for est in estudiantes.values():
        grupos[est["facultad"]].append(est)
    lineas = ["INFORME GENERAL DE ESTUDIANTES POR FACULTAD", "=" * 90]
    for fac in MALLAS_FACULTADES:
        lista = grupos.get(fac, [])
        if not lista:
            continue
        lineas += ["", "=" * 90, f"FACULTAD: {MALLAS_FACULTADES[fac]['nombre']} ({fac})",
                   f"Total de estudiantes: {len(lista)}", "=" * 90]
        for est in sorted(lista, key=lambda e: (e["semestre"], e["nombre"])):
            lineas += ["", texto_estudiante(est)]
    _guardar_txt("registros_por_facultad.txt", "\n".join(lineas))


def estadisticas_facultad():
    if aviso_sin_datos():
        return
    grupos = defaultdict(list)
    for est in estudiantes.values():
        grupos[est["facultad"]].append(est)
    lineas = ["ESTADÍSTICAS DEMOGRÁFICAS POR FACULTAD", "=" * 85]
    for fac, lista in grupos.items():
        mayor = max(lista, key=lambda e: e["edad"])
        menor = min(lista, key=lambda e: e["edad"])
        hombres = sum(e["genero"] == "M" for e in lista)
        mujeres = sum(e["genero"] == "F" for e in lista)
        lineas += ["", f"Facultad: {MALLAS_FACULTADES[fac]['nombre']} ({fac})",
                   f"Total estudiantes: {len(lista)}",
                   f"Promedio de edad: {sum(e['edad'] for e in lista) / len(lista):.1f} años",
                   f"Distribución de género: Hombres (M): {hombres} | Mujeres (F): {mujeres}",
                   f"Mayor edad: {mayor['nombre']} ({mayor['edad']} años, código {mayor['codigo']})",
                   f"Menor edad: {menor['nombre']} ({menor['edad']} años, código {menor['codigo']})",
                   "-" * 85]
    mostrar_texto("Estadísticas por facultad", "\n".join(lineas))


def crear_interfaz():
    global tabla, facultad_var, semestre_var, estado, facultad_combo, semestre_combo
    
    estilo = ttk.Style()
    try:
        estilo.theme_use("clam")
    except tk.TclError:
        pass
    estilo.configure("Titulo.TLabel", font=("Arial", 17, "bold"), foreground="#1B4F72", background="#EAF2F8")
    estilo.configure("Sub.TLabel", font=("Arial", 10), background="#EAF2F8")
    estilo.configure("Treeview", rowheight=25, font=("Arial", 9))
    estilo.configure("Treeview.Heading", font=("Arial", 9, "bold"))

    cabecera = tk.Frame(root, bg="#EAF2F8")
    cabecera.pack(fill="x", padx=18, pady=(14, 8))
    ttk.Label(cabecera, text="Sistema Multifacultad de Gestión Académica", style="Titulo.TLabel").pack(anchor="w")
    ttk.Label(cabecera, text="Generación, consulta de notas, informes y estadísticas", style="Sub.TLabel").pack(anchor="w", pady=(3, 0))

    acciones = ttk.LabelFrame(root, text="Acciones del sistema", padding=8)
    acciones.pack(fill="x", padx=18, pady=6)
    botones = [
        ("1. Generar estudiantes", generar), ("2. Listado por cursos", listado_cursos),
        ("3. Consultar por código", consultar_codigo), ("4. Estadísticas generales", estadisticas_generales),
        ("5. Informe individual TXT", informe_individual), ("6. Exportar por facultad TXT", exportar_facultad),
        ("7. Estadísticas por facultad", estadisticas_facultad)
    ]
    for i, (texto_btn, comando) in enumerate(botones):
        ttk.Button(acciones, text=texto_btn, command=comando).grid(row=i // 4, column=i % 4, padx=4, pady=4, sticky="ew")
    for col in range(4):
        acciones.columnconfigure(col, weight=1)

    filtros = ttk.LabelFrame(root, text="Consulta gráfica por facultad y semestre", padding=10)
    filtros.pack(fill="x", padx=18, pady=6)
    ttk.Label(filtros, text="Facultad:").grid(row=0, column=0, padx=(0, 5), sticky="w")
    facultad_var = tk.StringVar(value="Todas")
    opciones_fac = ["Todas"] + [f"{k} - {v['nombre']}" for k, v in MALLAS_FACULTADES.items()]
    facultad_combo = ttk.Combobox(filtros, textvariable=facultad_var, values=opciones_fac, state="readonly", width=37)
    facultad_combo.grid(row=0, column=1, padx=(0, 15), sticky="ew")
    facultad_combo.bind("<<ComboboxSelected>>", lambda e: consultar_filtros())
    ttk.Label(filtros, text="Semestre:").grid(row=0, column=2, padx=(0, 5), sticky="w")
    semestre_var = tk.StringVar(value="Todos")
    semestre_combo = ttk.Combobox(filtros, textvariable=semestre_var, values=["Todos"] + [str(i) for i in range(1, 11)], state="readonly", width=12)
    semestre_combo.grid(row=0, column=3, padx=(0, 15), sticky="w")
    semestre_combo.bind("<<ComboboxSelected>>", lambda e: consultar_filtros())
    ttk.Button(filtros, text="Consultar", command=consultar_filtros).grid(row=0, column=4, padx=3)
    ttk.Button(filtros, text="Limpiar", command=limpiar_filtros).grid(row=0, column=5, padx=3)
    filtros.columnconfigure(1, weight=1)

    cuerpo = ttk.Frame(root, padding=(18, 4, 18, 10))
    cuerpo.pack(fill="both", expand=True)
    ttk.Label(cuerpo, text="Estudiantes encontrados (doble clic para ver notas completas):").pack(anchor="w", pady=(2, 5))
    columnas = ("codigo", "nombre", "facultad", "semestre", "edad", "genero", "promedio")
    tabla = ttk.Treeview(cuerpo, columns=columnas, show="headings", selectmode="browse")
    encabezados = {"codigo": "Código", "nombre": "Estudiante", "facultad": "Facultad", "semestre": "Semestre",
                   "edad": "Edad", "genero": "Género", "promedio": "Promedio"}
    anchos = {"codigo": 75, "nombre": 190, "facultad": 300, "semestre": 80, "edad": 55, "genero": 65, "promedio": 85}
    for col in columnas:
        tabla.heading(col, text=encabezados[col])
        tabla.column(col, width=anchos[col], minwidth=50, anchor="w" if col in ("nombre", "facultad") else "center")
    scroll_y = ttk.Scrollbar(cuerpo, orient="vertical", command=tabla.yview)
    scroll_x = ttk.Scrollbar(cuerpo, orient="horizontal", command=tabla.xview)
    tabla.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
    tabla.pack(fill="both", expand=True, side="top")
    scroll_y.place(relx=1, rely=0.08, relheight=0.86, anchor="ne")
    scroll_x.pack(fill="x")
    tabla.bind("<Double-1>", detalle_seleccionado)
    estado = tk.StringVar(value="Genere estudiantes para comenzar. Los registros permanecen en memoria mientras la aplicación esté abierta.")
    ttk.Label(root, textvariable=estado, relief="sunken", anchor="w", padding=5).pack(fill="x", side="bottom")


def main():
    global root
    root = tk.Tk()
    root.title("Sistema Multifacultad de Gestión Académica")
    root.geometry("1120x720")
    root.minsize(900, 600)
    root.configure(bg="#EAF2F8")
    
    crear_interfaz()
    root.mainloop()


if __name__ == "__main__":
    main()
