"""
===========================================================
SYNERGIA CORE NEXT_PRO
OMEGA WORKSPACE TABS V1
===========================================================

Administrador de pestañas del Workspace.

Gestiona:

- tabs dinámicas
- tab activo
- registro de espacios
- estado

Preparado para:

- Editor PRO
- AI Assistant
- Runtime Console
- Preview Engine


===========================================================
"""


from PySide6.QtWidgets import (
    QTabWidget,
    QWidget
)


class WorkspaceTabs(QTabWidget):


    """
    Sistema de pestañas OMEGA.
    """



    def __init__(self):

        super().__init__()


        self.tabs = {}


        self.current = None



        self.currentChanged.connect(
            self._changed
        )



    # -----------------------------------------------------
    # ADD TAB
    # -----------------------------------------------------


    def add_workspace(
            self,
            name,
            widget=None
    ):


        if widget is None:

            widget = QWidget()



        index = self.addTab(
            widget,
            name
        )


        self.tabs[name] = {

            "index": index,

            "widget": widget

        }


        return {

            "status":
                "added",

            "tab":
                name

        }



    # -----------------------------------------------------
    # OPEN TAB
    # -----------------------------------------------------


    def open(
            self,
            name
    ):


        if name not in self.tabs:

            return {

                "status":
                    "error",

                "error":
                    "tab_not_found"

            }



        index = self.tabs[name]["index"]


        self.setCurrentIndex(
            index
        )


        self.current = name


        return {

            "status":
                "opened",

            "tab":
                name

        }



    # -----------------------------------------------------
    # EVENT
    # -----------------------------------------------------


    def _changed(
            self,
            index
    ):


        for name, data in self.tabs.items():

            if data["index"] == index:

                self.current = name



    # -----------------------------------------------------
    # STATUS
    # -----------------------------------------------------


    def status(self):

        return {

            "component":
                "OMEGA Workspace Tabs",

            "tabs":
                list(
                    self.tabs.keys()
                ),

            "current":
                self.current,

            "count":
                len(
                    self.tabs
                )

        }





workspace_tabs = WorkspaceTabs()
