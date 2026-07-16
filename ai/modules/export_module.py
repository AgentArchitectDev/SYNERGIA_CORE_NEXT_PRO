import os
from datetime import datetime


class ExportModule:

    def __init__(self):

        self.base_path = "exports"

        os.makedirs(self.base_path, exist_ok=True)

    def execute(self, input_text: str):

        filename = f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        path = os.path.join(self.base_path, filename)

        with open(path, "w") as f:
            f.write(input_text)

        return {
            "status": "executed",
            "module": "export",
            "file": path
        }


export_module = ExportModule()
