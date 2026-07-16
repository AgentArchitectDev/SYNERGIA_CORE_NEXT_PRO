class Evaluator:

    """
    Evalúa información recibida.
    """

    def evaluate(self, observation):

        if observation.get("input"):

            return {

                "state":
                    "active",

                "confidence":
                    0.8

            }


        return {

            "state":
                "idle",

            "confidence":
                0

        }



evaluator = Evaluator()
