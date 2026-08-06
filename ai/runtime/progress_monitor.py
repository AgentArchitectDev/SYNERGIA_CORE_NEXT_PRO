import time
from datetime import datetime


print("[PROGRESS MONITOR LOADED]")


class ProgressMonitor:

    def __init__(
        self,
        total_tasks=1
    ):

        self.total_tasks = total_tasks
        self.completed_tasks = 0
        self.current_task = None
        self.current_model = None
        self.start_time = time.time()


    def start_task(
        self,
        task,
        model=None
    ):

        self.current_task = task
        self.current_model = model

        self.display(
            "RUNNING"
        )


    def complete_task(
        self,
        task
    ):

        self.completed_tasks += 1
        self.current_task = task

        self.display(
            "COMPLETED"
        )


    def get_progress(self):

        return round(
            (
                self.completed_tasks /
                self.total_tasks
            ) * 100,
            2
        )


    def get_elapsed(self):

        return round(
            time.time() -
            self.start_time,
            2
        )


    def get_remaining_estimate(self):

        if self.completed_tasks == 0:
            return None

        average = (
            self.get_elapsed() /
            self.completed_tasks
        )

        remaining = (
            self.total_tasks -
            self.completed_tasks
        )

        return round(
            average * remaining,
            2
        )


    def status(self):

        return {

            "progress":
                self.get_progress(),

            "completed_tasks":
                self.completed_tasks,

            "total_tasks":
                self.total_tasks,

            "current_task":
                self.current_task,

            "current_model":
                self.current_model,

            "elapsed_seconds":
                self.get_elapsed(),

            "eta_seconds":
                self.get_remaining_estimate(),

            "timestamp":
                datetime.now().isoformat()
        }



    def display(
        self,
        status
    ):

        print()
        print("==============================")
        print("[SYNERGIA EXECUTION MONITOR]")
        print("==============================")

        print(
            "STATUS:",
            status
        )

        print(
            "PROGRESS:",
            f"{self.get_progress()}%"
        )

        print(
            "CURRENT TASK:",
            self.current_task
        )

        print(
            "MODEL:",
            self.current_model
        )

        print(
            "ELAPSED:",
            self.get_elapsed(),
            "seconds"
        )

        print(
            "ETA:",
            self.get_remaining_estimate(),
            "seconds"
        )

        print(
            "TIME:",
            datetime.now().isoformat()
        )

        print("==============================")
