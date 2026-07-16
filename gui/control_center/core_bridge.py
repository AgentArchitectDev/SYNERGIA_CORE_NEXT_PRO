"""
===========================================================
SYNERGIA CORE NEXT_PRO

OMEGA CONTROL CENTER

CORE BRIDGE V2.1

RUNTIME INTEGRATION + COMMAND NORMALIZER

===========================================================

Arquitectura:

SHELL CONTROLLER

        |

CORE BRIDGE V2.1

        |

+---------------------------+

| Cognitive Router           |
| Runtime Connector          |
| Model Layer                |

+---------------------------+

        |

RUNTIME LAYER

        |

MAQ1 / MAQ2


===========================================================
"""


import unicodedata


from gui.control_center.runtime_connector import (
    runtime_connector
)





class CoreBridge:



    """
    OMEGA Core Bridge V2.1


    Orquestador principal entre:

    - comandos
    - planificación
    - runtime
    - ejecución


    """



    def __init__(self):


        self.connected = False


        self.executions = 0


        self.last_command = None


        self.last_plan = []


        self.runtime = False



    # =====================================================
    # CONNECT
    # =====================================================


    def connect(self):


        runtime_status = runtime_connector.connect()



        self.runtime = (
            runtime_status["status"]
            ==
            "runtime_connected"
        )



        self.connected = True



        return {


            "connected":
                True,


            "runtime":
                self.runtime

        }





    # =====================================================
    # COMMAND NORMALIZER
    # =====================================================


    def normalize_command(
            self,
            command
    ):


        """
        Normaliza lenguaje humano.

        Ejemplos:

        evolución
        evolucion
        EVOLUCIÓN

        quedan:

        evolucion

        """



        command = command.lower()



        command = unicodedata.normalize(
            "NFD",
            command
        )



        command = "".join(

            char

            for char in command

            if unicodedata.category(char)
            !=
            "Mn"

        )



        return command.strip()





    # =====================================================
    # BUILD PLAN
    # =====================================================


    def build_plan(
            self,
            command
    ):



        command = self.normalize_command(
            command
        )



        plan = []



        # -----------------------------
        # OLLAMA / MODELS
        # -----------------------------


        if (
            "ollama"
            in command
        ):


            plan.extend(

                [

                    "runtime",

                    "ollama"

                ]

            )



        # -----------------------------
        # MODELOS
        # -----------------------------


        elif (
            "modelo"
            in command
            or
            "model"
            in command
        ):


            plan.append(
                "models"
            )



        # -----------------------------
        # EVOLUTION
        # -----------------------------


        elif (

            "evolucion"
            in command

            or

            "evolution"
            in command

        ):


            plan.append(
                "evolution"
            )



        # -----------------------------
        # AGENTES
        # -----------------------------


        elif (

            "agente"
            in command

            or

            "agent"
            in command

        ):


            plan.append(
                "agent"
            )



        # -----------------------------
        # DEFAULT CORE
        # -----------------------------


        else:


            plan.append(
                "core"
            )



        return plan





    # =====================================================
    # EXECUTE
    # =====================================================


    def execute(
            self,
            command
    ):



        if not self.connected:


            self.connect()



        plan = self.build_plan(
            command
        )



        self.executions += 1



        self.last_command = command



        self.last_plan = plan



        runtime_result = None



        if "runtime" in plan:


            runtime_result = runtime_connector.execute(

                command

            )



        return {


            "command":
                command,


            "plan":
                plan,


            "execution":
                self.executions,


            "runtime":
                runtime_result

        }





    # =====================================================
    # STATUS
    # =====================================================


    def status(
            self
    ):



        return {


            "component":

                "OMEGA Core Bridge V2.1",



            "connected":

                self.connected,



            "runtime":

                self.runtime,



            "executions":

                self.executions,



            "last_command":

                self.last_command,



            "last_plan":

                self.last_plan,



            "runtime_status":

                runtime_connector.status()

        }





# =========================================================
# SINGLETON
# =========================================================


core_bridge = CoreBridge()
