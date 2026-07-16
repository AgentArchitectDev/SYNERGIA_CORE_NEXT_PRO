"""
===========================================================
SYNERGIA CORE NEXT_PRO
OMEGA CONTROL CENTER
SIDE BAR V1
===========================================================

Sidebar principal del sistema.

Integra:

- Navigation V6
- Control Center
- Workspace


Preparado para:

- Module Registry
- Navigation Controller
- Dynamic Modules


===========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)



class SideBar(QWidget):


    """
    OMEGA Sidebar.
    """



    def __init__(self):

        super().__init__()


        self.modules = {}


        self.active = None



        self.layout = QVBoxLayout()


        self.title = QLabel(
            "SYNERGIA MODULES"
        )


        self.layout.addWidget(
            self.title
        )


        self.setLayout(
            self.layout
        )



    # -------------------------------------------------
    # MODULE REGISTER
    # -------------------------------------------------


    def add_module(
            self,
            name
    ):


        button = QPushButton(
            name
        )


        button.clicked.connect(

            lambda checked=False,
            module=name:
            self.open(module)

        )


        self.layout.addWidget(
            button
        )


        self.modules[name] = button



        return {

            "status":
                "added",

            "module":
                name

        }



    # -------------------------------------------------
    # OPEN MODULE
    # -------------------------------------------------


    def open(
            self,
            name
    ):


        if name not in self.modules:

            return {

                "status":
                    "error",

                "error":
                    "module_not_found"

            }



        self.active = name



        return {

            "status":
                "opened",

            "module":
                name

        }



    # -------------------------------------------------
    # STATUS
    # -------------------------------------------------


    def status(self):

        return {

            "component":
                "OMEGA SideBar",

            "modules":
                list(
                    self.modules.keys()
                ),

            "active":
                self.active,

            "count":
                len(
                    self.modules
                )

        }





side_bar = SideBar()
