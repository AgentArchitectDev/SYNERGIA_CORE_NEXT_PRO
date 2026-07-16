class DecisionEngine:

    """
    Motor de decisión cognitiva.
    """

    def decide(self, evaluation):

        if evaluation["confidence"] > 0:

            return {

                "action":
                    "execute",

                "priority":
                    "normal"

            }


        return {

            "action":
                "wait",

            "priority":
                "low"

        }



decision_engine = DecisionEngine()
