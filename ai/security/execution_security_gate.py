#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
SYNERGIA EXECUTION SECURITY GATE
SECURITY-17
============================================================

Central execution interception layer.

FAIL-CLOSED:
If security state cannot be validated safely,
execution is BLOCKED.

The Gate does not execute anything.
It only authorizes or blocks execution.
============================================================
"""

from __future__ import annotations


class ExecutionSecurityGate:

    NAME = "EXECUTION_SECURITY_GATE"

    FAIL_CLOSED = True

    def __init__(
        self,
        emergency_stop=None,
        autonomy_off=None,
        master_security_lock=None,
        sovereign_escape=None,
    ):

        self.emergency_stop = emergency_stop
        self.autonomy_off = autonomy_off
        self.master_security_lock = master_security_lock
        self.sovereign_escape = sovereign_escape

        self.executions_checked = 0
        self.executions_allowed = 0
        self.executions_blocked = 0

        self.last_decision = None

        print("[EXECUTION SECURITY GATE READY]")

    # ========================================================
    # CONTROL CONNECTION
    # ========================================================

    def connect_controls(
        self,
        emergency_stop=None,
        autonomy_off=None,
        master_security_lock=None,
        sovereign_escape=None,
    ):

        if emergency_stop is not None:
            self.emergency_stop = emergency_stop

        if autonomy_off is not None:
            self.autonomy_off = autonomy_off

        if master_security_lock is not None:
            self.master_security_lock = master_security_lock

        if sovereign_escape is not None:
            self.sovereign_escape = sovereign_escape

        return self.status()

    # ========================================================
    # EXECUTION CHECK
    # ========================================================

    def check_execution(
        self,
        execution_name="UNKNOWN",
    ):

        self.executions_checked += 1

        controls = {
            "emergency_stop": self.emergency_stop,
            "autonomy_off": self.autonomy_off,
            "master_security_lock": self.master_security_lock,
            "sovereign_escape": self.sovereign_escape,
        }

        missing = [
            name
            for name, control in controls.items()
            if control is None
        ]

        if missing:

            return self._block(
                execution_name,
                "SECURITY_CONTROL_MISSING",
                missing,
            )

        # ----------------------------------------------------
        # EMERGENCY STOP
        # ----------------------------------------------------

        try:

            if self.emergency_stop.active:

                return self._block(
                    execution_name,
                    "EMERGENCY_STOP_ACTIVE",
                )

        except Exception:

            return self._block(
                execution_name,
                "EMERGENCY_STOP_STATE_UNREADABLE",
            )

        # ----------------------------------------------------
        # AUTONOMY OFF
        # ----------------------------------------------------

        try:

            if self.autonomy_off.active:

                return self._block(
                    execution_name,
                    "AUTONOMY_OFF_ACTIVE",
                )

        except Exception:

            return self._block(
                execution_name,
                "AUTONOMY_OFF_STATE_UNREADABLE",
            )

        # ----------------------------------------------------
        # MASTER SECURITY LOCK
        # ----------------------------------------------------

        try:

            if self.master_security_lock.is_locked():

                return self._block(
                    execution_name,
                    "MASTER_SECURITY_LOCK_ACTIVE",
                )

        except Exception:

            return self._block(
                execution_name,
                "MASTER_SECURITY_LOCK_STATE_UNREADABLE",
            )

        # ----------------------------------------------------
        # SOVEREIGN ESCAPE
        # ----------------------------------------------------

        try:

            if self.sovereign_escape.active:

                return self._block(
                    execution_name,
                    "SOVEREIGN_ESCAPE_ACTIVE",
                )

        except Exception:

            return self._block(
                execution_name,
                "SOVEREIGN_ESCAPE_STATE_UNREADABLE",
            )

        # ----------------------------------------------------
        # ALLOW
        # ----------------------------------------------------

        self.executions_allowed += 1

        decision = {
            "status": "ALLOWED",
            "authorized": True,
            "execution": execution_name,
            "fail_closed": self.FAIL_CLOSED,
            "reason": "SECURITY_CONTROLS_VALID",
        }

        self.last_decision = decision

        return decision

    # ========================================================
    # BLOCK
    # ========================================================

    def _block(
        self,
        execution_name,
        reason,
        details=None,
    ):

        self.executions_blocked += 1

        decision = {
            "status": "BLOCKED",
            "authorized": False,
            "execution": execution_name,
            "fail_closed": self.FAIL_CLOSED,
            "reason": reason,
        }

        if details is not None:
            decision["details"] = details

        self.last_decision = decision

        return decision

    # ========================================================
    # STATUS
    # ========================================================

    def status(self):

        return {
            "module": self.NAME,
            "loaded": True,
            "fail_closed": self.FAIL_CLOSED,
            "executions_checked": self.executions_checked,
            "executions_allowed": self.executions_allowed,
            "executions_blocked": self.executions_blocked,
            "last_decision": self.last_decision,
        }


# ============================================================
# GLOBAL INSTANCE
# ============================================================

execution_security_gate = ExecutionSecurityGate()
