import ollama


class OllamaProvider:
    """
    SYNERGIA CORE NEXT PRO
    Provider simple para generación sin memoria compleja aún
    """

    def __init__(self):
        print("[OLLAMA PROVIDER LOADED]")

    # =====================================================
    # SIMPLE CHAT
    # =====================================================
    def generate(self, model_name, prompt):

        try:
            response = ollama.chat(
                model=model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            return response["message"]["content"]

        except Exception as e:
            print("[OLLAMA ERROR]", e)
            return None

    # =====================================================
    # STREAM CHAT (CLI)
    # =====================================================
    def generate_stream(self, model_name, prompt):

        try:
            stream = ollama.chat(
                model=model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                stream=True
            )

            full = ""

            for chunk in stream:
                token = chunk["message"]["content"]
                print(token, end="", flush=True)
                full += token

            print()
            return full

        except Exception as e:
            print("[OLLAMA STREAM ERROR]", e)
            return None
