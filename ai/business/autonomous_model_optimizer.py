# =========================================================
# SYNERGIA AUTONOMOUS MODEL OPTIMIZER
#
# STAGE 6.3.15.7.8
#
# AUTONOMOUS MODEL OPTIMIZATION ENGINE
#
# Uses:
# - Runtime Memory
# - Adaptive Scores
# - Historical Performance
#
# =========================================================


from datetime import datetime


print(
    "[AUTONOMOUS MODEL OPTIMIZER LOADED]"
)



try:

    from ai.memory.runtime_memory import (
        runtime_memory
    )

except Exception:

    runtime_memory = None



class AutonomousModelOptimizer:


    def __init__(
        self,
        memory=None
    ):


        self.memory = (
            memory
            if memory
            else runtime_memory
        )



    # =====================================================
    # ANALYZE TASK PERFORMANCE
    # =====================================================

    def analyze_task(
        self,
        task
    ):


        if not self.memory:

            return {
                "status":
                    "NO_MEMORY"
            }



        experiences = (

            self.memory.get_experiences()

        )



        filtered = [

            item

            for item in experiences

            if item.get(
                "task",
                ""
            ).upper()
            ==
            task.upper()

        ]



        if not filtered:


            return {

                "status":
                    "NO_DATA",

                "task":
                    task

            }



        models = {}



        for item in filtered:


            model = item.get(
                "model"
            )


            if model not in models:

                models[model] = {

                    "executions": 0,

                    "success": 0,

                    "times": []

                }


            models[model]["executions"] += 1


            if item.get(
                "status"
            ) == "SUCCESS":

                models[model]["success"] += 1


            models[model]["times"].append(

                item.get(
                    "duration_seconds",
                    999999
                )

            )



        ranking = []



        for model,data in models.items():


            avg_time = (

                sum(data["times"])
                /
                len(data["times"])

            )


            success_rate = (

                data["success"]
                /
                data["executions"]

            )



            score = round(

                (
                    success_rate * 70
                )
                +
                (
                    max(
                        0,
                        30 -
                        avg_time / 10
                    )
                ),

                2

            )



            ranking.append(

                {

                    "model":
                        model,

                    "score":
                        score,

                    "success_rate":
                        success_rate,

                    "average_time":
                        avg_time

                }

            )



        ranking.sort(

            key=lambda x:
            x["score"],

            reverse=True

        )



        return {


            "status":
                "ANALYZED",


            "task":
                task,


            "best_model":
                ranking[0]["model"],


            "ranking":
                ranking,


            "timestamp":
                datetime.now()
                .isoformat()

        }
