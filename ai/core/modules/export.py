import os
import json
import time


class ExportModule:
    def __init__(self):
        self.base_path = "exports"
        os.makedirs(self.base_path, exist_ok=True)

    def run(self, input_text: str):
        filename = f"export_{int(time.time())}.txt"
        path = os.path.join(self.base_path, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(input_text)

        return {
            "status": "executed",
            "file": path
        }
