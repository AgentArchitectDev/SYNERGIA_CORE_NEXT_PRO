# ============================================================
# SYNERGIA OS
#
# SELF LEARNING LOOP ENGINE ACEA
#
# STAGE 6.3.15.7.10.2
#
# AI BUSINESS SELF LEARNING CORE
#
# RESPONSIBILITY:
#
# Analyze execution experience,
# store learning history,
# generate autonomous optimization knowledge.
#
# ============================================================


from datetime import datetime
from pathlib import Path
import json


from ai.memory.runtime_memory import (
    runtime_memory
)


print(
    "[SELF LEARNING LOOP LOADED]"
)



# ============================================================
# STORAGE
# ============================================================


LEARNING_PATH = Path(
    "storage/ai_learning/self_learning_history.json"
)


LEARNING_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)



# ============================================================
# SELF LEARNING ENGINE
# ============================================================


class SelfLearningLoop:


    def __init__(self):

        self.last_analysis = None

        self.history = self.load_history()


        print(
            "[SELF LEARNING ENGINE READY]"
        )



    # ========================================================
    # LOAD HISTORY
    # ========================================================


    def load_history(self):


        if LEARNING_PATH.exists():

            try:

                with open(
                    LEARNING_PATH,
                    "r",
                    encoding="utf-8"
                ) as file:

                    data = json.load(file)


                print(
                    "[SELF LEARNING HISTORY LOADED]"
                )


                return data


            except Exception as error:

                print(
                    "[SELF LEARNING HISTORY ERROR]",
                    error
                )

                return []


        return []



    # ========================================================
    # SAVE HISTORY
    # ========================================================


    def save_history(self):


        with open(
            LEARNING_PATH,
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(
                self.history,
                file,
                indent=4,
                ensure_ascii=False
            )



    # ========================================================
    # ANALYZE EXPERIENCE MEMORY
    # ========================================================


    def analyze(self):


        memory = runtime_memory.status()


        total = memory.get(
            "total_executions",
            0
        )


        successful = memory.get(
            "successful",
            0
        )


        failed = memory.get(
            "failed",
            0
        )



        success_rate = 0


        if total > 0:

            success_rate = round(
                (successful / total) * 100,
                2
            )



        recommendation = (
            self.generate_recommendation(
                success_rate
            )
        )


        action = (
            self.generate_action(
                success_rate
            )
        )



        analysis = {


            "timestamp":
                datetime.now().isoformat(),


            "total_executions":
                total,


            "successful":
                successful,


            "failed":
                failed,


            "success_rate":
                success_rate,


            "recommendation":
                recommendation,


            "action":
                action

        }



        self.last_analysis = analysis



        self.history.append(
            analysis
        )


        self.save_history()



        return analysis



    # ========================================================
    # RECOMMENDATION ENGINE
    # ========================================================


    def generate_recommendation(
        self,
        success_rate
    ):


        if success_rate >= 90:


            return (
                "SYSTEM PERFORMANCE OPTIMAL. "
                "KEEP CURRENT MODEL STRATEGY."
            )


        elif success_rate >= 70:


            return (
                "PERFORMANCE ACCEPTABLE. "
                "CONTINUE LEARNING."
            )


        else:


            return (
                "PERFORMANCE LOW. "
                "RETRAIN MODEL SELECTION STRATEGY."
            )



    # ========================================================
    # AUTONOMOUS ACTION ENGINE
    # ========================================================


    def generate_action(
        self,
        success_rate
    ):


        if success_rate >= 90:

            return (
                "KEEP_STRATEGY"
            )


        elif success_rate >= 70:

            return (
                "MONITOR_STRATEGY"
            )


        else:

            return (
                "OPTIMIZE_ROUTER"
            )



    # ========================================================
    # STATUS
    # ========================================================


    def status(self):


        return {


            "module":
                "SELF_LEARNING_LOOP",


            "loaded":
                True,


            "history_entries":
                len(self.history),


            "last_analysis":
                self.last_analysis

        }



# ============================================================
# GLOBAL INSTANCE
# ============================================================


self_learning_loop = SelfLearningLoop()
