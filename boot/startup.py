#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

BOOT STARTUP

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

Responsable de preparar el entorno antes de iniciar
el sistema.

En futuras versiones iniciará automáticamente:

- Runtime Manager
- Agent Manager
- Core Bridge
- Workspace
- Control Center
- Model Router
- Memoria Persistente

============================================================
"""


class BootStartup:

    """
    Preparación del entorno de arranque.
    """

    def __init__(self):

        self.machine = None
        self.mode = None

        self.modules = []

    # ------------------------------------------------------

    def prepare(self, machine, mode):

        self.machine = machine
        self.mode = mode

        self.modules.clear()

        print()

        print("Preparando entorno...")

        print()

        # -----------------------------------------

        self._load("Workspace")

        self._load("Core Bridge")

        self._load("Runtime Connector")

        self._load("Runtime Manager")

        self._load("Agent Manager")

        # -----------------------------------------

        if mode in ("runtime", "production", "ai"):

            self._load("Ollama")

        if mode in ("development",):

            self._load("Developer Tools")

        if mode == "diagnostic":

            self._load("Diagnostics")

        if mode == "benchmark":

            self._load("Benchmark Engine")

        print()

        print("------------------------------------------")

        print("Entorno preparado.")

        print("------------------------------------------")

        return self.status()

    # ------------------------------------------------------

    def _load(self, module):

        print(f"[ OK ] {module}")

        self.modules.append(module)

    # ------------------------------------------------------

    def status(self):

        return {

            "component": "OMEGA Boot Startup",

            "machine": self.machine,

            "mode": self.mode,

            "modules": self.modules,

            "count": len(self.modules)

        }


boot_startup = BootStartup()
