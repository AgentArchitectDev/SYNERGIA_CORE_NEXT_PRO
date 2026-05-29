# =========================================================
# SYNERGIA AI ENGINE v2
# =========================================================

import ollama


# =========================================================
# AI ENGINE
# =========================================================

class AIEngine:

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        self.model = "llama3"

    # =====================================================
    # GENERATE
    # =====================================================

    def generate(
        self,
        prompt
    ):

        print(f"\n🤖 Running model: {self.model}")

        response = ollama.chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response["message"]["content"]

    # =====================================================
    # BACKWARD COMPATIBILITY
    # =====================================================

    def run(
        self,
        prompt
    ):

        return self.generate(prompt)


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    engine = AIEngine()

    response = engine.generate(
        "Hola IA"
    )

    print("\nRESPONSE:\n")

    print(response)
