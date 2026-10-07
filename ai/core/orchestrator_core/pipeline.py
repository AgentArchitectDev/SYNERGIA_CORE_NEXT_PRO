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

            plan,

            execution_envelope=getattr(
                context,
                "execution_envelope",
                None,
            ),

            execution_grant=getattr(
                context,
                "execution_grant",
                None,
            ),

        )



        # ---------------------------------------------
        # Guardar resultados
        # ---------------------------------------------

        if hasattr(context, "plan"):


            context.plan = plan

            context.results = results

            blocked = any(
                isinstance(result, dict)
                and result.get("status") in {"BLOCKED", "error"}
                for result in results
            )

            context.status = "blocked" if blocked else "completed"


            return context



        else:


            context["plan"] = plan

            context["results"] = results

            blocked = any(
                isinstance(result, dict)
                and result.get("status") in {"BLOCKED", "error"}
                for result in results
            )

            context["status"] = "blocked" if blocked else "completed"


            return context





pipeline = Pipeline()
