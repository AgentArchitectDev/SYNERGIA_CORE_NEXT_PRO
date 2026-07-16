"""
====================================================================
SYNERGIA OMEGA UI
Navigation Manager V6 Enterprise
====================================================================

Administrador central del sistema de navegación.

No contiene widgets.

No contiene botones.

No contiene layouts.

Únicamente administra el estado y coordina la navegación.

====================================================================
"""

from typing import Dict, List, Optional


class NavigationManager:

    """
    Cerebro del Navigation Framework.
    """

    def __init__(self):

        self.workspace = None

        self.registry = None

        self.current_module = None

        self.previous_module = None

        self.history: List[str] = []

        self.favorites = set()

        self.loaded = False

    # =====================================================

    def register_workspace(self, workspace):

        self.workspace = workspace

    # =====================================================

    def register_registry(self, registry):

        self.registry = registry

    # =====================================================

    def initialize(self):

        if self.registry is None:

            raise RuntimeError(
                "Module Registry no registrado."
            )

        self.registry.load_modules()

        self.loaded = True

    # =====================================================

    def open(self, module_id: str):

        if self.workspace is None:

            return False

        if self.current_module:

            self.previous_module = self.current_module

        self.current_module = module_id

        self.history.append(module_id)

        self.workspace.show_page(module_id)

        return True

    # =====================================================

    def reload(self):

        if self.registry:

            self.registry.reload()

        if self.workspace:

            self.workspace.reload()

    # =====================================================

    def back(self):

        if len(self.history) < 2:

            return

        self.history.pop()

        previous = self.history[-1]

        self.current_module = previous

        self.workspace.show_page(previous)

    # =====================================================

    def add_favorite(self, module_id):

        self.favorites.add(module_id)

    # =====================================================

    def remove_favorite(self, module_id):

        self.favorites.discard(module_id)

    # =====================================================

    def get_favorites(self):

        return sorted(self.favorites)

    # =====================================================

    def search(self, text):

        if self.registry is None:

            return []

        text = text.lower()

        result = []

        for module in self.registry.modules.values():

            if text in module["title"].lower():

                result.append(module)

        return result

    # =====================================================

    def statistics(self):

        return {

            "history": len(self.history),

            "favorites": len(self.favorites)

        }

    # =====================================================

    def status(self):

        return {

            "framework": "OMEGA Navigation",

            "loaded": self.loaded,

            "current": self.current_module,

            "previous": self.previous_module,

            "history": len(self.history),

            "favorites": len(self.favorites)

        }


navigation_manager = NavigationManager()
