from datetime import datetime

from ai.business.business_resource_optimizer import (
    BusinessResourceOptimizer
)



print("[BUSINESS PERFORMANCE LOADED]")


class BusinessPerformance:


    def __init__(self):

        self.tasks = []

        self.optimizer = (
            BusinessResourceOptimizer()
        )
        self.start_time = None
        self.end_time = None


    def start(self):

        self.start_time = datetime.now()


    def add_task(
        self,
        task,
        model,
        duration,
        status="SUCCESS"
    ):

        self.tasks.append(
            {
                "task": task,
                "model": model,
                "duration_seconds": duration,
                "status": status,
                "timestamp": datetime.now().isoformat()
            }
        )


        self.optimizer.add_model(
            task,
            model,
            duration,
            status == "SUCCESS"
        )


    def finish(self):

        self.end_time = datetime.now()



    def resource_report(
        self
    ):

        return (
            self.optimizer.generate_report()
        )


    def report(self):

        total = 0

        for task in self.tasks:
            total += task["duration_seconds"]


        fastest = None
        slowest = None


        if self.tasks:

            fastest = min(
                self.tasks,
                key=lambda x: x["duration_seconds"]
            )


            slowest = max(
                self.tasks,
                key=lambda x: x["duration_seconds"]
            )


        return {

            "tasks": self.tasks,

            "total_seconds": round(
                total,
                2
            ),

            "fastest_task": fastest,

            "slowest_task": slowest,

            "generated_at":
                datetime.now().isoformat()

        }
