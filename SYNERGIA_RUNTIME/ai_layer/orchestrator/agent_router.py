
class AgentRouter:

    def route(self, category):

        mapping = {
            "business": ["business"],
            "dev": ["dev"],
            "cms": ["cms"],
            "social": ["social"]
        }

        return mapping.get(category, ["business"])
