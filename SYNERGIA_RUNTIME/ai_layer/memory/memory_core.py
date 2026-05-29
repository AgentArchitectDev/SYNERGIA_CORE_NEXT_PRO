import json
import os
from datetime import datetime

class MemoryCore:

    def __init__(self, path="synergia_memory.json"):

        self.path = path
        self.memory = self.load_memory()

    # =========================
    # LOAD MEMORY
    # =========================
    def load_memory(self):

        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                return json.load(f)

        return {
            "sessions": [],
            "agents": {},
            "global_context": []
        }

    # =========================
    # SAVE MEMORY
    # =========================
    def save_memory(self):

        with open(self.path, "w") as f:
            json.dump(self.memory, f, indent=4)

    # =========================
    # ADD EVENT
    # =========================
    def add_event(self, agent, task, output):

        event = {
            "timestamp": str(datetime.now()),
            "agent": agent,
            "task": task,
            "output": output
        }

        self.memory["sessions"].append(event)

        if agent not in self.memory["agents"]:
            self.memory["agents"][agent] = []

        self.memory["agents"][agent].append(event)

        self.save_memory()

    # =========================
    # GET CONTEXT
    # =========================
    def get_context(self, agent, limit=5):

        if agent in self.memory["agents"]:
            return self.memory["agents"][agent][-limit:]

        return []

    # =========================
    # GLOBAL MEMORY
    # =========================
    def add_global(self, text):

        self.memory["global_context"].append({
            "timestamp": str(datetime.now()),
            "text": text
        })

        self.save_memory()
