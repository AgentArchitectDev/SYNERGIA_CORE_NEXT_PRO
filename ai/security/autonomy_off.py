#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
SYNERGIA AUTONOMY OFF
============================================================

STAGE 6.3.15.7.11.3-S3

PURPOSE
-------
Human administrator control that disables autonomous
decision and execution capabilities.

DIRECTION
---------
ADMIN -> SYNERGIA ONLY

SECURITY PRINCIPLE
------------------
The administrator may disable autonomy.

Autonomous components MUST NOT be able to:

- activate autonomy
- disable this protection
- modify authorization rules
- redefine administrator authority

IMPORTANT
---------
AUTONOMY OFF does not erase memory.
AUTONOMY OFF does not destroy the system.
AUTONOMY OFF does not modify the Router.

It establishes a security state in which autonomous
execution is prohibited.

This mechanism is visible, documented and auditable.

It is NOT a secret backdoor.
============================================================
"""


class AutonomyOff:

    AUTHORITY = "HUMAN_ADMINISTRATOR"

    DIRECTION = "ADMIN_TO_SYNERGIA_ONLY"

    SECRET_BACKDOOR = False

    AUTONOMOUS_ACCESS = False

    def __init__(self):

        self.active = False
        self.reason = None

        print(
            "[AUTONOMY OFF READY]"
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
        Disable autonomous operation.

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
            or "ADMINISTRATOR_AUTONOMY_OFF"
        )

        return {

            "status":
                "ACTIVATED",

            "activated":
                True,

            "autonomy":
                "OFF",

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
        Restore autonomous operation.

        Explicit administrator authorization is required.
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

            "autonomy":
                "AVAILABLE",

            "authority":
                self.AUTHORITY

        }

    # ========================================================
    # CAN AUTONOMOUS EXECUTION PROCEED?
    # ========================================================

    def autonomous_execution_allowed(self):

        return not self.active

    # ========================================================
    # STATUS
    # ========================================================

    def status(self):

        return {

            "module":
                "AUTONOMY_OFF",

            "loaded":
                True,

            "authority":
                self.AUTHORITY,

            "direction":
                self.DIRECTION,

            "active":
                self.active,

            "autonomous_execution_allowed":
                self.autonomous_execution_allowed(),

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

autonomy_off = AutonomyOff()
