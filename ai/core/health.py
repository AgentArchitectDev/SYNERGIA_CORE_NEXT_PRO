import time


class HealthSystem:
    """
    SYNERGIA HEALTH MODULE
    - controla estado de módulos
    - evalúa ejecución
    """

    def __init__(self):
        self.state = {}
        self.last_check = time.time()

    def update(self, module: str, status: str, latency=None):
        self.state[module] = {
            "status": status,
            "latency": latency,
            "timestamp": time.time()
        }

    def get(self):
        return self.state

    def summary(self):
        ok = sum(1 for m in self.state.values() if m["status"] == "executed")
        fail = sum(1 for m in self.state.values() if m["status"] != "executed")

        return {
            "ok": ok,
            "failed": fail,
            "total": len(self.state)
        }


# instancia global
health = HealthSystem()
