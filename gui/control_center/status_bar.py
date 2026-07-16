"""
===========================================================
SYNERGIA CORE NEXT_PRO
OMEGA CONTROL CENTER
STATUS BAR V1
===========================================================

Barra inferior del sistema.

Gestiona:

- Estado general
- Runtime
- AI Core
- Evolución
- Información del sistema


Preparado para:

- Telemetry
- Health Manager
- Runtime Manager
- Evolution Engine


===========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel
)



class StatusBar(QWidget):


    """
    OMEGA Status Bar
    """



    def __init__(self):

        super().__init__()


        self.layout = QHBoxLayout()


        self.cpu = QLabel(
            "CPU: --"
        )


        self.memory = QLabel(
            "RAM: --"
        )


        self.runtime = QLabel(
            "RUNTIME: OFFLINE"
        )


        self.ai = QLabel(
            "AI CORE: IDLE"
        )


        self.evolution = QLabel(
            "EVOLUTION: READY"
        )



        self.layout.addWidget(
            self.cpu
        )


        self.layout.addWidget(
            self.memory
        )


        self.layout.addStretch()


        self.layout.addWidget(
            self.runtime
        )


        self.layout.addWidget(
            self.ai
        )


        self.layout.addWidget(
            self.evolution
        )


        self.setLayout(
            self.layout
        )



    # -------------------------------------------------
    # SYSTEM INFO
    # -------------------------------------------------


    def update_system(
            self,
            cpu=None,
            memory=None
    ):


        if cpu is not None:

            self.cpu.setText(
                f"CPU: {cpu}%"
            )


        if memory is not None:

            self.memory.setText(
                f"RAM: {memory}%"
            )



    # -------------------------------------------------
    # RUNTIME
    # -------------------------------------------------


    def set_runtime(
            self,
            active=True
    ):


        if active:

            self.runtime.setText(
                "RUNTIME: ONLINE"
            )

        else:

            self.runtime.setText(
                "RUNTIME: OFFLINE"
            )



    # -------------------------------------------------
    # AI
    # -------------------------------------------------


    def set_ai_status(
            self,
            text
    ):


        self.ai.setText(
            f"AI CORE: {text}"
        )



    # -------------------------------------------------
    # EVOLUTION
    # -------------------------------------------------


    def set_evolution(
            self,
            text
    ):


        self.evolution.setText(
            f"EVOLUTION: {text}"
        )



    # -------------------------------------------------
    # STATUS
    # -------------------------------------------------


    def status(self):

        return {

            "component":
                "OMEGA Status Bar",

            "cpu":
                self.cpu.text(),

            "memory":
                self.memory.text(),

            "runtime":
                self.runtime.text(),

            "ai":
                self.ai.text(),

            "evolution":
                self.evolution.text()

        }





status_bar = StatusBar()
