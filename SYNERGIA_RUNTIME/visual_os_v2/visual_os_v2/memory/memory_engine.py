import os
import json
from datetime import datetime


# =====================================================
# MEMORY ENGINE
# =====================================================

class MemoryEngine:

    def __init__(self):

        self.memory_path = "memory/experiences"

        os.makedirs(self.memory_path, exist_ok=True)

    # =================================================
    # SAVE EXPERIENCE
    # =================================================

    def save_experience(self, data):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        safe_task = (
            data["task"]
            .replace(" ", "_")
            .replace("/", "_")
            .lower()
        )

        filename = f"{safe_task}_{timestamp}.json"

        filepath = os.path.join(
            self.memory_path,
            filename
        )

        memory_data = {
            "task": data["task"],
            "mode": data["mode"],
            "nodes": data["nodes"],
            "graph": data["graph"],
            "timestamp": timestamp
        }

        with open(filepath, "w") as f:

            json.dump(
                memory_data,
                f,
                indent=4
            )

        print(f"\n💾 MEMORY SAVED:")
        print(filepath)

        return filepath

    # =================================================
    # LOAD EXPERIENCES
    # =================================================

    def load_experiences(self):

        experiences = []

        for file in os.listdir(self.memory_path):

            if file.endswith(".json"):

                filepath = os.path.join(
                    self.memory_path,
                    file
                )

                with open(filepath, "r") as f:

                    data = json.load(f)

                    experiences.append(data)

        return experiences
