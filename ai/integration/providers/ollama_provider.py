import ollama
import time


from ai.runtime.execution_history import (
    execution_history
)


from ai.core_system.brain.model_ranker import (
    model_ranker
)


# =========================================================
# OLLAMA PROVIDER
# STAGE 6.3.6
# RUNTIME METRICS + MODEL RANKER V2
# =========================================================


print("[OLLAMA PROVIDER LOADED]")


class OllamaProvider:


    # =====================================================
    # GENERATE
    # =====================================================

    def generate(
        self,
        prompt,
        model="llama3.2:3b"
    ):


        start_time = time.time()


        try:


            print("\n[OLLAMA CALL]")
            print(f"MODEL: {model}")



            response = ollama.chat(

                model=model,

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]

            )



            duration = round(

                time.time() - start_time,

                2

            )


            print(

                f"[OLLAMA OK] time={duration}s"

            )



            content = response.get(

                "message",

                {}

            ).get(

                "content",

                ""

            )



            if not content:


                execution_history.register(

                    task="OLLAMA_GENERATE",

                    node="MAQ2",

                    model=model,

                    result="empty_response"

                )


                model_ranker.register_execution(

                    model=model,

                    duration=duration,

                    success=False

                )


                return "[OLLAMA ERROR] empty response"



            # =================================================
            # EXECUTION HISTORY
            # =================================================


            execution_history.register(

                task="OLLAMA_GENERATE",

                node="MAQ2",

                model=model,

                result=f"completed_{duration}s"

            )



            # =================================================
            # MODEL RANKER V2
            # =================================================


            ranking = model_ranker.register_execution(

                model=model,

                duration=duration,

                success=True

            )


            print()

            print(
                "[MODEL RANK UPDATED]"
            )

            print(
                ranking
            )



            return content




        except Exception as e:



            duration = round(

                time.time() - start_time,

                2

            )


            print("\n[OLLAMA ERROR]")
            print(str(e))



            execution_history.register(

                task="OLLAMA_GENERATE",

                node="MAQ2",

                model=model,

                result=f"failed_{duration}s"

            )


            model_ranker.register_execution(

                model=model,

                duration=duration,

                success=False

            )



            return f"[OLLAMA FAIL] {str(e)}"



    # =====================================================
    # SIMPLE GENERATE
    # =====================================================

    def simple(
        self,
        prompt
    ):


        return self.generate(

            prompt

        )

