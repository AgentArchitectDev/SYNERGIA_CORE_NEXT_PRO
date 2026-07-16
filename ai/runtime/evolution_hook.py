"""
============================================================
SYNERGIA RUNTIME EVOLUTION HOOK
Auto Agent Evolution Trigger System
============================================================
"""

from ai.agents.agent_evolver import agent_evolver
from ai.runtime.event_bus import event_bus


class EvolutionHook:

    def __init__(self):

        self.last_cycle = None

    # -------------------------------------------------
    # MAIN EVOLUTION CYCLE
    # -------------------------------------------------

    def run_cycle(self):

        evolved = agent_evolver.evaluate_and_evolve()

        self.last_cycle = evolved

        event_bus.emit(
            "agent_evolution_cycle",
            {
                "result": evolved,
                "status": "completed"
            }
        )

        return {
            "status": "completed",
            "evolved": evolved
        }

    # -------------------------------------------------

    def get_last_cycle(self):

        return self.last_cycle


evolution_hook = EvolutionHook()
