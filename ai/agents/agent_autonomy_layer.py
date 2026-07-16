import time

from ai.agents.agent_evolution_layer import (
    agent_evolution_layer
)


class AgentAutonomyLayer:

    """
    Autonomía de agentes.

    Modifica el comportamiento de un agente
    según su evolución.
    """

    def __init__(self):

        self.behavior_profiles = {}

        self.history = []

    # --------------------------------------------------

    def build_profile(self, agent_name):

        stats = agent_evolution_layer.get_agent(agent_name)

        if stats is None:

            profile = "default"

        else:

            score = stats["score"]

            if score >= 0.85:

                profile = "expert"

            elif score >= 0.65:

                profile = "stable"

            elif score >= 0.45:

                profile = "learning"

            else:

                profile = "recovery"

        self.behavior_profiles[agent_name] = profile

        return profile

    # --------------------------------------------------

    def adapt(self, agent_name):

        profile = self.build_profile(agent_name)

        info = {

            "agent": agent_name,

            "profile": profile,

            "timestamp": time.time()

        }

        self.history.append(info)

        return info

    # --------------------------------------------------

    def get_profile(self, agent_name):

        return self.behavior_profiles.get(
            agent_name,
            "default"
        )

    # --------------------------------------------------

    def status(self):

        return {

            "profiles": self.behavior_profiles,

            "adaptations": len(self.history)

        }


agent_autonomy_layer = AgentAutonomyLayer()
