"""
===========================================================
SYNERGIA CORE NEXT_PRO
OMEGA WORKSPACE LAYOUT V1
===========================================================

Layout principal del Workspace.

Responsabilidades:

- Crear estructura visual
- Integrar Panel
- Integrar Tabs
- Administrar zona central

Arquitectura:

Workspace Controller

        |

Workspace Layout

        |

Panel + Tabs


===========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)


from gui.workspace.workspace_panel import (
    WorkspacePanel
)


from gui.workspace.workspace_tabs import (
    WorkspaceTabs
)



class WorkspaceLayout(QWidget):


    """
    Layout principal OMEGA.
    """



    def __init__(self):

        super().__init__()


        self.layout = QVBoxLayout()


        self.header = QLabel(
            "SYNERGIA OMEGA WORKSPACE"
        )


        self.panel = WorkspacePanel(
            "OMEGA Main Panel"
        )


        self.tabs = WorkspaceTabs()



        self.layout.addWidget(
            self.header
        )


        self.layout.addWidget(
            self.panel
        )


        self.layout.addWidget(
            self.tabs
        )


        self.setLayout(
            self.layout
        )



    # -----------------------------------------------------
    # ADD TAB
    # -----------------------------------------------------


    def add_tab(
            self,
            name
    ):

        return self.tabs.add_workspace(
            name
        )



    # -----------------------------------------------------
    # OPEN TAB
    # -----------------------------------------------------


    def open_tab(
            self,
            name
    ):

        return self.tabs.open(
            name
        )



    # -----------------------------------------------------
    # STATUS
    # -----------------------------------------------------


    def status(self):

        return {

            "component":
                "OMEGA Workspace Layout",

            "panel":
                self.panel.status(),

            "tabs":
                self.tabs.status()

        }




workspace_layout = WorkspaceLayout()
