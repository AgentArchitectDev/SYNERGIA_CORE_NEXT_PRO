"""
====================================================================
SYNERGIA OMEGA UI
Navigation Controller V6 Enterprise
====================================================================

Controlador principal del Navigation Framework.

Centraliza la coordinación entre todos los componentes
de navegación.

Componentes gestionados

✔ Navigation Manager
✔ Navigation Builder
✔ Navigation Search
✔ Navigation History
✔ Navigation State

Preparado para:

✔ IA
✔ OMEGA
✔ Multi Workspace
✔ Plugins
✔ Persistencia

====================================================================
"""

from gui.navigation.navigation_manager import navigation_manager
from gui.navigation.navigation_builder import navigation_builder
from gui.navigation.navigation_search import navigation_search
from gui.navigation.navigation_history import navigation_history
from gui.navigation.navigation_state import navigation_state


class NavigationController:
    """
    Controlador principal del Navigation Framework.
    """

    # ---------------------------------------------------------

    def __init__(self):

        self.initialized = False

    # ---------------------------------------------------------

    def initialize(self, registry):

        navigation_manager.registry = registry

        navigation_search.register_registry(registry)

        navigation_builder.build()

        self.initialized = True

        return {

            "status": "initialized"

        }

    # ---------------------------------------------------------

    def open(self, module_id):

        navigation_manager.open(module_id)

        navigation_history.visit(module_id)

        navigation_state.set_active_module(module_id)

        navigation_builder.highlight(module_id)

        return {

            "status": "opened",

            "module": module_id

        }

    # ---------------------------------------------------------

    def search(self, text):

        return navigation_search.search(text)

    # ---------------------------------------------------------

    def favorites(self):

        return navigation_history.favorites

    # ---------------------------------------------------------

    def add_favorite(self, module_id):

        navigation_history.add_favorite(module_id)

    # ---------------------------------------------------------

    def remove_favorite(self, module_id):

        navigation_history.remove_favorite(module_id)

    # ---------------------------------------------------------

    def expand_category(self, category):

        navigation_state.expand_category(category)

    # ---------------------------------------------------------

    def collapse_category(self, category):

        navigation_state.collapse_category(category)

    # ---------------------------------------------------------

    def current_module(self):

        return navigation_state.get_active_module()

    # ---------------------------------------------------------

    def refresh(self):

        navigation_builder.refresh()

    # ---------------------------------------------------------

    def snapshot(self):

        return {

            "state": navigation_state.snapshot(),

            "history": navigation_history.statistics(),

            "search": navigation_search.statistics(),

            "builder": navigation_builder.status()

        }

    # ---------------------------------------------------------

    def restore(self, snapshot):

        navigation_state.restore(

            snapshot.get(

                "state",

                {}

            )

        )

        navigation_builder.refresh()

    # ---------------------------------------------------------

    def status(self):

        return {

            "initialized": self.initialized,

            "manager": navigation_manager.status(),

            "builder": navigation_builder.status(),

            "history": navigation_history.statistics(),

            "search": navigation_search.statistics(),

            "state": navigation_state.status()

        }


navigation_controller = NavigationController()
