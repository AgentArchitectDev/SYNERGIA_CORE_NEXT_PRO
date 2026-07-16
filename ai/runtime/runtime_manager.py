"""
=========================================================
SYNERGIA CORE NEXT_PRO

RUNTIME MANAGER EVOLUTION V2

Responsabilidades:

- Control principal de ejecución
- Comunicación con Orchestrator
- Registro evolutivo
- Cognitive Loop
- Self Improvement

=========================================================
"""


import time


from ai.core.orchestrator import orchestrator


from ai.core.self_improving_loop import (
    self_improving_loop
)


# Evolution Bridge

try:

    from ai.evolution.evolution_core.evolution_bridge import (
        evolution_bridge
    )

except Exception:

    evolution_bridge = None



# Cognitive Layer

try:

    from ai.cognitive.cognitive_loop import (
        cognitive_loop
    )

except Exception:

    cognitive_loop = None





class RuntimeManager:



    def __init__(self):

        self.started = False

        self.start_time = None

        self.last_result = None

        self.executions = 0



    # -------------------------------------------------

    def start(self):


        self.started = True

        self.start_time = time.time()



        # iniciar cognitive loop

        if cognitive_loop:

            cognitive_loop.start()



        return {

            "status":
                "started",

            "mode":
                "evolution"

        }




    # -------------------------------------------------

    def execute(
            self,
            input_text: str
    ):


        if not self.started:

            self.start()



        start = time.time()



        # ----------------------------
        # Cognitive observation
        # ----------------------------

        cognitive_result = None


        if cognitive_loop:

            cognitive_result = (
                cognitive_loop.process(
                    input_text
                )
            )



        # ----------------------------
        # Main execution
        # ----------------------------

        result = orchestrator.run(
            input_text
        )



        self.last_result = result


        self.executions += 1



        latency = (
            time.time()
            -
            start
        )



        # ----------------------------
        # Evolution record
        # ----------------------------


        if evolution_bridge:


            evolution_bridge.record_execution(

                "runtime",

                success=True,

                latency=latency

            )




        return {


            "result":
                result,


            "cognitive":
                cognitive_result,


            "latency":
                latency

        }





    # -------------------------------------------------

    def evolve(self):


        return (
            self_improving_loop.optimize()
        )




    # -------------------------------------------------

    def status(self):


        return {


            "started":
                self.started,


            "uptime":
                (
                    time.time()
                    -
                    self.start_time
                )
                if self.start_time
                else 0,


            "executions":
                self.executions,


            "last":
                self.last_result,


            "evolution":
                self_improving_loop.status()


        }





# =====================================================
# SINGLETON
# =====================================================


runtime_manager = RuntimeManager()
