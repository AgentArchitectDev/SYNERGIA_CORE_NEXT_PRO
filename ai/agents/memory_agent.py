from ai.agents.base_agent import BaseAgent
from ai.router.multi_model_engine import multi_model_engine


class MemoryAgent(BaseAgent):

    def __init__(self, memory_runtime):
        super().__init__("memory")
        self.memory = memory_runtime

    def run(self, input_text: str, context=None):

        result = multi_model_engine.run("memory", input_text)

        entry = {
            "text": input_text,
            "model": result["model"]
        }

        self.memory.append(entry)

        return {
            "agent": self.name,
            "stored": entry
        }
