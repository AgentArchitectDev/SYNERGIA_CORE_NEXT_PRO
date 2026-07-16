import time
from collections import defaultdict


class AgentEvolutionLayer:
    """
    SYNERGIA Agent Evolution Layer

    Registra la evolución de cada agente.
    """

    def __init__(self):

        self.stats = defaultdict(lambda: {
            "executions": 0,
            "success": 0,
            "failures": 0,
            "latency": [],
            "score": 0.50,
            "last_execution": None
        })

    # --------------------------------------------------

    def record_execution(
        self,
        agent_name: str,
        success: bool = True,
        latency: float = 0.0
    ):

        agent = self.stats[agent_name]

        agent["executions"] += 1

        if success:
            agent["success"] += 1
        else:
            agent["failures"] += 1

        agent["latency"].append(latency)
        agent["last_execution"] = time.time()

        self.compute_score(agent_name)

    # --------------------------------------------------

    def compute_score(self, agent_name):

        agent = self.stats[agent_name]

        executions = agent["executions"]

        if executions == 0:
            agent["score"] = 0.50
            return 0.50

        success_rate = agent["success"] / executions

        if len(agent["latency"]) == 0:
            avg_latency = 0
        else:
            avg_latency = sum(agent["latency"]) / len(agent["latency"])

        latency_bonus = max(0.0, 1 - avg_latency)

        score = success_rate * 0.8 + latency_bonus * 0.2

        score = round(score, 3)

        agent["score"] = score

        return score

    # --------------------------------------------------

    def get_agent(self, agent_name):

        return self.stats.get(agent_name)

    # --------------------------------------------------

    def ranking(self):

        ranking = []

        for name, data in self.stats.items():

            ranking.append({
                "agent": name,
                "score": data["score"]
            })

        ranking.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return ranking

    # --------------------------------------------------

    def status(self):

        return {
            "agents": len(self.stats),
            "ranking": self.ranking()
        }


agent_evolution_layer = AgentEvolutionLayer()
