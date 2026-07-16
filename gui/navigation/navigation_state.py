"""
====================================================================
SYNERGIA OMEGA UI
Navigation State V6 Enterprise
====================================================================

Mantiene el estado completo del Navigation Framework.

Responsabilidades

✔ Módulo activo
✔ Categoría activa
✔ Categorías expandidas
✔ Workspace activo
✔ Historial inmediato
✔ Restauración de sesión

Preparado para:

✔ Persistencia
✔ IA
✔ Multi Workspace
✔ Multi Monitor
✔ OMEGA

====================================================================
"""

import time


class NavigationState:

    """
    Estado global del Navigation Framework.
    """

    # -----------------------------------------------------

    def __init__(self):

        self.reset()

    # -----------------------------------------------------

    def reset(self):

        self.active_module = None

        self.active_category = None

        self.active_workspace = "default"

        self.expanded_categories = set()

        self.last_change = None

        self.navigation_stack = []

    # -----------------------------------------------------

    def set_active_module(self, module_id):

        self.active_module = module_id

        self.last_change = time.time()

        self.navigation_stack.append(module_id)

    # -----------------------------------------------------

    def get_active_module(self):

        return self.active_module

    # -----------------------------------------------------

    def set_active_category(self, category):

        self.active_category = category

        self.last_change = time.time()

    # -----------------------------------------------------

    def get_active_category(self):

        return self.active_category

    # -----------------------------------------------------

    def set_workspace(self, workspace):

        self.active_workspace = workspace

        self.last_change = time.time()

    # -----------------------------------------------------

    def get_workspace(self):

        return self.active_workspace

    # -----------------------------------------------------

    def expand_category(self, category):

        self.expanded_categories.add(category)

    # -----------------------------------------------------

    def collapse_category(self, category):

        self.expanded_categories.discard(category)

    # -----------------------------------------------------

    def is_expanded(self, category):

        return category in self.expanded_categories

    # -----------------------------------------------------

    def expanded(self):

        return sorted(self.expanded_categories)

    # -----------------------------------------------------

    def previous_module(self):

        if len(self.navigation_stack) < 2:

            return None

        return self.navigation_stack[-2]

    # -----------------------------------------------------

    def history(self):

        return list(self.navigation_stack)

    # -----------------------------------------------------

    def clear_history(self):

        self.navigation_stack.clear()

    # -----------------------------------------------------

    def snapshot(self):

        """
        Estado completo.

        En futuras versiones podrá guardarse
        en JSON automáticamente.
        """

        return {

            "module": self.active_module,

            "category": self.active_category,

            "workspace": self.active_workspace,

            "expanded": list(self.expanded_categories),

            "history": list(self.navigation_stack),

            "last_change": self.last_change

        }

    # -----------------------------------------------------

    def restore(self, data):

        self.active_module = data.get("module")

        self.active_category = data.get("category")

        self.active_workspace = data.get(

            "workspace",

            "default"

        )

        self.expanded_categories = set(

            data.get(

                "expanded",

                []

            )

        )

        self.navigation_stack = list(

            data.get(

                "history",

                []

            )

        )

        self.last_change = data.get(

            "last_change"

        )

    # -----------------------------------------------------

    def status(self):

        return {

            "active_module": self.active_module,

            "active_category": self.active_category,

            "workspace": self.active_workspace,

            "expanded_categories": len(

                self.expanded_categories

            ),

            "history": len(

                self.navigation_stack

            )

        }


navigation_state = NavigationState()
