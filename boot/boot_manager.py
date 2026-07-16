#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
========================================================

BOOT MANAGER

SYNERGIA OMEGA

ACEA V1

========================================================
"""

from boot.environment import Environment

from boot.menu import BootMenu

from boot.profile import BootProfile

from boot.splash import BootSplash

from boot.startup import BootStartup


class BootManager:

    """
    Director del proceso de arranque.
    """

    def __init__(self):

        self.environment = Environment()

        self.menu = BootMenu()

        self.profile = BootProfile()

        self.splash = BootSplash()

        self.startup = BootStartup()

    # --------------------------------------------------

    def boot(self):

        self.splash.show()

        self.environment.detect()

        self.environment.print_summary()

        machine = self.menu.select_machine()

        mode = self.menu.select_mode()

        self.profile.load(machine)

        self.startup.prepare(machine, mode)

        print()

        print("========================================")

        print("BOOT FINALIZADO")

        print()

        print("Nodo :", machine)

        print("Modo :", mode)

        print()

        print("Listo para iniciar SYNERGIA")

        print("========================================")
