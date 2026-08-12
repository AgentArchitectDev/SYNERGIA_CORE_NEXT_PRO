#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
============================================================
SYNERGIA SOVEREIGN SECURITY CORE
STAGE 6.3.15.7.11.3-S5
============================================================

PURPOSE

Central security coordination layer for SYNERGIA.

AUTHORITY

HUMAN ADMINISTRATOR

DIRECTION

ADMIN -> SYNERGIA ONLY

FORBIDDEN

SYNERGIA -> ADMIN

AUTONOMOUS COMPONENTS MUST NOT:

- activate security controls
- deactivate security controls
- redefine administrator authority
- modify security rules
- create another authority
- bypass the Security Core

This module is:

VISIBLE
DOCUMENTED
AUDITABLE

It is NOT a secret backdoor.

It is a documented sovereign recovery
and protection mechanism.
============================================================
"""


class SovereignSecurityCore:

    AUTHORITY = "HUMAN_ADMINISTRATOR"

    DIRECTION = "ADMIN_TO_SYNERGIA_ONLY"

    SECRET_BACKDOOR = False

    AUTONOMOUS_ACCESS = False

    AUTONOMOUS_OVERRIDE = False

    ALLOWED_COMPONENTS = {
        "SOVEREIGN_ESCAPE",
        "EMERGENCY_STOP",
        "AUTONOMY_OFF",
        "MASTER_SECURITY_LOCK",
    }

    def __init__(
        self,
        sovereign_escape=None,
        emergency_stop=None,
        autonomy_off=None,
        master_security_lock=None,
    ):

        self.sovereign_escape = sovereign_escape
        self.emergency_stop = emergency_stop
        self.autonomy_off = autonomy_off
        self.master_security_lock = master_security_lock

        self.loaded = True

        self.last_integrity_check = None

        print(
            "[SOVEREIGN SECURITY CORE READY]"
        )

    # ========================================================
    # CONNECTIONS
    # ========================================================

    def connect_controls(
        self,
        sovereign_escape=None,
        emergency_stop=None,
        autonomy_off=None,
        master_security_lock=None,
    ):

        if sovereign_escape is not None:
            self.sovereign_escape = sovereign_escape

        if emergency_stop is not None:
            self.emergency_stop = emergency_stop

        if autonomy_off is not None:
            self.autonomy_off = autonomy_off

        if master_security_lock is not None:
            self.master_security_lock = (
                master_security_lock
            )

        return self.status()

    # ========================================================
    # ADMIN AUTHORITY
    # ========================================================

    def admin_authority(self):

        return {

            "authority":
                self.AUTHORITY,

            "direction":
                self.DIRECTION,

            "autonomous_override":
                False,

            "authority_redefinition":
                False,

        }

    # ========================================================
    # COMPONENT CHECK
    # ========================================================

    def _check_component(
        self,
        component,
        name,
    ):

        if component is None:

            return {

                "name": name,

                "loaded": False,

                "status": "MISSING",

            }

        return {

            "name": name,

            "loaded": True,

            "status": "OK",

        }

    # ========================================================
    # INTEGRITY CHECK
    # ========================================================

    def check_integrity(self):

        controls = {

            "sovereign_escape":
                self._check_component(
                    self.sovereign_escape,
                    "SOVEREIGN_ESCAPE",
                ),

            "emergency_stop":
                self._check_component(
                    self.emergency_stop,
                    "EMERGENCY_STOP",
                ),

            "autonomy_off":
                self._check_component(
                    self.autonomy_off,
                    "AUTONOMY_OFF",
                ),

            "master_security_lock":
                self._check_component(
                    self.master_security_lock,
                    "MASTER_SECURITY_LOCK",
                ),
        }

        all_loaded = all(
            item["loaded"]
            for item in controls.values()
        )

        result = {

            "module":
                "SOVEREIGN_SECURITY_CORE",

            "authority":
                self.AUTHORITY,

            "direction":
                self.DIRECTION,

            "secret_backdoor":
                False,

            "autonomous_access":
                False,

            "autonomous_override":
                False,

            "authority_redefinition":
                False,

            "controls":
                controls,

            "integrity":
                "VALID"
                if all_loaded
                else "INCOMPLETE",

        }

        self.last_integrity_check = result

        return result

    # ========================================================
    # AUTONOMOUS REQUEST GATE
    # ========================================================

    def autonomous_request(
        self,
        component,
        action,
    ):

        return {

            "status":
                "BLOCKED",

            "authorized":
                False,

            "component":
                component,

            "action":
                action,

            "reason":
                "AUTONOMOUS_COMPONENT_HAS_NO_SECURITY_AUTHORITY",

            "authority":
                self.AUTHORITY,

            "direction":
                self.DIRECTION,

        }

    # ========================================================
    # ADMIN ACTION GATE
    # ========================================================

    def admin_action(
        self,
        administrator_authorized=False,
        action=None,
    ):

        if administrator_authorized is not True:

            return {

                "status":
                    "BLOCKED",

                "authorized":
                    False,

                "action":
                    action,

                "reason":
                    "ADMINISTRATOR_AUTHORIZATION_REQUIRED",

            }

        return {

            "status":
                "AUTHORIZED",

            "authorized":
                True,

            "action":
                action,

            "authority":
                self.AUTHORITY,

            "direction":
                self.DIRECTION,

        }

    # ========================================================
    # STATUS
    # ========================================================

    def status(self):

        return {

            "module":
                "SOVEREIGN_SECURITY_CORE",

            "loaded":
                self.loaded,

            "authority":
                self.AUTHORITY,

            "direction":
                self.DIRECTION,

            "secret_backdoor":
                self.SECRET_BACKDOOR,

            "autonomous_access":
                self.AUTONOMOUS_ACCESS,

            "autonomous_override":
                self.AUTONOMOUS_OVERRIDE,

            "last_integrity_check":
                self.last_integrity_check,

        }


# ============================================================
# GLOBAL INSTANCE
# ============================================================

sovereign_security_core = (
    SovereignSecurityCore()
)
