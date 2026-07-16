import time
from ai.core.context_manager import context_manager
from ai.core.session import session_manager


class MemoryModule:
    """
    SYNERGIA MEMORY MODULE v2
    -------------------------
    - Memoria runtime + contexto + sesión
    """

    def __init__(self):
        self.memory = []

    def run(self, input_text: str):

        entry = {
            "text": input_text,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
        }

        # memoria local
        self.memory.append(entry)

        # contexto global
        context_manager.add_fact("memory_store", input_text)
        context_manager.add_working_memory(entry)

        # sesión
        session_manager.add_event({
            "module": "memory",
            "action": "store",
            "data": input_text
        })

        return {
            "status": "executed",
            "stored": entry,
            "size": len(self.memory)
        }

    def get_all(self):
        return self.memory

    def clear(self):
        self.memory = []
        return {"status": "cleared"}
