"""
brain_panel.py
-------------------------
Panel que muestra el flujo de pensamiento del sistema.
Fase 2.5 - SYNERGIA Dashboard OS
"""

import tkinter as tk
from tkinter import scrolledtext


class BrainPanel:

    def __init__(self, parent):

        self.widget = scrolledtext.ScrolledText(
            parent,
            width=45,
            bg="#0b0f14",
            fg="#00ff99",
            font=("Consolas", 10),
            wrap=tk.WORD
        )

    # -------------------------
    # Mostrar panel
    # -------------------------
    def pack(self, **kwargs):
        self.widget.pack(**kwargs)

    # -------------------------
    # Limpiar panel
    # -------------------------
    def clear(self):
        self.widget.delete("1.0", tk.END)

    # -------------------------
    # Agregar línea
    # -------------------------
    def add(self, text):

        self.widget.insert(tk.END, text + "\n")
        self.widget.see(tk.END)

    # -------------------------
    # Flujo estándar
    # -------------------------
    def show_execution_flow(self):

        self.clear()

        steps = [
            "🧠 INPUT NODE ACTIVE",
            "📦 MEMORY NODE LOADING",
            "⚙️ DECISION ENGINE ACTIVE",
            "🔀 ROUTER EXECUTING",
            "🧩 TASK ENGINE",
            "📤 EXPORT MANAGER",
            "✅ EXECUTION COMPLETE"
        ]

        for step in steps:
            self.add(step)

    # -------------------------
    # Mostrar lista personalizada
    # -------------------------
    def show_custom_flow(self, steps):

        self.clear()

        for step in steps:
            self.add(step)
