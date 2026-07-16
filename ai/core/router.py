"""
===========================================================
SYNERGIA CORE NEXT_PRO

Router Adapter V5

Compatibilidad entre módulos legacy
y Cognitive Router V5.

===========================================================
"""


from ai.core.cognitive_router import router as cognitive_router



class RouterAdapter:


    def route(self, text: str):

        return cognitive_router.route(
            text
        )



    def status(self):

        return cognitive_router.status()



# Singleton público

router = RouterAdapter()
