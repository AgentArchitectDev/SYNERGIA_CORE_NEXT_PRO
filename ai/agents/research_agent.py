import time
from ai.agents.base_agent import BaseAgent


class ResearchAgent(BaseAgent):

    name = "research"

    def run(self, input_text: str):

        time.sleep(0.01)

        return {
            "query": input_text,
            "result": f"Simulated research for: {input_text}"
        }
