"""
===============================================================
SYNERGIA CORE NEXT_PRO

ORCHESTRATOR ADAPTER V5.1 ENTERPRISE

Capa pública de compatibilidad.

Responsabilidades:

- Mantener compatibilidad con Runtime Manager
- Exponer interfaz estándar run()
- Conectar con Orchestrator Core
- Manejar errores
- Proveer health/status/info

Arquitectura:

run.py
   |
   ▼
Runtime Manager
   |
   ▼
Orchestrator Adapter
   |
   ▼
Orchestrator Core
   |
   ▼
Pipeline
   |
   ▼
Router Cognitivo
   |
   ▼
Scheduler
   |
   ▼
Agents
   |
   ▼
Memory / Knowledge Graph

===============================================================
"""


import time



# =============================================================
# IMPORT CORE
# =============================================================


try:

    from ai.core.orchestrator_core import (
        orchestrator as core_orchestrator
    )

except Exception as e:

    core_orchestrator = None

    CORE_IMPORT_ERROR = str(e)

else:

    CORE_IMPORT_ERROR = None





# =============================================================
# ADAPTER
# =============================================================


class OrchestratorAdapter:


    def __init__(self):

        self.version = "5.1 Enterprise Adapter"

        self.started = False

        self.executions = 0

        self.last_execution = None



    # =========================================================
    # MAIN INTERFACE
    # =========================================================


    def run(self, input_text: str):
        """
        Interface principal usada por:

        Runtime Manager
        Scheduler
        Servicios externos

        """

        return self.process(
            input_text
        )



    # =========================================================
    # PROCESS
    # =========================================================


    def process(self, input_text: str):


        self.executions += 1


        start = time.time()



        if not core_orchestrator:


            return {

                "status":
                    "error",

                "message":
                    "Orchestrator Core unavailable",

                "error":
                    CORE_IMPORT_ERROR

            }




        try:


            result = (
                core_orchestrator.run(
                    input_text
                )
            )


            status = "success"



        except Exception as e:


            result = {

                "status":
                    "error",

                "error":
                    str(e)

            }


            status = "error"



        latency = (
            time.time()
            -
            start
        )



        self.last_execution = {


            "input":
                input_text,


            "status":
                status,


            "latency":
                latency


        }



        return result




    # =========================================================
    # STATUS
    # =========================================================


    def status(self):


        core_status = {}



        if core_orchestrator:


            try:

                core_status = (
                    core_orchestrator.status()
                )


            except Exception as e:

                core_status = {

                    "error":
                        str(e)

                }



        return {


            "component":
                "Orchestrator Adapter",


            "version":
                self.version,


            "executions":
                self.executions,


            "last":
                self.last_execution,


            "core":
                core_status

        }




    # =========================================================
    # HEALTH
    # =========================================================


    def health(self):


        if not core_orchestrator:


            return {


                "status":
                    "error",


                "component":
                    "Orchestrator Core",


                "error":
                    CORE_IMPORT_ERROR

            }



        try:


            return {


                "status":
                    "healthy",


                "component":
                    "Orchestrator Adapter",


                "core":
                    core_orchestrator.health()

            }



        except Exception as e:


            return {


                "status":
                    "error",

                "error":
                    str(e)

            }




    # =========================================================
    # START / STOP
    # =========================================================


    def start(self):


        self.started = True


        if core_orchestrator and hasattr(
            core_orchestrator,
            "start"
        ):

            return core_orchestrator.start()



        return {


            "status":
                "started"

        }




    def stop(self):


        self.started = False



        if core_orchestrator and hasattr(
            core_orchestrator,
            "stop"
        ):

            return core_orchestrator.stop()



        return {


            "status":
                "stopped"

        }





    # =========================================================
    # INFO
    # =========================================================


    def info(self):


        return {


            "component":
                "Orchestrator Adapter",


            "version":
                self.version,


            "backend":
                "Orchestrator Core",


            "interface":
                [

                    "run",

                    "process",

                    "status",

                    "health"

                ]

        }





# =============================================================
# SINGLETON
# =============================================================


orchestrator = OrchestratorAdapter()
