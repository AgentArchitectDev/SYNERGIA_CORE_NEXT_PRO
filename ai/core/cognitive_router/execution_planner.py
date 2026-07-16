class ExecutionPlanner:

    """
    Construye el plan definitivo.
    """

    def build(self, intents):

        return [

            item["module"]

            for item in intents

        ]


execution_planner = ExecutionPlanner()
