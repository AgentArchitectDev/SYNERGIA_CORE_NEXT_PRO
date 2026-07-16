"""
============================================================
SYNERGIA MULTI MODEL ENGINE
Ejecución real vía Ollama con fallback
============================================================
"""

import subprocess

from ai.router.model_router import model_router
from ai.router.fallback_models import FALLBACK_MODELS


class MultiModelEngine:

    def __init__(self):
        self.last_model = None

    # -------------------------------------------------

    def run(self, task: str, input_text: str):

        model = model_router.select(task)
        self.last_model = model

        result = self._call_model(model, input_text)

        # fallback automático si falla
        if result.get("status") == "error":

            for fb in FALLBACK_MODELS:

                result = self._call_model(fb, input_text)

                if result.get("status") == "executed":
                    break

        return result

    # -------------------------------------------------

    def _call_model(self, model: str, input_text: str):

        try:
            proc = subprocess.run(
                ["ollama", "run", model, input_text],
                capture_output=True,
                text=True,
                timeout=60
            )

            return {
                "model": model,
                "status": "executed",
                "output": proc.stdout.strip()
            }

        except Exception as e:

            return {
                "model": model,
                "status": "error",
                "error": str(e)
            }


multi_model_engine = MultiModelEngine()
