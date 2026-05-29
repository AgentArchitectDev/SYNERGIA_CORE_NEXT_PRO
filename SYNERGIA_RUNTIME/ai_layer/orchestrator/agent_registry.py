
# =========================================================
# SYNERGIA AGENT REGISTRY
# =========================================================

class AgentRegistry:

    def __init__(self):

        self.agents = {
            "business": "Business AI Strategist",
            "cms": "CMS & UX Architect",
            "dev": "Backend & System Architect",
            "social": "Marketing & Social AI"
        }

    def get_agent(self, name):

        return self.agents.get(name, "Unknown Agent")
