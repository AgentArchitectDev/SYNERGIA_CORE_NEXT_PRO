"""
=========================================================
SYNERGIA CORE NEXT_PRO

COGNITIVE LOOP ADAPTER V1

Compatibility Layer

=========================================================
"""


from ai.cognitive.cognitive_core import (
    cognitive_loop as core_cognitive_loop
)



class CognitiveLoopAdapter:


    def __init__(self):

        self.version = "1.0 Adapter"



    # -------------------------------------------------

    def start(self):

        return core_cognitive_loop.start()



    # -------------------------------------------------

    def process(self, data):

        return core_cognitive_loop.process(
            data
        )



    # -------------------------------------------------

    def status(self):

        return core_cognitive_loop.status()



    # -------------------------------------------------

    def info(self):

        return {

            "component":
                "Cognitive Loop Adapter",

            "version":
                self.version,

            "backend":
                "Cognitive Core V1"

        }



# =====================================================
# SINGLETON
# =====================================================

cognitive_loop = CognitiveLoopAdapter()
