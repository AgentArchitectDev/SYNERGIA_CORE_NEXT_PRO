#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

BOOT CONTROLLER V2

CORE IA SYSTEMS

ACEA

============================================================

Orquestador principal del arranque.

BOOT
 |
 +-- Core Bridge
 +-- Runtime Manager
 +-- Agent Manager
 +-- Shell Controller

============================================================
"""


from gui.control_center.core_bridge import core_bridge

from gui.control_center.runtime_manager import runtime_manager

from gui.control_center.agent_manager import agent_manager

from gui.control_center.shell_controller import shell_controller



class BootController:


    def __init__(self):

        self.started = False

        self.profile = None

        self.mode = None

        self.components = []



    # --------------------------------------------------


    def start(self, profile, mode):


        self.profile = profile

        self.mode = mode


        print()

        print(
            "===================================="
        )

        print(
            " INICIANDO SYNERGIA OMEGA"
        )

        print(
            "===================================="
        )


        self.components.clear()



        # CORE

        try:

            core_result = core_bridge.connect()

            self.components.append(
                "Core Bridge"
            )

            print(
                "[ OK ] Core Bridge"
            )

        except Exception as e:

            print(
                "[FAIL] Core Bridge",
                e
            )



        # RUNTIME

        try:

            runtime_manager.initialize()

            self.components.append(
                "Runtime Manager"
            )

            print(
                "[ OK ] Runtime Manager"
            )

        except Exception as e:

            print(
                "[FAIL] Runtime Manager",
                e
            )



        # AGENTS

        try:

            agent_manager.initialize()

            self.components.append(
                "Agent Manager"
            )

            print(
                "[ OK ] Agent Manager"
            )

        except Exception as e:

            print(
                "[FAIL] Agent Manager",
                e
            )



        # CONTROL CENTER

        try:

            shell_controller.initialize()

            shell_controller.start()

            self.components.append(
                "Control Center"
            )

            print(
                "[ OK ] Control Center"
            )


        except Exception as e:

            print(
                "[FAIL] Control Center",
                e
            )



        self.started = True


        print()

        print(
            "===================================="
        )

        print(
            " SYNERGIA ONLINE"
        )

        print(
            "===================================="
        )


        return self.status()



    # --------------------------------------------------


    def status(self):


        return {


            "component":
            "OMEGA Boot Controller V2",


            "started":
            self.started,


            "profile":
            self.profile,


            "mode":
            self.mode,


            "components":
            self.components


        }



boot_controller = BootController()
