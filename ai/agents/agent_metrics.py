"""
============================================================
SYNERGIA AGENT METRICS
Tracks performance of agents over time
============================================================
"""

import time


class AgentMetrics:

    def __init__(self):

        self.metrics = {}

    # -------------------------------------------------

    def record(self, agent_name: str, success: bool, latency: float = 0):

        if agent_name not in self.metrics:

            self.metrics[agent_name] = {
                "runs": 0,
                "success": 0,
                "fail": 0,
                "avg_latency": 0,
                "last_seen": None
            }

        m = self.metrics[agent_name]

        m["runs"] += 1
        m["last_seen"] = time.time()

        if success:
            m["success"] += 1
        else:
            m["fail"] += 1

        # promedio simple
        m["avg_latency"] = (
            (m["avg_latency"] * (m["runs"] - 1) + latency)
            / m["runs"]
        )

    # -------------------------------------------------

    def score(self, agent_name: str):

        m = self.metrics.get(agent_name)

        if not m or m["runs"] == 0:
            return 0

        success_rate = m["success"] / m["runs"]

        # penaliza latencia
        latency_penalty = min(m["avg_latency"] / 10, 1)

        return success_rate * (1 - latency_penalty)

    # -------------------------------------------------

    def all_scores(self):

        return {
            name: self.score(name)
            for name in self.metrics
        }


agent_metrics = AgentMetrics()
