"""
====================================================
SYNERGIA EVOLUTION BRIDGE V1
====================================================

Puente entre:

Runtime Manager
        |
        |
Evolution Engine
        |
        |
Agent Evolution Layer

====================================================
"""


from ai.evolution.evolution_core import runtime_evolution


try:
    from ai.agents.agent_evolution_layer import (
        agent_evolution_layer
    )
except Exception:
    agent_evolution_layer = None



class EvolutionBridge:


    def __init__(self):

        self.events = []



    # ---------------------------------------------

    def record_execution(
            self,
            agent,
            success=True,
            latency=0
    ):


        event = {

            "agent":
                agent,

            "success":
                success,

            "latency":
                latency

        }


        self.events.append(event)


        # Evolution Engine

        runtime_evolution.analyze(
            event
        )


        # Agent Evolution Layer

        if agent_evolution_layer:

            agent_evolution_layer.record_execution(
                agent,
                success,
                latency
            )


        return event



    # ---------------------------------------------

    def status(self):

        return {

            "events":
                len(self.events)

        }



evolution_bridge = EvolutionBridge()
