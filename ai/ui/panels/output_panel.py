"""
output_panel.py
------------------------------------
Panel de salida del sistema
SYNERGIA Dashboard OS
Fase 2.5
"""

import tkinter as tk
from tkinter import scrolledtext


class OutputPanel:

    def __init__(self, parent):

        self.widget = scrolledtext.ScrolledText(
            parent,
            width=50,
            bg="#111111",
            fg="#FFFFFF",
            font=("Consolas", 10),
            wrap=tk.WORD
        )

    # -------------------------
    # Mostrar panel
    # -------------------------

    def pack(self, **kwargs):
        self.widget.pack(**kwargs)

    # -------------------------
    # Limpiar
    # -------------------------

    def clear(self):
        self.widget.delete("1.0", tk.END)

    # -------------------------
    # Escribir
    # -------------------------

    def write(self, text):

        self.widget.insert(tk.END, text)
        self.widget.see(tk.END)

    # -------------------------
    # Mostrar respuesta
    # -------------------------

    def show_result(self, result):

        self.clear()

        self.write(self.format_result(result))

    # -------------------------
    # Formato humano
    # -------------------------

    def format_result(self, result):

        if isinstance(result, dict):

            # --------------------
            # TASK ENGINE
            # --------------------

            if result.get("status") == "executed":

                return (
                    "\n"
                    "══════════════════════════════\n"
                    "      TASK ENGINE\n"
                    "══════════════════════════════\n\n"

                    f"Tarea:\n"
                    f"   {result.get('task')}\n\n"

                    f"Resultado:\n"
                    f"   Ejecutada correctamente\n\n"

                    f"Análisis:\n"
                    f"   {result.get('analysis')}\n"
                )

            # --------------------
            # CORE ENGINE
            # --------------------

            if result.get("type") == "core":

                return (
                    "\n"
                    "══════════════════════════════\n"
                    "      CORE ENGINE\n"
                    "══════════════════════════════\n\n"

                    f"Respuesta:\n"
                    f"   {result.get('response')}\n"
                )

        # -------------------------
        # STRING
        # -------------------------

        if isinstance(result, str):

            return (
                "\n"
                "══════════════════════════════\n"
                "      SYSTEM MESSAGE\n"
                "══════════════════════════════\n\n"
                f"{result}\n"
            )

        # -------------------------
        # OTRO
        # -------------------------

        return str(result)
