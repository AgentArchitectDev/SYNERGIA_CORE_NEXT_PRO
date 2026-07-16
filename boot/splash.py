#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

BOOT SPLASH

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================
"""

import os
import time


class BootSplash:

    """
    Pantalla inicial del Boot.

    En versiones futuras esta clase controlará:

    - Splash Qt
    - Barra gráfica
    - Logo animado
    - Progreso
    - Carga de módulos
    """

    VERSION = "OMEGA 1.0"

    BUILD = "ACEA"

    COMPANY = "CORE IA SYSTEMS"

    SYSTEM = "SYNERGIA OMEGA"

    # --------------------------------------------------

    def __init__(self):

        self.progress = 0

    # --------------------------------------------------

    def clear(self):

        os.system("cls" if os.name == "nt" else "clear")

    # --------------------------------------------------

    def banner(self):

        print()

        print("############################################################")
        print("#                                                          #")
        print("#                 SYNERGIA OMEGA                           #")
        print("#                                                          #")
        print("#             Artificial Cognitive OS                      #")
        print("#                                                          #")
        print("#                 CORE IA SYSTEMS                          #")
        print("#                                                          #")
        print("############################################################")

        print()

        print("Version :", self.VERSION)

        print("Build   :", self.BUILD)

        print()

    # --------------------------------------------------

    def loading(self):

        print()

        print("Inicializando Boot Manager...")

        for i in range(0, 101, 10):

            self.progress = i

            bar = "█" * (i // 5)

            empty = "░" * (20 - len(bar))

            print(
                f"\r[{bar}{empty}] {i:3d}% ",
                end="",
                flush=True,
            )

            time.sleep(0.05)

        print()

        print()

    # --------------------------------------------------

    def show(self):

        self.clear()

        self.banner()

        self.loading()

    # --------------------------------------------------

    def status(self):

        return {

            "component": "SYNERGIA Splash",

            "version": self.VERSION,

            "progress": self.progress,

        }


boot_splash = BootSplash()
