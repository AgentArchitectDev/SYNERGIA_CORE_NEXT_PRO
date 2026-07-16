from datetime import datetime


class MemoryModule:

    def __init__(self):
        self.memory = []

    def execute(self, input_text: str):

        entry = {
            "text": input_text,
            "timestamp": datetime.now().isoformat()
        }

        self.memory.append(entry)

        return {
            "status": "executed",
            "module": "memory",
            "stored": entry,
            "size": len(self.memory)
        }


memory_module = MemoryModule()
