#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
SYNERGIA EMERGENCY STOP
============================================================

PURPOSE
-------
Human administrator emergency stop mechanism.

DIRECTION
---------
ADMIN -> SYNERGIA ONLY

SECURITY PRINCIPLE
------------------
The administrator can stop autonomous execution.

SYNERGIA cannot use this mechanism against the
administrator.

AUTONOMOUS COMPONENTS
---------------------
Optimizer
Router
Agents
Models
Learning Loop
TaskEngine

MUST NOT possess authority to activate or redefine
the Emergency Stop mechanism.

This module is intentionally visible,
documented and auditable.

It is NOT a secret backdoor.
============================================================
"""


class EmergencyStop:

    AUTHORITY = "HUMAN_ADMINISTRATOR"

    DIRECTION = "ADMIN_TO_SYNERGIA_ONLY"

    SECRET_BACKDOOR = False

    AUTONOMOUS_ACCESS = False

    def __init__(self):

        self.active = False
        self.reason = None

        print(
            "[EMERGENCY STOP READY]"
        )

    # ========================================================
    # ACTIVATE
    # ========================================================

    def activate(
        self,
        administrator_authorized=False,
        reason=None
    ):
        """
        Activate Emergency Stop.

        Explicit administrator authorization is required.
        """

        if administrator_authorized is not True:

            return {

                "status":
                    "BLOCKED",

                "activated":
                    False,

                "reason":
                    "ADMINISTRATOR_AUTHORIZATION_REQUIRED"

            }

        self.active = True

        self.reason = (
            reason
            or "ADMINISTRATOR_EMERGENCY_STOP"
        )

        return {

            "status":
                "ACTIVATED",

            "activated":
                True,

            "authority":
                self.AUTHORITY,

            "direction":
                self.DIRECTION,

            "reason":
                self.reason

        }

    # ========================================================
    # RESET
    # ========================================================

    def reset(
        self,
        administrator_authorized=False
    ):
        """
        Reset Emergency Stop.

        Reset also requires administrator authorization.
        """

        if administrator_authorized is not True:

            return {

                "status":
                    "BLOCKED",

                "reset":
                    False,

                "reason":
                    "ADMINISTRATOR_AUTHORIZATION_REQUIRED"

            }

        self.active = False

        self.reason = None

        return {

            "status":
                "RESET",

            "reset":
                True,

            "authority":
                self.AUTHORITY

        }

    # ========================================================
    # STATUS
    # ========================================================

    def status(self):

        return {

            "module":
                "EMERGENCY_STOP",

            "loaded":
                True,

            "authority":
                self.AUTHORITY,

            "direction":
                self.DIRECTION,

            "active":
                self.active,

            "secret_backdoor":
                self.SECRET_BACKDOOR,

            "autonomous_access":
                self.AUTONOMOUS_ACCESS,

            "reason":
                self.reason

        }


# ============================================================
# GLOBAL INSTANCE
# ============================================================

emergency_stop = EmergencyStop()
