import requests


OLLAMA_URL = "http://localhost:11434/api/generate"


def generate(
    model,
    prompt,
    system=""
):

    payload = {
        "model": model,
        "prompt": prompt,
        "system": system,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    return response.json()["response"]
