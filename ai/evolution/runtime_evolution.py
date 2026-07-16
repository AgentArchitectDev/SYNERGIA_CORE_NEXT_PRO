"""
=========================================================
SYNERGIA CORE NEXT_PRO

RUNTIME EVOLUTION ADAPTER V1

Capa pública del sistema evolutivo.

=========================================================
"""


from ai.evolution.evolution_core import (
    runtime_evolution as core_runtime_evolution
)



class RuntimeEvolutionAdapter:


    def __init__(self):

        self.version = "1.0 Adapter"



    # -------------------------------------------------

    def start(self):

        return core_runtime_evolution.start()



    # -------------------------------------------------

    def analyze(self, state):

        return core_runtime_evolution.analyze(
            state
        )



    # -------------------------------------------------

    def recover(self, error):

        return core_runtime_evolution.recover(
            error
        )



    # -------------------------------------------------

    def status(self):

        return core_runtime_evolution.status()



    # -------------------------------------------------

    def info(self):

        return {

            "component":
                "Runtime Evolution Adapter",

            "version":
                self.version,

            "backend":
                "Evolution Core V1"

        }



# =====================================================
# SINGLETON
# =====================================================

runtime_evolution = RuntimeEvolutionAdapter()
