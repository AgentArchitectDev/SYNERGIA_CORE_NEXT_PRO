"""
===========================================================
SYNERGIA CORE NEXT_PRO
OMEGA WORKSPACE CONTROLLER V1
===========================================================

Controlador principal del Workspace.

Responsabilidades:

- Coordinar Workspace Manager
- Gestionar navegación interna
- Controlar módulos
- Controlar paneles
- Controlar tabs
- Exponer estado global

Arquitectura:

Navigation V6
      |
      |
Workspace Controller
      |
      |
Workspace Manager
      |
      |
Workspace State


===========================================================
"""


from gui.workspace.workspace_manager import workspace_manager



class WorkspaceController:


    """
    Workspace Controller OMEGA V1
    """



    def __init__(self):

        self.initialized = False



    # -----------------------------------------------------
    # INIT
    # -----------------------------------------------------


    def initialize(self):

        result = workspace_manager.initialize()

        self.initialized = True


        return {

            "status":
                "workspace_ready",

            "manager":
                result

        }



    # -----------------------------------------------------
    # MODULES
    # -----------------------------------------------------


    def open(
            self,
            module
    ):

        return workspace_manager.open(
            module
        )



    # -----------------------------------------------------
    # PANELS
    # -----------------------------------------------------


    def open_panel(
            self,
            panel
    ):

        return workspace_manager.activate_panel(
            panel
        )



    # -----------------------------------------------------
    # TABS
    # -----------------------------------------------------


    def open_tab(
            self,
            tab
    ):

        return workspace_manager.activate_tab(
            tab
        )



    # -----------------------------------------------------
    # REGISTRATION
    # -----------------------------------------------------


    def register_module(
            self,
            name,
            module
    ):

        return workspace_manager.register_module(
            name,
            module
        )



    def register_panel(
            self,
            name,
            panel
    ):

        return workspace_manager.register_panel(
            name,
            panel
        )



    def register_tab(
            self,
            name,
            tab
    ):

        return workspace_manager.register_tab(
            name,
            tab
        )



    # -----------------------------------------------------
    # STATUS
    # -----------------------------------------------------


    def status(self):

        return {

            "controller":
                "OMEGA Workspace Controller",

            "initialized":
                self.initialized,

            "manager":
                workspace_manager.status()

        }



    # -----------------------------------------------------
    # SNAPSHOT
    # -----------------------------------------------------


    def snapshot(self):

        return {

            "controller":
                self.status(),

            "workspace":
                workspace_manager.snapshot()

        }




workspace_controller = WorkspaceController()
