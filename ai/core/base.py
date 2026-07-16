class BaseModule:

    name = "base"

    def execute(self, input_text: str, context: dict = None):
        raise NotImplementedError("Module must implement execute()")
