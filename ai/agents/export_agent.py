import time
import os
from ai.agents.base_agent import BaseAgent


class ExportAgent(BaseAgent):

    name = "export"

    def run(self, input_text: str):

        os.makedirs("exports", exist_ok=True)

        filename = f"export_{int(time.time())}.txt"
        path = os.path.join("exports", filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(input_text)

        return {
            "file": path
        }
