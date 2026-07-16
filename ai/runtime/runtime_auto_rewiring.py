from ai.core.router import router
from ai.agents.agent_evolution_layer import agent_evolution_layer


class RuntimeAutoRewiring:
    """
    SYNERGIA RUNTIME AUTO REWIRING
    ------------------------------
    - Ajusta rutas según performance
    - Reasigna prioridades de agentes
    """

    def __init__(self):from ai.core.router import router
from ai.agents.agent_evolution_layer import agent_evolution_layer


class RuntimeAutoRewiring:
    """
    SYNERGIA RUNTIME AUTO REWIRING
    ------------------------------
    - Ajusta rutas según performance
    - Reasigna prioridades de agentes
    """

    def __init__(self):
        self.routing_weights = {}

    # -----------------------------
    # REWIRE LOGIC
    # -----------------------------

    def rewire(self):

        stats = agent_evolution_layer.stats

        if not stats:
            return {"status": "no_data"}

        # recalcular pesos
        for agent, data in stats.items():
            self.routing_weights[agent] = data["score"]

        return {
            "status": "rewired",
            "weights": self.routing_weights
        }

    # -----------------------------
    # GET BEST PATH
    # -----------------------------

    def best_path(self):

        if not self.routing_weights:
            return None

        return max(self.routing_weights.items(), key=lambda x: x[1])[0]

    # -----------------------------
    # STATUS
    # -----------------------------

    def status(self):

        return {
            "weights": self.routing_weights,
            "best": self.best_path()
        }


# singleton
runtime_auto_rewiring = RuntimeAutoRewiring()
        self.routing_weights = {}

    # -----------------------------
    # REWIRE LOGIC
    # -----------------------------

    def rewire(self):

        stats = agent_evolution_layer.stats

        if not stats:
            return {"status": "no_data"}

        # recalcular pesos
        for agent, data in stats.items():
            self.routing_weights[agent] = data["score"]

        return {
            "status": "rewired",
            "weights": self.routing_weights
        }

    # -----------------------------
    # GET BEST PATH
    # -----------------------------

    def best_path(self):

        if not self.routing_weights:
            return None

        return max(self.routing_weights.items(), key=lambda x: x[1])[0]

    # -----------------------------
    # STATUS
    # -----------------------------

    def status(self):

        return {
            "weights": self.routing_weights,
            "best": self.best_path()
        }


# singleton
runtime_auto_rewiring = RuntimeAutoRewiring()
