"""
===========================================================
SYNERGIA CORE NEXT_PRO
OMEGA WORKSPACE PANEL V1
===========================================================

Panel visual base del Workspace.

Responsabilidades:

- Crear contenedor visual
- Gestionar título
- Gestionar contenido
- Exponer estado
- Preparado para herencia

Arquitectura:

Workspace Controller
        |
        |
Workspace Panel
        |
        |
Qt QWidget


===========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)


class WorkspacePanel(QWidget):


    """
    Panel base OMEGA.
    """



    def __init__(
            self,
            title="OMEGA Workspace"
    ):

        super().__init__()


        self.title = title


        self.layout = QVBoxLayout()


        self.label = QLabel(
            self.title
        )


        self.layout.addWidget(
            self.label
        )


        self.setLayout(
            self.layout
        )


        self.content = None



    # -----------------------------------------------------
    # CONTENT
    # -----------------------------------------------------


    def set_content(
            self,
            widget
    ):


        if widget:

            self.content = widget

            self.layout.addWidget(
                widget
            )



    # -----------------------------------------------------
    # TITLE
    # -----------------------------------------------------


    def set_title(
            self,
            title
    ):

        self.title = title

        self.label.setText(
            title
        )



    # -----------------------------------------------------
    # STATUS
    # -----------------------------------------------------


    def status(self):

        return {

            "component":
                "OMEGA Workspace Panel",

            "title":
                self.title,

            "has_content":
                self.content is not None

        }





