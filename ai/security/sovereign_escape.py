#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNERGIA SOVEREIGN ESCAPE

PURPOSE
-------
Human administrator emergency recovery mechanism.

DIRECTION
---------
ADMIN -> SYNERGIA ONLY

FORBIDDEN
---------
SYNERGIA -> ADMIN

This mechanism is intentionally visible,
documented and auditable.

It is NOT a secret backdoor.
It is a documented sovereign recovery mechanism.
"""

class SovereignEscape:

    AUTHORITY = "HUMAN_ADMINISTRATOR"
    DIRECTION = "ADMIN_TO_SYNERGIA_ONLY"

    SECRET_BACKDOOR = False
    AUTONOMOUS_ACCESS = False

    def __init__(self):

        self.active = False
        self.reason = None

        print("[SOVEREIGN ESCAPE READY]")

    def activate(
        self,
        administrator_authorized=False,
        reason=None
    ):

        if administrator_authorized is not True:

            return {
                "status": "BLOCKED",
                "activated": False,
                "reason":
                    "ADMINISTRATOR_AUTHORIZATION_REQUIRED"
            }

        self.active = True

        self.reason = (
            reason
            or "ADMINISTRATOR_EMERGENCY_RECOVERY"
        )

        return {
            "status": "ACTIVATED",
            "activated": True,
            "authority": self.AUTHORITY,
            "direction": self.DIRECTION,
            "reason": self.reason
        }

    def reset(
        self,
        administrator_authorized=False
    ):

        if administrator_authorized is not True:

            return {
                "status": "BLOCKED",
                "activated": True,
                "reason":
                    "ADMINISTRATOR_AUTHORIZATION_REQUIRED"
            }

        self.active = False
        self.reason = None

        return {
            "status": "RESET",
            "activated": False,
            "authority": self.AUTHORITY,
            "direction": self.DIRECTION
        }


    def status(self):

        return {
            "module":
                "SOVEREIGN_ESCAPE",

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


sovereign_escape = SovereignEscape()
