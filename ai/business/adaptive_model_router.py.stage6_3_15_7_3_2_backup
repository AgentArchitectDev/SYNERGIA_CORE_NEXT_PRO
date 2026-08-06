from datetime import datetime


print("[ADAPTIVE MODEL ROUTER LOADED]")


class AdaptiveModelRouter:

    def __init__(self, optimizer=None):

        self.optimizer = optimizer


    def select_model(
        self,
        task,
        default_model=None
    ):

        if self.optimizer:

            recommendation = (
                self.optimizer.recommend_model(task)
            )

            if recommendation.get(
                "recommendation"
            ):

                return {
                    "task": task,
                    "model": recommendation["recommendation"],
                    "reason": recommendation["reason"],
                    "time": recommendation.get(
                        "time"
                    ),
                    "timestamp":
                        datetime.now().isoformat()
                }


        return {
            "task": task,
            "model": default_model,
            "reason": "DEFAULT FALLBACK",
            "timestamp":
                datetime.now().isoformat()
        }
