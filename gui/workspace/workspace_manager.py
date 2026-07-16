"""
===========================================================
SYNERGIA CORE NEXT_PRO
OMEGA WORKSPACE MANAGER V1
===========================================================

Administrador principal del Workspace.

Gestiona:

- módulos activos
- paneles
- pestañas
- ciclo de vida
- estado operativo

Preparado para:

- Editor PRO
- AI Assistant
- Runtime Console
- Preview Engine
- OMEGA Desktop

===========================================================
"""


from gui.workspace.workspace_state import workspace_state



class WorkspaceManager:


    """
    Workspace Manager OMEGA V1
    """


    def __init__(self):

        self.modules = {}

        self.panels = {}

        self.tabs = {}

        self.loaded = False

        self.current = None



    # -----------------------------------------------------
    # REGISTRO
    # -----------------------------------------------------


    def register_module(
            self,
            name,
            module
    ):

        self.modules[name] = module



    def register_panel(
            self,
            name,
            panel
    ):

        self.panels[name] = panel



    def register_tab(
            self,
            name,
            tab
    ):

        self.tabs[name] = tab



    # -----------------------------------------------------
    # INICIALIZACION
    # -----------------------------------------------------


    def initialize(self):

        self.loaded = True

        return {

            "status":
                "initialized",

            "modules":
                len(self.modules),

            "panels":
                len(self.panels),

            "tabs":
                len(self.tabs)

        }



    # -----------------------------------------------------
    # ABRIR WORKSPACE
    # -----------------------------------------------------


    def open(
            self,
            module
    ):


        self.current = module


        workspace_state.set_module(
            module
        )


        return {

            "status":
                "opened",

            "module":
                module

        }



    # -----------------------------------------------------
    # PANELES
    # -----------------------------------------------------


    def activate_panel(
            self,
            panel
    ):


        workspace_state.set_panel(
            panel
        )


        return {

            "status":
                "panel_active",

            "panel":
                panel

        }



    # -----------------------------------------------------
    # TABS
    # -----------------------------------------------------


    def activate_tab(
            self,
            tab
    ):


        workspace_state.set_tab(
            tab
        )


        return {

            "status":
                "tab_active",

            "tab":
                tab

        }



    # -----------------------------------------------------
    # STATUS
    # -----------------------------------------------------


    def status(self):

        return {

            "manager":
                "OMEGA Workspace Manager",

            "loaded":
                self.loaded,

            "current":
                self.current,

            "modules":
                list(
                    self.modules.keys()
                ),

            "panels":
                list(
                    self.panels.keys()
                ),

            "tabs":
                list(
                    self.tabs.keys()
                )

        }



    # -----------------------------------------------------
    # SNAPSHOT
    # -----------------------------------------------------


    def snapshot(self):

        return {

            "manager":
                self.status(),

            "state":
                workspace_state.snapshot()

        }





workspace_manager = WorkspaceManager()
