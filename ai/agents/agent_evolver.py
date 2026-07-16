"""
============================================================
SYNERGIA AGENT EVOLUTION ENGINE
Replaces low performance agents automatically
============================================================
"""

from ai.agents.agent_metrics import agent_metrics
from ai.agents.agent_registry import agent_registry


class AgentEvolver:

    def __init__(self):

        self.threshold = 0.5  # mínimo aceptable

    # -------------------------------------------------

    def evaluate_and_evolve(self):

        scores = agent_metrics.all_scores()

        evolved = []

        for agent_name, score in scores.items():

            if score < self.threshold:

                # marcar como candidato a reemplazo
                agent_registry.remove(agent_name)

                evolved.append({
                    "agent": agent_name,
                    "action": "removed",
                    "score": score
                })

            else:

                evolved.append({
                    "agent": agent_name,
                    "action": "kept",
                    "score": score
                })

        return evolved


agent_evolver = AgentEvolver()
