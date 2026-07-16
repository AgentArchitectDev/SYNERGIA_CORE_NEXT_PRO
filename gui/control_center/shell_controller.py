"""
===========================================================
SYNERGIA CORE NEXT_PRO

OMEGA CONTROL CENTER

SHELL CONTROLLER V3

CORE BRIDGE ARCHITECTURE

===========================================================

Responsabilidad:

Control visual del sistema.

NO ejecuta inteligencia directamente.

Comunica mediante:

CoreBridge


Arquitectura:

GUI

 |

Shell Controller

 |

Core Bridge

 |

SYNERGIA CORE


===========================================================
"""


from PySide6.QtWidgets import QApplication



from gui.control_center.main_window import (
    main_window
)


from gui.control_center.top_bar import (
    top_bar
)


from gui.control_center.side_bar import (
    side_bar
)


from gui.control_center.status_bar import (
    status_bar
)



from gui.control_center.core_bridge import (
    core_bridge
)





class ShellController:



    """
    OMEGA Shell Controller V3

    GUI Coordinator

    """



    def __init__(self):


        self.app = None


        self.window = main_window


        self.initialized = False


        self.running = False


        self.core_connected = False



        self.last_command = None


        self.last_response = None





    # =================================================
    # INITIALIZE
    # =================================================


    def initialize(self):


        if self.app is None:


            self.app = QApplication.instance()


            if self.app is None:

                self.app = QApplication([])



        self.connect_core()


        self.prepare_gui()



        self.initialized = True



        return {


            "status":
                "shell_initialized",


            "core":
                self.core_connected

        }





    # =================================================
    # CONNECT CORE
    # =================================================


    def connect_core(self):


        result = core_bridge.connect()



        self.core_connected = result[
            "connected"
        ]



        return result





    # =================================================
    # GUI PREPARE
    # =================================================


    def prepare_gui(self):


        top_bar.set_runtime(
            True
        )


        top_bar.set_status(
            "CORE BRIDGE ONLINE"
        )



        status_bar.set_runtime(
            True
        )


        status_bar.set_ai_status(
            "CONNECTED"
        )


        status_bar.set_evolution(
            "ACTIVE"
        )





    # =================================================
    # EXECUTE COMMAND
    # =================================================


    def execute(
            self,
            text
    ):


        self.last_command = text



        self.last_response = core_bridge.execute(
            text
        )



        return self.last_response





    # =================================================
    # START
    # =================================================


    def start(self):


        if not self.initialized:

            self.initialize()



        self.window.show()



        self.running = True



        return {


            "status":
                "shell_running"

        }





    # =================================================
    # STATUS
    # =================================================


    def status(self):


        return {


            "component":
                "OMEGA Shell Controller V3",


            "initialized":
                self.initialized,


            "running":
                self.running,


            "core_connected":
                self.core_connected,


            "last_command":
                self.last_command,


            "last_response":
                self.last_response,


            "core_bridge":
                core_bridge.status()

        }





shell_controller = ShellController()
