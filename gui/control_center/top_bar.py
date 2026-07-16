"""
===========================================================
SYNERGIA CORE NEXT_PRO
OMEGA CONTROL CENTER
TOP BAR V1
===========================================================

Barra superior principal.

Gestiona:

- Identidad del sistema
- Estado visual
- Información runtime


Preparado para:

- Language Selector
- User Manager
- AI Status
- Evolution State


===========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel
)



class TopBar(QWidget):


    """
    OMEGA Top Bar
    """



    def __init__(self):

        super().__init__()


        self.layout = QHBoxLayout()


        self.system_label = QLabel(
            "SYNERGIA OMEGA"
        )


        self.status_label = QLabel(
            "SYSTEM READY"
        )


        self.runtime_label = QLabel(
            "RUNTIME: OFFLINE"
        )


        self.layout.addWidget(
            self.system_label
        )


        self.layout.addStretch()


        self.layout.addWidget(
            self.runtime_label
        )


        self.layout.addWidget(
            self.status_label
        )


        self.setLayout(
            self.layout
        )


        self.runtime = False



    # -------------------------------------------------
    # Runtime
    # -------------------------------------------------


    def set_runtime(
            self,
            active=True
    ):


        self.runtime = active


        if active:

            self.runtime_label.setText(
                "RUNTIME: ONLINE"
            )

        else:

            self.runtime_label.setText(
                "RUNTIME: OFFLINE"
            )



    # -------------------------------------------------
    # Status
    # -------------------------------------------------


    def set_status(
            self,
            text
    ):

        self.status_label.setText(
            text
        )



    # -------------------------------------------------
    # STATUS
    # -------------------------------------------------


    def status(self):

        return {

            "component":
                "OMEGA Top Bar",

            "system":
                self.system_label.text(),

            "runtime":
                self.runtime,

            "status":
                self.status_label.text()

        }





top_bar = TopBar()
