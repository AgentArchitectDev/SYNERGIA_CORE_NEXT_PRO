import time

from ai.runtime.runtime_manager import runtime_manager
from ai.runtime.runtime_auto_rewiring import runtime_auto_rewiring
from ai.agents.agent_autonomy_layer import agent_autonomy_layer


class CognitiveContinuousLoop:
    """
    SYNERGIA COGNITIVE CONTINUOUS LOOP
    ----------------------------------
    - Loop autónomo de mejora
    - Rewiring + adaptación continua
    - Simula "conciencia operativa"
    """

    def __init__(self):
        self.running = False
        self.iterations = 0
        self.history = []

    # -----------------------------
    # STEP LOOP
    # -----------------------------

    def step(self):

        self.iterations += 1

        # 1. rewire runtime
        rewiring = runtime_auto_rewiring.rewire()

        # 2. adaptar agentes principales
        agents = ["memory", "research", "export", "ollama"]

        adaptations = []

        for agent in agents:
            adaptation = agent_autonomy_layer.adapt(agent)
            adaptations.append(adaptation)

        snapshot = {
            "iteration": self.iterations,
            "rewiring": rewiring,
            "adaptations": adaptations,
            "timestamp": time.time()
        }

        self.history.append(snapshot)

        return snapshot

    # -----------------------------
    # RUN LOOP (manual control)
    # -----------------------------

    def run(self, steps: int = 1):

        self.running = True

        results = []

        for _ in range(steps):
            results.append(self.step())

        self.running = False

        return results

    # -----------------------------
    # STATUS
    # -----------------------------

    def status(self):

        return {
            "running": self.running,
            "iterations": self.iterations,
            "history_size": len(self.history)
        }


# singleton
cognitive_continuous_loop = CognitiveContinuousLoop()
