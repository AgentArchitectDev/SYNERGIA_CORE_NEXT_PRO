
# =========================================================
# SYNERGIA DECISION ENGINE
# =========================================================

class DecisionEngine:

    def __init__(self):

        self.available_agents = [
            "business",
            "cms",
            "dev",
            "social"
        ]

    def analyze(self, task):

        task = task.lower()

        selected_agents = []

        if "saas" in task or "business" in task:
            selected_agents.append("business")

        if "web" in task or "landing" in task:
            selected_agents.append("cms")

        if "backend" in task or "api" in task or "system" in task:
            selected_agents.append("dev")

        if "marketing" in task or "social" in task:
            selected_agents.append("social")

        if not selected_agents:
            selected_agents = self.available_agents

        return selected_agents
