"""
SYNERGIA V3 - Registry (FIXED)
Garantiza consistencia de retorno para Kernel
"""


class Registry:

    def __init__(self):

        self.modules = {}

    # -----------------------------

    def register(self, name, instance, capabilities=None):

        self.modules[name] = {
            "instance": instance,
            "capabilities": capabilities or [],
            "status": "ONLINE",
            "version": "1.0"
        }

    # -----------------------------

    def get(self, name):

        module = self.modules.get(name)

        if module:
            return module["instance"]

        return None

    # -----------------------------

    def info(self):

        # 🔥 IMPORTANTE: SIEMPRE DICT (NO LIST)
        return {
            name: {
                "status": data["status"],
                "version": data["version"],
                "capabilities": data["capabilities"]
            }
            for name, data in self.modules.items()
        }

    # -----------------------------

    def online_modules(self):

        return list(self.modules.keys())

    # -----------------------------

    def by_capability(self, capability):

        return [
            name
            for name, data in self.modules.items()
            if capability in data.get("capabilities", [])
        ]


registry = Registry()
