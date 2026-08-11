# ============================================================
# SYNERGIA OS
#
# SELF LEARNING FEEDBACK ENGINE
#
# STAGE 6.3.15.7.10.3
#
# RESPONSIBILITY:
#
# Convert self learning analysis into
# autonomous optimization feedback.
#
# ============================================================

from datetime import datetime

from ai.business.self_learning_loop import (
    self_learning_loop
)

print("[SELF LEARNING FEEDBACK LOADED]")


class SelfLearningFeedback:


    def __init__(self):

        self.last_feedback = None

        print(
            "[SELF LEARNING FEEDBACK ENGINE READY]"
        )


    # ========================================================
    # GENERATE FEEDBACK
    # ========================================================

    def generate(self):


        analysis = (
            self_learning_loop.analyze()
        )


        feedback = {


            "timestamp":
                datetime.now().isoformat(),


            "source":
                "SELF_LEARNING_LOOP",


            "success_rate":
                analysis.get(
                    "success_rate",
                    0
                ),


            "recommendation":
                analysis.get(
                    "recommendation",
                    ""
                ),


            "action":
                analysis.get(
                    "action",
                    "KEEP_STRATEGY"
                ),


            "router_feedback":
                self.generate_router_feedback(
                    analysis
                )

        }


        self.last_feedback = feedback


        return feedback



    # ========================================================
    # ROUTER KNOWLEDGE
    # ========================================================

    def generate_router_feedback(
        self,
        analysis
    ):


        success_rate = analysis.get(
            "success_rate",
            0
        )


        if success_rate >= 90:


            return {

                "mode":
                    "OPTIMAL",


                "confidence":
                    round(
                        success_rate / 100,
                        2
                    ),


                "decision":
                    "KEEP_CURRENT_MODEL_STRATEGY"

            }


        else:


            return {

                "mode":
                    "LEARNING",


                "confidence":
                    round(
                        success_rate / 100,
                        2
                    ),


                "decision":
                    "REVIEW_MODEL_SELECTION"

            }



    # ========================================================
    # STATUS
    # ========================================================

    def status(self):


        return {


            "module":
                "SELF_LEARNING_FEEDBACK",


            "loaded":
                True,


            "last_feedback":
                self.last_feedback

        }



# ============================================================
# GLOBAL INSTANCE
# ============================================================

self_learning_feedback = (
    SelfLearningFeedback()
)
