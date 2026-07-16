import time
from ai.core.event_bus import event_bus


class ContextManager:
    """
    SYNERGIA CONTEXT MANAGER
    ------------------------
    - Mantiene contexto vivo de ejecución
    - Une memoria + runtime + eventos
    """

    def __init__(self):
        self.context = {
            "sessions": [],
            "facts": [],
            "working_memory": []
        }

    def add_fact(self, key: str, value: str):

        fact = {
            "key": key,
            "value": value,
            "timestamp": time.time()
        }

        self.context["facts"].append(fact)

        event_bus.emit("context_fact_added", fact)

        return fact

    def add_working_memory(self, item: dict):

        item["timestamp"] = time.time()
        self.context["working_memory"].append(item)

        return item

    def get_context(self):
        return self.context

    def clear_working_memory(self):
        self.context["working_memory"] = []

        event_bus.emit("context_cleared", {})

        return {"status": "cleared"}


# singleton
context_manager = ContextManager()
