# =========================================================
# SYNERGIA LIVE EXECUTION DASHBOARD
#
# STAGE 6.3.15.7.5.1
# AI BUSINESS RUNTIME OBSERVABILITY
#
# STAGE 6.3.15.7.5.2
# LIVE DASHBOARD + PROGRESS MONITOR
#
# STAGE 6.3.15.7.6.3
# OBSERVABILITY PIPELINE
#
# STAGE 6.3.15.7.7.2
# RUNTIME MEMORY VISUALIZATION
# =========================================================


import json

from pathlib import Path

from datetime import datetime



print(
    "[LIVE DASHBOARD LOADED]"
)




class LiveDashboard:



    def __init__(self):


        self.created_at = (
            datetime.now()
            .isoformat()
        )



        self.storage = Path(
            "storage/ai_business"
        )



        self.storage.mkdir(
            parents=True,
            exist_ok=True
        )



        # =====================================
        # PROGRESS MONITOR LINK
        # =====================================

        self.monitor = None





    # =====================================================
    # CONNECT PROGRESS MONITOR
    # =====================================================


    def attach_monitor(
        self,
        monitor
    ):


        self.monitor = monitor





    # =====================================================
    # GET LIVE PROGRESS
    # =====================================================


    def get_live_progress(
        self
    ):


        if self.monitor:


            return self.monitor.status()



        return {}





    # =====================================================
    # LOAD MODEL PERFORMANCE MEMORY
    # =====================================================


    def load_model_metrics(
        self
    ):


        file = (

            self.storage /

            "model_performance.json"

        )



        if not file.exists():


            return {}



        try:


            return json.loads(

                file.read_text(
                    encoding="utf-8"
                )

            )


        except Exception:


            return {}





    # =====================================================
    # LOAD EXECUTION HISTORY
    # =====================================================


    def load_execution_history(
        self
    ):


        file = Path(
            "storage/omega_execution_history.json"
        )



        if not file.exists():


            return []



        try:


            data = json.loads(

                file.read_text(
                    encoding="utf-8"
                )

            )



            if isinstance(data, dict):


                return data.get(
                    "history",
                    data
                )



            return data



        except Exception:


            return {}





    # =====================================================
    # LOAD RUNTIME MEMORY
    # =====================================================


    def load_runtime_memory(
        self
    ):


        try:


            from ai.memory.runtime_memory import (
                RuntimeMemory
            )



            memory = RuntimeMemory()



            return memory.status()



        except Exception as e:


            return {

                "error":
                str(e)

            }





    # =====================================================
    # GENERATE LIVE STATUS
    # =====================================================


    def generate_status(
        self,
        progress=None
    ):


        return {


            "system":

                "SYNERGIA CORE NEXT PRO",



            "module":

                "LIVE EXECUTION DASHBOARD",



            "timestamp":

                datetime.now()
                .isoformat(),




            # -----------------------------
            # PROGRESS MONITOR
            # -----------------------------

            "progress":

                progress

                if progress is not None

                else self.get_live_progress(),




            # -----------------------------
            # AI MODEL METRICS
            # -----------------------------

            "models":

                self.load_model_metrics(),




            # -----------------------------
            # EXECUTION HISTORY
            # -----------------------------

            "execution_history":

                self.load_execution_history(),




            # -----------------------------
            # RUNTIME MEMORY
            # -----------------------------

            "runtime_memory":

                self.load_runtime_memory()



        }





    # =====================================================
    # PRINT DASHBOARD
    # =====================================================


    def display(
        self,
        progress=None
    ):



        data = self.generate_status(
            progress
        )



        print()

        print(
            "=============================="
        )


        print(
            "[SYNERGIA LIVE DASHBOARD]"
        )


        print(
            "=============================="
        )



        print(

            json.dumps(

                data,

                indent=4,

                ensure_ascii=False

            )

        )



        print(
            "=============================="
        )
