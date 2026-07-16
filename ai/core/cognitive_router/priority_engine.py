class PriorityEngine:

    """
    Ordena agentes.
    """

    def sort(self, intents):

        return sorted(

            intents,

            key=lambda x: x["priority"],

            reverse=True

        )


priority_engine = PriorityEngine()
