class TaskEngine:

    def execute(self, user_input, context=None):

        text = user_input.lower()

        if "calcular" in text:
            return self._calc(user_input)

        if "estado" in text:
            return {"status": "system_ok"}

        return {
            "status": "executed",
            "task": user_input,
            "analysis": "generic_task_handled"
        }

    def _calc(self, text):
        return {
            "type": "calc",
            "result": "simulación de cálculo (placeholder)"
        }
