from datetime import datetime
from ai.business.model_performance_memory import ModelPerformanceMemory


print("[BUSINESS RESOURCE OPTIMIZER LOADED]")


class BusinessResourceOptimizer:

    def __init__(self):

        self.models = []

        self.memory = ModelPerformanceMemory()


        historical = self.memory.load()


        for model, data in historical.items():

            self.models.append(
                {
                    "task": "HISTORICAL",
                    "model": model,
                    "duration_seconds":
                        data.get(
                            "average_time",
                            0
                        ),
                    "success":
                        data.get(
                            "success",
                            0
                        ) > 0,
                    "timestamp":
                        data.get(
                            "last_execution"
                        )
                }
            )


    def add_model(
        self,
        task,
        model,
        duration_seconds,
        success=True
    ):

        self.models.append(
            {
                "task": task,
                "model": model,
                "duration_seconds": duration_seconds,
                "success": success,
                "timestamp": datetime.now().isoformat()
            }
        )


        self.memory.update_model(
            model=model,
            success=success,
            duration=duration_seconds
        )


    def calculate_efficiency(
        self
    ):

        report = {}

        for item in self.models:

            model = item["model"]

            if model not in report:

                report[model] = {
                    "uses": 0,
                    "success": 0,
                    "total_time": 0
                }


            report[model]["uses"] += 1

            if item["success"]:
                report[model]["success"] += 1

            report[model]["total_time"] += (
                item["duration_seconds"]
            )


        for model in report:

            data = report[model]

            data["average_time"] = round(
                data["total_time"] /
                data["uses"],
                2
            )

            data["success_rate"] = round(
                (
                    data["success"] /
                    data["uses"]
                ) * 100,
                2
            )


        return report



    def recommend_model(
        self,
        task
    ):

        candidates = [
            x for x in self.models
            if x["task"] == task
            and x["success"]
        ]


        if not candidates:

            return {
                "task": task,
                "recommendation": None,
                "reason": "NO DATA"
            }


        best = sorted(
            candidates,
            key=lambda x:
            x["duration_seconds"]
        )[0]


        return {
            "task": task,
            "recommendation": best["model"],
            "reason":
                "FASTEST SUCCESSFUL MODEL",
            "time":
                best["duration_seconds"]
        }



    def generate_report(
        self
    ):

        return {

            "models":
                self.models,

            "efficiency":
                self.calculate_efficiency(),

            "generated_at":
                datetime.now().isoformat()

        }
