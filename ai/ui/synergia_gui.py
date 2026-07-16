"""
SYNERGIA CONTROL CENTER
Fase 2.6

GUI Principal
"""

import tkinter as tk

from ai.runtime.orchestrator import Orchestrator

from ai.ui.panels.brain_panel import BrainPanel
from ai.ui.panels.output_panel import OutputPanel
from ai.ui.panels.system_monitor import SystemMonitor

from ai.ui.controllers.dashboard_controller import DashboardController


class SynergiaDashboard:

    def __init__(self, root):

        self.root = root

        self.root.title("SYNERGIA CONTROL CENTER V2.6")

        self.root.geometry("1450x820")

        orchestrator = Orchestrator()

        # ---------------- INPUT ----------------

        self.input_box = tk.Entry(
            root,
            width=120
        )

        self.input_box.pack(
            pady=10
        )

        self.run_button = tk.Button(
            root,
            text="EJECUTAR",
            command=self.execute
        )

        self.run_button.pack()

        # ---------------- FRAME ----------------

        frame = tk.Frame(root)

        frame.pack(
            fill=tk.BOTH,
            expand=True
        )

        # ---------------- PANELS ----------------

        self.brain = BrainPanel(frame)

        self.brain.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True
        )

        self.output = OutputPanel(frame)

        self.output.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True
        )

        self.monitor = SystemMonitor(frame)

        self.monitor.pack(
            side=tk.RIGHT,
            fill=tk.BOTH,
            expand=True
        )

        self.monitor.render()

        # ---------------- CONTROLLER ----------------

        self.controller = DashboardController(

            self.brain,

            self.output,

            self.monitor,

            orchestrator

        )

    # --------------------------------

    def execute(self):

        text = self.input_box.get().strip()

        if not text:
            return

        self.controller.execute(text)


# ----------------------------------------

if __name__ == "__main__":

    root = tk.Tk()

    app = SynergiaDashboard(root)

    root.mainloop()
