"""
=========================================================
SYNERGIA CORE NEXT_PRO

EXECUTION CONTEXT V2

Contexto estándar de ejecución

Compatibilidad:

- Orchestrator Core V5
- Pipeline
- Scheduler
- Servicios legacy

=========================================================
"""


import time



class ExecutionContext:


    def __init__(self, input_text=None):


        self.input = input_text

        self.timestamp = time.time()

        self.plan = []

        self.results = []

        self.status = "created"



    # -------------------------------------------------

    def add_plan(self, module):

        self.plan.append(module)



    # -------------------------------------------------

    def add_result(self, result):

        self.results.append(result)



    # -------------------------------------------------

    def to_dict(self):

        return {


            "input":
                self.input,


            "timestamp":
                self.timestamp,


            "plan":
                self.plan,


            "results":
                self.results,


            "status":
                self.status

        }




    # -------------------------------------------------

    # COMPATIBILIDAD LEGACY

    # -------------------------------------------------

    def create(self, text):


        return ExecutionContext(
            text
        ).to_dict()





# singleton legacy

execution_context = ExecutionContext()
