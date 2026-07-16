"""
============================================================
SYNERGIA OMEGA
AGENT REGISTRY
ACEA Architecture
============================================================
"""

from __future__ import annotations

import time

# ============================================================
# Agent Registry
# ============================================================


class AgentRegistry:

    def __init__(self):

        self._agents = {}

    # --------------------------------------------------------

    def register(
        self,
        name,
        role,
        provider="local",
        node="MAQ1",
        enabled=True
    ):

        self._agents[name] = {

            "name": name,

            "role": role,

            "provider": provider,

            "node": node,

            "enabled": enabled,

            "created": time.time()

        }

        return {

            "status": "registered",

            "agent": name

        }

    # --------------------------------------------------------

    def unregister(
        self,
        name
    ):

        if name not in self._agents:

            return {

                "status": "not_found"

            }

        del self._agents[name]

        return {

            "status": "removed",

            "agent": name

        }

    # --------------------------------------------------------

    def exists(
        self,
        name
    ):

        return name in self._agents

    # --------------------------------------------------------

    def get(
        self,
        name
    ):

        return self._agents.get(name)

    # --------------------------------------------------------

    def list_agents(self):

        return list(

            self._agents.keys()

        )

    # --------------------------------------------------------

    def enable(
        self,
        name
    ):

        if name in self._agents:

            self._agents[name]["enabled"] = True

        return {

            "status": "enabled",

            "agent": name

        }

    # --------------------------------------------------------

    def disable(
        self,
        name
    ):

        if name in self._agents:

            self._agents[name]["enabled"] = False

        return {

            "status": "disabled",

            "agent": name

        }

    # --------------------------------------------------------

    def status(self):

        return {

            "component": "OMEGA Agent Registry",

            "agents": len(

                self._agents

            ),

            "registered":

                self.list_agents()

        }


# ============================================================
# Singleton
# ============================================================

agent_registry = AgentRegistry()
