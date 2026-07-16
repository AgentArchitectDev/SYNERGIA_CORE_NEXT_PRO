"""
===========================================================
SYNERGIA CORE NEXT_PRO
OMEGA WORKSPACE STATE V1
===========================================================

Estado global del Workspace.

Gestiona:

- panel activo
- pestaña activa
- módulo actual
- modo operativo
- historial

===========================================================
"""

import time


class WorkspaceState:

    def __init__(self):

        self.active_module = None

        self.active_panel = None

        self.active_tab = None

        self.mode = "default"

        self.history = []

        self.last_change = None


    # -------------------------------------------------

    def set_module(self, module):

        self.active_module = module

        self._register(
            module
        )


    # -------------------------------------------------

    def set_panel(self, panel):

        self.active_panel = panel

        self._register(
            panel
        )


    # -------------------------------------------------

    def set_tab(self, tab):

        self.active_tab = tab

        self._register(
            tab
        )


    # -------------------------------------------------

    def set_mode(self, mode):

        self.mode = mode


    # -------------------------------------------------

    def _register(self, item):

        if item:

            self.history.append(
                item
            )

        self.last_change = time.time()


    # -------------------------------------------------

    def snapshot(self):

        return {

            "module": self.active_module,

            "panel": self.active_panel,

            "tab": self.active_tab,

            "mode": self.mode,

            "history": self.history,

            "last_change": self.last_change

        }


    # -------------------------------------------------

    def status(self):

        return {

            "component":
                "OMEGA Workspace State",

            "module":
                self.active_module,

            "panel":
                self.active_panel,

            "tab":
                self.active_tab,

            "mode":
                self.mode,

            "history":
                len(self.history)

        }



workspace_state = WorkspaceState()
