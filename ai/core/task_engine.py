# =========================================================
#
# SYNERGIA TASK ENGINE
#
# RUNTIME MEMORY INTEGRATION
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
# STAGE 6.3.15.7.7.2
# TASK ENGINE → RUNTIME MEMORY
# AUTOMATIC EXPERIENCE STORAGE
#
# STAGE 6.3.15.7.9.1
# REAL MODEL TRACKING
#
# AdaptiveModelRouter
#        ↓
# Generator
#        ↓
# TaskEngine
#        ↓
# RuntimeMemory
#        ↓
# Learning Loop
#
# =========================================================


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



# =========================================================
# RUNTIME MEMORY
# =========================================================


from ai.memory.runtime_memory import (
    runtime_memory
)



print(
    "[TASK ENGINE LOADED]"
)



print(
    "[TASK ENGINE RUNTIME MEMORY ENABLED]"
)



print(
    "[TASK ENGINE REAL MODEL TRACKING ENABLED]"
)



# =========================================================
# TASK ENGINE
# =========================================================


class TaskEngine:



    def __init__(self):


        # =========================================
        # BUSINESS TASK QUEUE
        # =========================================


        self.tasks = []



        # =========================================
        # RUNTIME COMPONENTS
        # =========================================


        self.monitor = None



        self.dashboard = LiveDashboard()



    # =====================================================
    # ADD TASK
    # =====================================================


    def add_task(

        self,

        name,

        function,

        model=None

    ):



        if not callable(function):


            raise TypeError(

                f"Task '{name}' is not callable"

            )



        self.tasks.append(

            {

                "name":

                    name,


                "function":

                    function,


                "model":

                    model

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



        print()



        print(

            f"[TASK ENGINE] Running {total} task(s)"

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



        # =========================================
        # EXECUTION LOOP
        # =========================================


        for index, task in enumerate(

            self.tasks,

            start=1

        ):



            name = task["name"]



            requested_model = task.get(

                "model",

                "AUTO"

            )



            print()



            print(

                f"[TASK {index}/{total}] {name}"

            )



            start_time = time.time()



            try:



                self.monitor.start_task(

                    name,

                    requested_model

                )



                # =====================================
                # EXECUTE GENERATOR
                # =====================================


                result = (

                    task["function"]()

                )



                duration = round(

                    time.time() - start_time,

                    2

                )



                # =====================================
                # REAL MODEL TRACKING
                #
                # STAGE 6.3.15.7.9.1
                #
                # Capture the model returned
                # by generators
                # =====================================


                real_model = requested_model



                model_source = "TASK_DEFAULT"



                if isinstance(result, dict):


                    real_model = result.get(

                        "model",

                        requested_model

                    )



                    if "model" in result:


                        model_source = (

                            "GENERATOR_OUTPUT"

                        )



                self.monitor.complete_task(

                    name

                )



                # =====================================
                # EXECUTION HISTORY
                # =====================================


                execution_history.register(

                    task=name,

                    node="MAQ2",

                    result="completed"

                )



                # =====================================
                # RUNTIME EXPERIENCE MEMORY
                #
                # REAL MODEL STORAGE
                # =====================================


                runtime_memory.add_experience(

                    task=name,

                    model=real_model,

                    status="SUCCESS",

                    duration_seconds=duration,

                    metadata={

                        "result_type":

                            type(result).__name__,


                        "requested_model":

                            requested_model,


                        "real_model":

                            real_model,


                        "model_source":

                            model_source,


                        "stage":

                            "6.3.15.7.9.1"

                    }

                )
                results.append(

                    {

                        "name":

                            name,


                        "status":

                            "success",


                        "result":

                            result,


                        "model":

                            real_model,


                        "duration_seconds":

                            duration

                    }

                )



                print(

                    f"[TASK OK] {name}"

                )



                print(

                    f"[REAL MODEL] {real_model}"

                )



            except Exception as e:



                duration = round(

                    time.time() - start_time,

                    2

                )



                # =====================================
                # FAILED EXECUTION HISTORY
                # =====================================


                execution_history.register(

                    task=name,

                    node="MAQ2",

                    result="failed"

                )



                # =====================================
                # FAILED EXPERIENCE MEMORY
                # =====================================


                runtime_memory.add_experience(

                    task=name,

                    model=requested_model,

                    status="FAILED",

                    duration_seconds=duration,

                    metadata={

                        "error":

                            str(e),


                        "requested_model":

                            requested_model,


                        "stage":

                            "6.3.15.7.9.1"

                    }

                )



                results.append(

                    {

                        "name":

                            name,


                        "status":

                            "error",


                        "error":

                            str(e),


                        "model":

                            requested_model,


                        "duration_seconds":

                            duration

                    }

                )



                print(

                    f"[TASK ERROR] {name}"

                )



                print(

                    str(e)

                )



        # =========================================
        # EXECUTION SUMMARY
        # =========================================


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

                runtime_memory.status()

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



        print()



        print(

            "[RUNTIME MEMORY STATUS]"

        )



        print(

            runtime_memory.status()

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


                "message":

                    "Calculation request detected"

            }



        return {


            "type":

                "general",


            "input":

                user_input,


            "context":

                context

        }
