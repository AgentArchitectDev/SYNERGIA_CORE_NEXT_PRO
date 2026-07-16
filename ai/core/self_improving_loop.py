import time

from ai.agents.agent_evolution_layer import agent_evolution_layer
from ai.core.router import router


class SelfImprovingLoop:
    """
    SYNERGIA SELF IMPROVING LOOP
    ----------------------------
    - Analiza performance de agentes
    - Ajusta routing dinámico
    - Base de auto-optimización del sistema
    """

    def __init__(self):
        self.last_optimization = None
        self.optimization_history = []

    # -----------------------------
    # ANALYSIS ENGINE
    # -----------------------------

    def analyze(self):

        stats = agent_evolution_layer.stats

        if not stats:
            return {"status": "no_data"}

        best = max(stats.items(), key=lambda x: x[1]["score"])
        worst = min(stats.items(), key=lambda x: x[1]["score"])

        return {
            "best_agent": best[0],
            "worst_agent": worst[0],
            "scores": {k: v["score"] for k, v in stats.items()}
        }

    # -----------------------------
    # OPTIMIZATION STEP
    # -----------------------------

    def optimize(self):

        analysis = self.analyze()

        if analysis.get("status") == "no_data":
            return analysis

        # ajuste simple del router (heurístico)
        best_agent = analysis["best_agent"]

        # guardamos optimización
        self.last_optimization = {
            "best": best_agent,
            "timestamp": time.time()
        }

        self.optimization_history.append(self.last_optimization)

        return self.last_optimization

    # -----------------------------
    # STATUS
    # -----------------------------

    def status(self):

        return {
            "last": self.last_optimization,
            "history": len(self.optimization_history)
        }


# singleton
self_improving_loop = SelfImprovingLoop()
