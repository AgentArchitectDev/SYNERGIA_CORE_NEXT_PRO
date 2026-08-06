# =========================================================
# AI ORCHESTRATOR - SYNERGIA CORE NEXT PRO
# STAGE 6.3.7 - ADAPTIVE MODEL ROUTING
# =========================================================

print("[AI ORCHESTRATOR LOADED]")


from ai.core_system.brain.model_ranker import (
    model_ranker
)


class AIOrchestrator:


    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):


        # ROUTING BASE ESTABLE
        #
        # Se mantiene como fallback seguro
        #

        self.routing = {


            # WEB GENERATION
            "website": "llama3.2:3b",


            # BRANDING
            "branding": "gemma3:4b",


            # SOCIAL
            "social": "llama3.2:3b",


            # DOCUMENTATION
            "docs": "mistral:latest"

        }



    # =====================================================
    # SELECT MODEL
    # ROUTING COMPATIBILITY
    # =====================================================

    def select_model(
        self,
        task_type
    ):


        model = self.routing.get(

            task_type,

            "llama3.2:3b"

        )


        print(

            f"\n[ROUTER] task={task_type} → model={model}"

        )


        return model



    # =====================================================
    # ADAPTIVE MODEL SELECTION
    # STAGE 6.3.7
    # =====================================================

    def select_best_model(
        self,
        task_type=None
    ):


        ranked_model = (

            model_ranker.best_model()

        )


        if ranked_model:


            print(

                "\n[ADAPTIVE ROUTER]"

            )

            print(

                f"TASK: {task_type}"

            )

            print(

                f"BEST MODEL: {ranked_model}"

            )


            return ranked_model



        # FALLBACK

        return self.select_model(

            task_type

        )



    # =====================================================
    # REGISTER PERFORMANCE
    # =====================================================

    def register_model_result(

        self,
        model,
        duration,
        success=True

    ):


        result = model_ranker.register_execution(

            model=model,

            duration=duration,

            success=success

        )


        print(

            "\n[MODEL PERFORMANCE UPDATED]"

        )


        print(result)


        return result



    # =====================================================
    # SCORE COMPATIBILITY
    # =====================================================

    def score_model(

        self,
        model,
        score=1

    ):


        return {

            "model": model,

            "score": score

        }



    # =====================================================
    # STATUS
    # =====================================================

    def status(self):


        return {


            "component":

            "AIOrchestrator",


            "stage":

            "6.3.7",


            "adaptive":

            True,


            "best_model":

            model_ranker.best_model()

        }





# =========================================================
# SINGLETON GLOBAL
# =========================================================

ai_orchestrator = AIOrchestrator()
