"""
============================================================
SYNERGIA COGNITIVE OS
Context Manager
Version 4.0
============================================================
"""

from datetime import datetime


class ContextManager:
    """
    Maneja contexto global compartido entre tareas,
    módulos y sesiones del runtime.
    """

    def __init__(self):

        self.context = {}

        self.history = []

    # -------------------------------------------------

    def set(self, key, value):

        self.context[key] = value

        self.history.append({
            "action": "set",
            "key": key,
            "value": value,
            "timestamp": datetime.now().isoformat()
        })

    # -------------------------------------------------

    def get(self, key, default=None):

        return self.context.get(key, default)

    # -------------------------------------------------

    def delete(self, key):

        if key in self.context:

            del self.context[key]

            self.history.append({
                "action": "delete",
                "key": key,
                "timestamp": datetime.now().isoformat()
            })

    # -------------------------------------------------

    def clear(self):

        self.context.clear()

        self.history.append({
            "action": "clear",
            "timestamp": datetime.now().isoformat()
        })

    # -------------------------------------------------

    def dump(self):

        return {
            "context": self.context,
            "history": self.history
        }


context_manager = ContextManager()
