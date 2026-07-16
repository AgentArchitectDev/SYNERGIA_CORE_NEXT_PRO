import subprocess
import json


class OllamaModule:

    name = "ollama"

    def execute(self, input_text: str, context=None):

        # usa modelo por defecto liviano
        model = "llama3.2:3b"

        try:
            result = subprocess.run(
                ["ollama", "run", model, input_text],
                capture_output=True,
                text=True
            )

            return {
                "model": model,
                "output": result.stdout
            }

        except Exception as e:
            return {"error": str(e)}
