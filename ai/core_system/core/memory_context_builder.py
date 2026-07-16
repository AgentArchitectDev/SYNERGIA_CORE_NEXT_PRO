import json
import os

MEMORY_FILE = "ai/runtime_storage/memory.json"


class MemoryContextBuilder:

    def __init__(self):
        self.memory_file = MEMORY_FILE
        self._ensure()

    def _ensure(self):
        if not os.path.exists(self.memory_file):
            os.makedirs(os.path.dirname(self.memory_file), exist_ok=True)
            with open(self.memory_file, "w") as f:
                json.dump([], f)

    def build(self, user_input: str):
        memory = self._load()

        return {
            "input": user_input,
            "memory": memory[-5:]
        }

    def retrieve(self, user_input: str):
        return self._load()[-10:]

    def save(self, user_input: str):
        memory = self._load()
        memory.append(user_input)
        self._save(memory)

    def _load(self):
        with open(self.memory_file, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.memory_file, "w") as f:
            json.dump(data, f, indent=2)
