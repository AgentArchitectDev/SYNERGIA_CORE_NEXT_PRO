
class MultiAgentRouter:

    def route(self, task):

        task = task.lower()

        agents = []

        if "saas" in task:
            agents.extend([
                "business",
                "dev",
                "cms",
                "social"
            ])

        elif "backend" in task:
            agents.append("dev")

        elif "landing" in task:
            agents.append("cms")

        elif "marketing" in task:
            agents.append("social")

        else:
            agents.append("business")

        return agents
