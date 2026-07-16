"""
============================================================
SYNERGIA AGENT REGISTRY
============================================================
"""

from typing import Dict
from ai.agents.base_agent import BaseAgent


class AgentRegistry:

    def __init__(self):

        self.agents: Dict[str, BaseAgent] = {}

    # -------------------------------------------------

    def register(self, agent: BaseAgent):

        self.agents[agent.name] = agent

    # -------------------------------------------------

    def get(self, name: str):

        return self.agents.get(name)

    # -------------------------------------------------

    def list(self):

        return list(self.agents.keys())

    # -------------------------------------------------

    def execute(self, name: str, input_text: str, context=None):

        agent = self.get(name)

        if not agent:
            return {
                "status": "missing_agent",
                "agent": name
            }

        try:
            return agent.run(input_text, context)

        except Exception as e:

            return {
                "status": "error",
                "agent": name,
                "error": str(e)
            }


agent_registry = AgentRegistry()
