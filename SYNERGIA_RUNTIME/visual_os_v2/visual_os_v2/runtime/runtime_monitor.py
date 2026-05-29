class RuntimeMonitor:

    def __init__(self):

        self.active_agents = []
        self.active_models = [
            "llama3",
            "qwen2.5-coder",
            "deepseek-coder"
        ]

    def register_agents(self, nodes):

        self.active_agents = nodes

    def get_status(self):

        agents_status = {}

        for agent in self.active_agents:

            agents_status[agent] = {
                "status": "RUNNING"
            }

        return {
            "agents": agents_status,
            "models": self.active_models,
            "memory": "memory/experience_2026.json",
            "output_path": "projects/generated_project/",
            "system_status": "ONLINE"
        }
