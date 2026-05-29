# =========================================================
# SYNERGIA OS v3
# OLLAMA RUNTIME
# =========================================================

import ollama


# =========================================================
# OLLAMA RUNTIME
# =========================================================

class OllamaRuntime:

    def __init__(self):

        print("🤖 OLLAMA RUNTIME ONLINE")

    # =====================================================
    # GENERATE
    # =====================================================

    def generate(
        self,
        model,
        prompt
    ):

        print()
        print(f"🧠 RUNNING MODEL: {model}")

        try:

            response = ollama.chat(

                model=model,

                messages=[

                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            content = response["message"]["content"]

            print("✅ RESPONSE GENERATED")

            return content

        except Exception as e:

            print()
            print("❌ OLLAMA ERROR")
            print(str(e))

            return f"Ollama Error: {str(e)}"
