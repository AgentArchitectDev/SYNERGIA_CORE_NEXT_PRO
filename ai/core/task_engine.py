# =========================================================
# SYNERGIA TASK ENGINE
# COMPATIBILITY + LEGACY BUSINESS SUPPORT
#
# STAGE 6.3.1
# AI RUNTIME EXECUTION HISTORY
#
# STAGE 6.3.15.7.4.2.3
# TASK ENGINE + PROGRESS MONITOR
#
# STAGE 6.3.15.7.5.2
# LIVE DASHBOARD INTEGRATION
#
# STAGE 6.3.15.7.6.3
# REAL PIPELINE OBSERVABILITY
#
# STAGE 6.3.15.7.7.1
# RUNTIME MEMORY INTEGRATION
# =========================================================


from datetime import datetime
import time


from ai.runtime.execution_history import (
    execution_history
)


from ai.runtime.progress_monitor import (
    ProgressMonitor
)


from ai.runtime.live_dashboard import (
    LiveDashboard
)


from ai.memory.runtime_memory import (
    RuntimeMemory
)



print(
    "[TASK ENGINE LOADED]"
)



class TaskEngine:


    def __init__(self):


        # =========================================
        # BUSINESS TASK QUEUE
        # =========================================

        self.tasks = []



        # =========================================
        # RUNTIME OBSERVABILITY
        # =========================================

        self.monitor = None


        self.dashboard = LiveDashboard()



        # =========================================
        # AI EXPERIENCE MEMORY
        # =========================================

        self.memory = RuntimeMemory()



    # =====================================================
    # ADD TASK
    # =====================================================


    def add_task(
        self,
        name,
        function
    ):


        if not callable(function):

            raise TypeError(
                f"Task '{name}' is not callable"
            )


        self.tasks.append(
            {
                "name": name,
                "function": function,
            }
        )


        print(
            f"[TASK ADDED] {name}"
        )



    # =====================================================
    # RUN TASK QUEUE
    # =====================================================


    def run(self):


        results = []


        total = len(
            self.tasks
        )



        print(
            f"\n[TASK ENGINE] Running {total} task(s)"
        )



        # =========================================
        # CREATE MONITOR
        # =========================================

        self.monitor = ProgressMonitor(
            total_tasks=total
        )



        self.dashboard.attach_monitor(
            self.monitor
        )



        for index, task in enumerate(
            self.tasks,
            start=1
        ):


            name = task["name"]


            print(
                f"\n[TASK {index}/{total}] {name}"
            )


            start_time = time.time()


            model_used = "AUTO"



            try:


                self.monitor.start_task(
                    name,
                    model_used
                )



                result = (
                    task["function"]()
                )



                duration = round(
                    time.time() - start_time,
                    2
                )



                self.monitor.complete_task(
                    name
                )



                execution_history.register(
                    task=name,
                    node="MAQ2",
                    result="completed"
                )



                # =====================================
                # SAVE EXPERIENCE MEMORY
                # =====================================

                self.memory.add_experience(

                    task=name,

                    model=model_used,

                    status="SUCCESS",

                    duration_seconds=duration,

                    metadata={
                        "stage":
                        "6.3.15.7.7.1",
                        "source":
                        "TaskEngine"
                    }

                )



                results.append(
                    {
                        "name": name,
                        "status": "success",
                        "result": result,
                        "duration_seconds": duration
                    }
                )



                print(
                    f"[TASK OK] {name}"
                )



            except Exception as e:



                duration = round(
                    time.time() - start_time,
                    2
                )



                execution_history.register(
                    task=name,
                    node="MAQ2",
                    result="failed"
                )



                # =====================================
                # SAVE FAILED EXPERIENCE
                # =====================================

                self.memory.add_experience(

                    task=name,

                    model=model_used,

                    status="FAILED",

                    duration_seconds=duration,

                    metadata={
                        "error": str(e),
                        "stage":
                        "6.3.15.7.7.1"
                    }

                )



                results.append(
                    {
                        "name": name,
                        "status": "error",
                        "error": str(e),
                        "duration_seconds": duration
                    }
                )



                print(
                    f"[TASK ERROR] {name}"
                )


                print(
                    str(e)
                )



        successful = sum(

            1

            for item in results

            if item["status"] == "success"

        )



        failed = total - successful



        summary = {


            "total":
                total,


            "successful":
                successful,


            "failed":
                failed,


            "results":
                results,


            "monitor":

                self.monitor.status()

            if self.monitor

            else {},


            "memory":

                self.memory.status()

        }



        print()

        print(
            "[TASK ENGINE FINISHED]"
        )


        print(
            f"SUCCESS: {successful}"
        )


        print(
            f"FAILED: {failed}"
        )



        return summary




    # =====================================================
    # MODERN EXECUTION API
    # =====================================================


    def execute(
        self,
        user_input,
        context=None
    ):



        text = user_input.lower()



        if "calcular" in text:


            return {

                "type":
                "calculator",

                "input":
                user_input

            }



        return {


            "type":
            "generic",

            "input":
            user_input,

            "context":
            context

        }
