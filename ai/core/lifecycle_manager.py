"""
SYNERGIA V3 - Lifecycle Manager (FINAL)
Control total del ciclo de vida de módulos
"""

import time


class LifecycleManager:

    def __init__(self):
        self.modules = {}     # name -> instance
        self.states = {}      # name -> running/stopped/failed
        self.boot_time = time.time()

    # -----------------------------

    def register(self, name, module):

        self.modules[name] = module
        self.states[name] = "stopped"

    # -----------------------------

    def start(self, name):

        if name not in self.modules:
            return {"module": name, "status": "not_found"}

        self.states[name] = "running"

        return {
            "module": name,
            "action": "start",
            "status": "ok"
        }

    # -----------------------------

    def stop(self, name):

        if name not in self.modules:
            return {"module": name, "status": "not_found"}

        self.states[name] = "stopped"

        return {
            "module": name,
            "action": "stop",
            "status": "ok"
        }

    # -----------------------------

    def restart(self, name):

        if name not in self.modules:
            return {"module": name, "status": "not_found"}

        self.states[name] = "running"

        return {
            "module": name,
            "action": "restart",
            "status": "ok",
            "timestamp": time.time()
        }

    # -----------------------------

    def status(self):

        return {
            "uptime": round(time.time() - self.boot_time, 4),
            "states": self.states,
            "modules": list(self.modules.keys())
        }


lifecycle_manager = LifecycleManager()
