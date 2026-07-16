"""
system_monitor.py
-------------------------------------------------
SYNERGIA Dashboard OS
Fase 2.5

Panel de monitoreo del sistema.
Muestra el estado del Runtime, Memoria,
Módulos, Última tarea y Estadísticas.
"""

import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime


class SystemMonitor:

    def __init__(self, parent):

        self.widget = scrolledtext.ScrolledText(
            parent,
            width=45,
            bg="#1b1b1b",
            fg="#00ffff",
            font=("Consolas", 10),
            wrap=tk.WORD
        )

        # Estado interno
        self.memory_size = 0
        self.last_command = "-"
        self.last_task = "-"
        self.last_module = "-"
        self.execution_time = "0.00 s"
        self.commands_executed = 0
        self.status = "ONLINE"
        self.runtime = "ACTIVE"
        self.mode = "COGNITIVE OS"
        self.ai_provider = "LOCAL"
        self.ai_model = "No conectado"

    # ------------------------------------------------
    # Mostrar panel
    # ------------------------------------------------

    def pack(self, **kwargs):
        self.widget.pack(**kwargs)

    # ------------------------------------------------
    # Actualizar datos
    # ------------------------------------------------

    def update(
        self,
        memory_size=None,
        last_command=None,
        last_task=None,
        last_module=None,
        execution_time=None,
        ai_provider=None,
        ai_model=None
    ):

        if memory_size is not None:
            self.memory_size = memory_size

        if last_command is not None:
            self.last_command = last_command

        if last_task is not None:
            self.last_task = last_task

        if last_module is not None:
            self.last_module = last_module

        if execution_time is not None:
            self.execution_time = execution_time

        if ai_provider is not None:
            self.ai_provider = ai_provider

        if ai_model is not None:
            self.ai_model = ai_model

        self.commands_executed += 1

        self.render()

    # ------------------------------------------------
    # Dibujar panel
    # ------------------------------------------------

    def render(self):

        self.widget.delete("1.0", tk.END)

        now = datetime.now().strftime("%H:%M:%S")

        self.widget.insert(
            tk.END,
            "═══════════════════════════════════════\n"
        )

        self.widget.insert(
            tk.END,
            "        SYNERGIA SYSTEM MONITOR\n"
        )

        self.widget.insert(
            tk.END,
            "═══════════════════════════════════════\n\n"
        )

        # ---------------- SYSTEM ----------------

        self.widget.insert(tk.END, "SYSTEM\n")
        self.widget.insert(tk.END, "──────────────────────────────\n")
        self.widget.insert(tk.END, f"Status          : {self.status}\n")
        self.widget.insert(tk.END, f"Runtime         : {self.runtime}\n")
        self.widget.insert(tk.END, f"Mode            : {self.mode}\n")
        self.widget.insert(tk.END, "\n")

        # ---------------- AI ----------------

        self.widget.insert(tk.END, "AI ENGINE\n")
        self.widget.insert(tk.END, "──────────────────────────────\n")
        self.widget.insert(tk.END, f"Provider        : {self.ai_provider}\n")
        self.widget.insert(tk.END, f"Model           : {self.ai_model}\n")
        self.widget.insert(tk.END, "\n")

        # ---------------- MEMORY ----------------

        self.widget.insert(tk.END, "MEMORY\n")
        self.widget.insert(tk.END, "──────────────────────────────\n")
        self.widget.insert(tk.END, f"Items           : {self.memory_size}\n")
        self.widget.insert(tk.END, f"Last Command    : {self.last_command}\n")
        self.widget.insert(tk.END, "\n")

        # ---------------- EXECUTION ----------------

        self.widget.insert(tk.END, "EXECUTION\n")
        self.widget.insert(tk.END, "──────────────────────────────\n")
        self.widget.insert(tk.END, f"Last Task       : {self.last_task}\n")
        self.widget.insert(tk.END, f"Last Module     : {self.last_module}\n")
        self.widget.insert(tk.END, f"Execution Time  : {self.execution_time}\n")
        self.widget.insert(tk.END, "\n")

        # ---------------- MODULES ----------------

        self.widget.insert(tk.END, "MODULES\n")
        self.widget.insert(tk.END, "──────────────────────────────\n")

        modules = [
            "Runtime",
            "Memory",
            "Router",
            "Task Engine",
            "Export Manager",
            "Brain Graph"
        ]

        for module in modules:
            self.widget.insert(
                tk.END,
                f"✓ {module}\n"
            )

        self.widget.insert(tk.END, "\n")

        # ---------------- SESSION ----------------

        self.widget.insert(tk.END, "SESSION\n")
        self.widget.insert(tk.END, "──────────────────────────────\n")
        self.widget.insert(
            tk.END,
            f"Commands        : {self.commands_executed}\n"
        )

        self.widget.insert(
            tk.END,
            f"Updated         : {now}\n"
        )

        self.widget.see(tk.END)
