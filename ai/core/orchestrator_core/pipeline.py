"""
=========================================================
SYNERGIA CORE NEXT_PRO

PIPELINE V2

Motor de ejecución del Orchestrator

Compatible con:

- ExecutionContext object
- Context dictionary legacy

=========================================================
"""


from ai.core.router import router
from ai.core.scheduler import scheduler



class Pipeline:


    def execute(self, context):


        # ---------------------------------------------
        # Detectar tipo de contexto
        # ---------------------------------------------

        if hasattr(context, "input"):

            input_text = context.input

        else:

            input_text = context["input"]



        # ---------------------------------------------
        # Router cognitivo
        # ---------------------------------------------

        plan = router.route(
            input_text
        )



        # ---------------------------------------------
        # Scheduler
        # ---------------------------------------------

        results = scheduler.execute(

            input_text,

            plan

        )



        # ---------------------------------------------
        # Guardar resultados
        # ---------------------------------------------

        if hasattr(context, "plan"):


            context.plan = plan

            context.results = results

            context.status = "completed"


            return context



        else:


            context["plan"] = plan

            context["results"] = results

            context["status"] = "completed"


            return context





pipeline = Pipeline()
