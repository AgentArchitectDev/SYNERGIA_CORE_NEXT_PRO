import ollama


# =====================================================
# OLLAMA AGENT ENGINE
# =====================================================

class OllamaRuntime:

    def __init__(self):

        self.models = {

            "business": "llama3",

            "dev": "qwen2.5-coder",

            "social_media": "mistral",

            "cms": "phi3"
        }

    # =================================================
    # EXECUTE AGENT
    # =================================================

    def run_agent(self, agent, task):

        model = self.models.get(
            agent,
            "llama3"
        )

        prompt = f"""

        You are the {agent} agent inside SYNERGIA OS.

        Task:

        {task}

        Respond shortly.
        """

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

            return {

                "agent": agent,

                "model": model,

                "response":
                    response["message"]["content"]
            }

        except Exception as e:

            return {

                "agent": agent,

                "model": model,

                "response":
                    f"ERROR: {str(e)}"
            }
