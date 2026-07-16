"""
====================================================================
SYNERGIA OMEGA UI
Navigation Search V6 Enterprise
====================================================================

Unified Navigation Search

Buscador inteligente del Navigation Framework.

Preparado para:

✔ Modules
✔ Pages
✔ Commands
✔ Agents
✔ Memory
✔ Knowledge
✔ Models
✔ Plugins
✔ Runtime
✔ Servers

En futuras versiones será el Command Palette de OMEGA.

====================================================================
"""

from typing import List


class NavigationSearch:

    """
    Motor de búsqueda del Navigation Framework.
    """

    # ---------------------------------------------------------

    def __init__(self):

        self.registry = None

        self.history = []

        self.last_query = ""

        self.last_results = []

    # ---------------------------------------------------------

    def register_registry(self, registry):

        self.registry = registry

    # ---------------------------------------------------------

    def search(self, text: str):

        self.last_query = text

        self.history.append(text)

        if self.registry is None:

            return []

        text = text.lower()

        results = []

        modules = getattr(self.registry, "modules", {})

        for module in modules.values():

            score = self.calculate_score(

                module,

                text

            )

            if score > 0:

                results.append({

                    "score": score,

                    "module": module

                })

        results.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        self.last_results = results

        return results

    # ---------------------------------------------------------

    def calculate_score(

        self,

        module,

        query

    ):

        score = 0

        title = module.get(

            "title",

            ""

        ).lower()

        category = module.get(

            "category",

            ""

        ).lower()

        module_id = module.get(

            "id",

            ""

        ).lower()

        if query in title:

            score += 100

        if query in module_id:

            score += 80

        if query in category:

            score += 40

        return score

    # ---------------------------------------------------------

    def clear_history(self):

        self.history.clear()

    # ---------------------------------------------------------

    def recent_queries(self):

        return self.history[-20:]

    # ---------------------------------------------------------

    def last(self):

        return self.last_results

    # ---------------------------------------------------------

    def statistics(self):

        return {

            "queries": len(

                self.history

            ),

            "last_results": len(

                self.last_results

            )

        }

    # ---------------------------------------------------------

    def status(self):

        return {

            "engine": "Navigation Search",

            "last_query": self.last_query,

            "history": len(self.history),

            "results": len(self.last_results)

        }


navigation_search = NavigationSearch()
