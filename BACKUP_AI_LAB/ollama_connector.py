import requests
import json


class OllamaConnector:

    def __init__(self):

        self.url = "http://localhost:11434/api/generate"

    def generate_stream(self, model, prompt):

        payload = {
            "model": model,
            "prompt": prompt,
            "stream": True
        }

        try:

            response = requests.post(
                self.url,
                json=payload,
                stream=True
            )

            for line in response.iter_lines():

                if line:

                    data = json.loads(line)

                    token = data.get("response", "")

                    yield token

        except Exception as e:

            yield f"ERROR: {e}"
