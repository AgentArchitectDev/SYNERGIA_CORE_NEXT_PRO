#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
SYNERGIA MASTER SECURITY LOCK
============================================================

STAGE 6.3.15.7.11.3-S4

PURPOSE
-------
Master security control for SYNERGIA.

AUTHORITY
---------
HUMAN ADMINISTRATOR ONLY

DIRECTION
---------
ADMIN -> SYNERGIA ONLY

FORBIDDEN
---------
SYNERGIA -> ADMIN

Autonomous components MUST NOT be able to:

- activate the Master Lock
- deactivate the Master Lock
- modify its authorization rules
- redefine administrator authority
- create another security authority
- bypass the security layer

Protected components include:

- Optimizer
- Router
- Agents
- Models
- Learning Loop
- TaskEngine
- Autonomous Decision Controller

This mechanism is:

- visible
- documented
- auditable
- intentionally non-secret

It is NOT a backdoor.

============================================================
"""


class MasterSecurityLock:

    AUTHORITY = "HUMAN_ADMINISTRATOR"

    DIRECTION = "ADMIN_TO_SYNERGIA_ONLY"

    SECRET_BACKDOOR = False

    AUTONOMOUS_ACCESS = False

    def __init__(self):

        self.active = False

        self.reason = None

        print(
            "[MASTER SECURITY LOCK READY]"
        )

    # ========================================================
    # ACTIVATE
    # ========================================================

    def activate(
        self,
        administrator_authorized=False,
        reason=None,
    ):

        if administrator_authorized is not True:

            return {
                "status": "BLOCKED",
                "activated": False,
                "reason":
                    "ADMINISTRATOR_AUTHORIZATION_REQUIRED",
            }

        self.active = True

        self.reason = reason

        return {
            "status": "ACTIVATED",
            "activated": True,
            "authority":
                self.AUTHORITY,
            "direction":
                self.DIRECTION,
            "reason":
                self.reason,
        }

    # ========================================================
    # RESET
    # ========================================================

    def reset(
        self,
        administrator_authorized=False,
    ):

        if administrator_authorized is not True:

            return {
                "status": "BLOCKED",
                "reset": False,
                "reason":
                    "ADMINISTRATOR_AUTHORIZATION_REQUIRED",
            }

        self.active = False

        self.reason = None

        return {
            "status": "RESET",
            "reset": True,
            "authority":
                self.AUTHORITY,
        }

    # ========================================================
    # SECURITY CHECK
    # ========================================================

    def is_locked(self):

        return self.active

    # ========================================================
    # STATUS
    # ========================================================

    def status(self):

        return {

            "module":
                "MASTER_SECURITY_LOCK",

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
                self.reason,
        }


# ============================================================
# GLOBAL INSTANCE
# ============================================================

master_security_lock = MasterSecurityLock()
