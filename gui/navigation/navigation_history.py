"""
====================================================================
SYNERGIA OMEGA UI
Navigation History V6 Enterprise
====================================================================

Historial inteligente de navegación.

Responsabilidades

✔ Historial
✔ Recientes
✔ Favoritos
✔ Último módulo
✔ Estadísticas
✔ Base para IA

Version:
    V6 Enterprise

====================================================================
"""

import time


class NavigationHistory:

    """
    Historial del Navigation Framework.
    """

    # -----------------------------------------------------

    def __init__(self):

        self.history = []

        self.favorites = []

        self.last_module = None

        self.max_history = 100

    # -----------------------------------------------------

    def visit(self, module_id):

        record = {

            "module": module_id,

            "timestamp": time.time()

        }

        self.history.append(record)

        self.last_module = module_id

        if len(self.history) > self.max_history:

            self.history.pop(0)

        return record

    # -----------------------------------------------------

    def add_favorite(self, module_id):

        if module_id not in self.favorites:

            self.favorites.append(module_id)

    # -----------------------------------------------------

    def remove_favorite(self, module_id):

        if module_id in self.favorites:

            self.favorites.remove(module_id)

    # -----------------------------------------------------

    def is_favorite(self, module_id):

        return module_id in self.favorites

    # -----------------------------------------------------

    def recent(self, limit=10):

        return list(

            reversed(

                self.history[-limit:]

            )

        )

    # -----------------------------------------------------

    def last(self):

        return self.last_module

    # -----------------------------------------------------

    def clear(self):

        self.history.clear()

        self.last_module = None

    # -----------------------------------------------------

    def clear_favorites(self):

        self.favorites.clear()

    # -----------------------------------------------------

    def module_usage(self):

        usage = {}

        for record in self.history:

            module = record["module"]

            usage[module] = usage.get(

                module,

                0

            ) + 1

        return usage

    # -----------------------------------------------------

    def most_used(self, limit=10):

        usage = self.module_usage()

        ordered = sorted(

            usage.items(),

            key=lambda x: x[1],

            reverse=True

        )

        return ordered[:limit]

    # -----------------------------------------------------

    def statistics(self):

        return {

            "history": len(

                self.history

            ),

            "favorites": len(

                self.favorites

            ),

            "last": self.last_module

        }

    # -----------------------------------------------------

    def status(self):

        return {

            "component": "Navigation History",

            "history_size": len(

                self.history

            ),

            "favorites": len(

                self.favorites

            ),

            "last_module": self.last_module

        }


navigation_history = NavigationHistory()
