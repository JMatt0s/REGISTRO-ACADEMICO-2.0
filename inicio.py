import subprocess
import sys
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk


DIRECTORIO = Path(__file__).resolve().parent
APLICACION = DIRECTORIO / "ren_4_men.py"


def abrir_sistema():
    if not APLICACION.is_file():
        messagebox.showerror(
            "Archivo no encontrado",
            f"No se encontró la aplicación:\n{APLICACION}",
            parent=ventana,
        )
        return

    try:
        subprocess.Popen([sys.executable, str(APLICACION)], cwd=str(DIRECTORIO))
    except OSError as error:
        messagebox.showerror(
            "No se pudo abrir",
            f"Ocurrió un error al iniciar el sistema:\n{error}",
            parent=ventana,
        )


ventana = tk.Tk()
ventana.title("Sistema Multifacultad")
ventana.geometry("560x360")
ventana.minsize(480, 320)
ventana.configure(background="#eef3f8")

estilo = ttk.Style(ventana)
estilo.configure("Titulo.TLabel", font=("Segoe UI", 22, "bold"))
estilo.configure("Descripcion.TLabel", font=("Segoe UI", 11))
estilo.configure("Abrir.TButton", font=("Segoe UI", 12, "bold"), padding=(18, 12))

contenido = ttk.Frame(ventana, padding=36)
contenido.pack(expand=True, fill="both")

ttk.Label(
    contenido,
    text="Sistema Multifacultad",
    style="Titulo.TLabel",
).pack(pady=(24, 10))

ttk.Label(
    contenido,
    text="Gestión académica y consulta de estudiantes",
    style="Descripcion.TLabel",
).pack(pady=(0, 28))

ttk.Button(
    contenido,
    text="Abrir sistema académico",
    style="Abrir.TButton",
    command=abrir_sistema, 
).pack()

ttk.Button(
    contenido,
    text="Salir",
    command=ventana.destroy,
).pack(pady=18)

ventana.mainloop()
