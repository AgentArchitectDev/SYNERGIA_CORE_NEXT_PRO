# ============================================
# SYNERGIA AGENT DEBATE ENGINE
# ============================================


class AgentDebateEngine:


    # ========================================
    # CREATE OPINIONS
    # ========================================

    def generate_opinions(self, task):

        opinions = {

            "business":

                "Necesitamos monetización SaaS rápida y escalable.",

            "dev":

                "La mejor arquitectura sería FastAPI + PostgreSQL + Docker.",

            "cms":

                "La interfaz debe ser minimalista y simple.",

            "social":

                "Necesitamos funnels automáticos y marketing IA."
        }

        return opinions


    # ========================================
    # ANALYZE OPINIONS
    # ========================================

    def analyze_opinions(self, opinions):

        print("\n==============================")
        print(" AGENT DEBATE ENGINE")
        print("==============================\n")

        for agent, opinion in opinions.items():

            print(f"🤖 {agent.upper()}:\n")

            print(f"{opinion}\n")

        print("------------------------------")

        print("\n🧠 FINAL DECISION:\n")

        print(
            "Sistema validado para arquitectura SaaS IA."
        )

        print("\n==============================")
        print(" DEBATE COMPLETE")
        print("==============================\n")


# ============================================
# TEST
# ============================================

if __name__ == "__main__":

    engine = AgentDebateEngine()

    task = """
    Crear SaaS IA para automatización
    """

    opinions = engine.generate_opinions(task)

    engine.analyze_opinions(opinions)
