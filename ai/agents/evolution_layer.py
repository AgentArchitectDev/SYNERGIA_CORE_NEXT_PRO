import time
from ai.core.event_bus import event_bus


class AgentEvolutionLayer:
    """
    SYNERGIA AGENT EVOLUTION LAYER v1.0
    -----------------------------------
    - Observa comportamiento de agentes
    - Ajusta prioridad y estado
    - Marca agentes como activos, degradados o mejorados
    - Base para auto-optimización futura
    """

    def __init__(self):
        self.agents = {}
        self.history = []

    # ---------------------------------------------------------
    # REGISTRO DE AGENTES
    # ---------------------------------------------------------
    def register(self, name: str, agent):

        self.agents[name] = {
            "agent": agent,
            "score": 1.0,
            "executions": 0,
            "failures": 0,
            "status": "active"
        }

        event_bus.emit("agent_registered", {"agent": name})

    # ---------------------------------------------------------
    # TRACK DE EJECUCIÓN
    # ---------------------------------------------------------
    def track_execution(self, name: str, success: bool):

        if name not in self.agents:
            return

        data = self.agents[name]

        data["executions"] += 1

        if success:
            data["score"] += 0.05
        else:
            data["failures"] += 1
            data["score"] -= 0.1

        # clamp score
        data["score"] = max(0.1, min(data["score"], 2.0))

        # update status
        if data["score"] < 0.5:
            data["status"] = "degraded"
        elif data["score"] > 1.5:
            data["status"] = "enhanced"
        else:
            data["status"] = "stable"

        event_bus.emit("agent_updated", {
            "agent": name,
            "score": data["score"],
            "status": data["status"]
        })

    # ---------------------------------------------------------
    # SELECCIÓN DE AGENTE ÓPTIMO
    # ---------------------------------------------------------
    def select_best(self, capability: str = None):

        if not self.agents:
            return None

        sorted_agents = sorted(
            self.agents.items(),
            key=lambda x: x[1]["score"],
            reverse=True
        )

        best = sorted_agents[0]

        return {
            "name": best[0],
            "agent": best[1]["agent"],
            "score": best[1]["score"]
        }

    # ---------------------------------------------------------
    # ESTADO GLOBAL
    # ---------------------------------------------------------
    def status(self):

        return {
            "total_agents": len(self.agents),
            "agents": self.agents
        }

    # ---------------------------------------------------------
    # EVOLUTION STEP (AUTO OPTIMIZATION LOOP)
    # ---------------------------------------------------------
    def evolve(self):

        for name, data in self.agents.items():

            if data["failures"] > data["executions"] * 0.6:
                data["status"] = "candidate_remove"

            if data["executions"] > 10 and data["score"] > 1.3:
                data["status"] = "core_agent"

        event_bus.emit("agent_evolution_cycle", {
            "timestamp": time.time()
        })


# singleton global
agent_evolution_layer = AgentEvolutionLayer()
