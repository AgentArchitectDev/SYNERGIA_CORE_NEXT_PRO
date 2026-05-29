from agent_core import AgentCore


class AgentCollab:

    def __init__(self):

        self.agents = AgentCore()

    # =========================
    # PROJECT GENERATOR
    # =========================
    def run_project(self, idea):

        print("\n🤝 SYNERGIA COLLAB v1")
        print("Project:", idea)

        # =========================
        # 1. BUSINESS ANALYSIS
        # =========================
        business = self.agents.run(
            "business",
            f"Analiza esta idea y crea modelo SaaS completo: {idea}"
        )

        # =========================
        # 2. CMS DESIGN
        # =========================
        cms = self.agents.run(
            "cms",
            f"Crea la landing page basada en este negocio: {business}"
        )

        # =========================
        # 3. DEV IMPLEMENTATION
        # =========================
        dev = self.agents.run(
            "dev",
            f"Genera el backend o estructura técnica: {idea}"
        )

        # =========================
        # 4. SOCIAL STRATEGY
        # =========================
        social = self.agents.run(
            "social",
            f"Crea campaña de marketing para: {idea}"
        )

        # =========================
        # RESULT MERGE
        # =========================
        result = {
            "idea": idea,
            "business": business,
            "cms": cms,
            "dev": dev,
            "social": social
        }

        return result
