import re
import subprocess
import sys
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk


DIRECTORIO = Path(__file__).resolve().parent
APLICACION = DIRECTORIO / "ren_4_men.py"


def autenticar_cedula(cedula: str) -> bool:
    cedula = cedula.strip()
    return bool(re.fullmatch(r"[0-9]{10}", cedula))


def abrir_sistema(ventana: tk.Tk) -> None:
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


def crear_ventana() -> tk.Tk:
    ventana = tk.Tk()
    ventana.title("Inicio de sesión - Sistema Multifacultad")
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
        text="Inicia sesión con tu cédula",
        style="Descripcion.TLabel",
    ).pack(pady=(0, 18))

    entrada_cedula = ttk.Entry(contenido, font=("Segoe UI", 12), justify="center")
    entrada_cedula.pack(fill="x", padx=35, ipady=6)
    entrada_cedula.focus_set()

    def iniciar_sesion() -> None:
        cedula = entrada_cedula.get().strip()
        if not autenticar_cedula(cedula):
            messagebox.showwarning(
                "Cédula inválida",
                "Ingresa una cédula válida de 10 dígitos.",
                parent=ventana,
            )
            entrada_cedula.focus_set()
            return

        abrir_sistema(ventana)

    ttk.Button(
        contenido,
        text="Iniciar sesión",
        style="Abrir.TButton",
        command=iniciar_sesion,
    ).pack(pady=18)
    ttk.Button(
        contenido,
        text="Salir",
        command=ventana.destroy,
    ).pack()

    return ventana


if __name__ == "__main__":
    crear_ventana().mainloop()
