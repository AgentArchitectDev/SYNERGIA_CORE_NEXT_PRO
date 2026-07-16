import time


class RuntimeState:

    def __init__(self):

        self.boot_time = time.time()

        self.running = False

        self.current_task = None

        self.total_tasks = 0

        self.total_errors = 0

    def start(self):

        self.running = True

    def stop(self):

        self.running = False

    def status(self):

        return {

            "running": self.running,

            "uptime": round(
                time.time() - self.boot_time,
                2
            ),

            "tasks": self.total_tasks,

            "errors": self.total_errors,

            "current_task": self.current_task

        }


runtime_state = RuntimeState()
