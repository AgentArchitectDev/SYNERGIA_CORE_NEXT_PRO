"""
SYNERGIA V3 - Model Manager (OLLAMA INTEGRATION)
Conecta SYNERGIA con modelos locales reales
"""

import subprocess


class ModelManager:

    def __init__(self):

        self.models = self._load_models()

    # -----------------------------

    def _load_models(self):

        try:
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                text=True
            )

            return result.stdout

        except Exception as e:

            return f"ERROR: {e}"

    # -----------------------------

    def refresh(self):

        self.models = self._load_models()

        return self.models

    # -----------------------------

    def list_raw(self):

        return self.models

    # -----------------------------

    def list_parsed(self):

        lines = self.models.split("\n")

        parsed = []

        for line in lines:

            if line and "NAME" not in line:

                parts = line.split()

                if len(parts) >= 2:

                    parsed.append({
                        "name": parts[0],
                        "id": parts[1] if len(parts) > 1 else None
                    })

        return parsed


model_manager = ModelManager()
