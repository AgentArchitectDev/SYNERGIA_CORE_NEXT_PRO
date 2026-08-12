#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNERGIA — SECURITY CONTROL CONSISTENCY VALIDATOR

STAGE 6.3.15.7.11.3-S5.6-A

Purpose
-------

Validate that all sovereign security controls share the
same canonical security identity.

Canonical authority:

    HUMAN_ADMINISTRATOR

Canonical direction:

    ADMIN_TO_SYNERGIA_ONLY

Autonomous security authority:

    ZERO

This validator:

- does not activate controls
- does not deactivate controls
- does not modify controls
- does not modify the security specification
- does not grant authority
- does not create authority
- does not bypass the Sovereign Security Core

It only validates consistency.
"""

from __future__ import annotations

from typing import Any, Dict


class SecurityControlConsistencyValidator:

    MODULE = "SECURITY_CONTROL_CONSISTENCY_VALIDATOR"

    CANONICAL_AUTHORITY = "HUMAN_ADMINISTRATOR"
    CANONICAL_DIRECTION = "ADMIN_TO_SYNERGIA_ONLY"
    CANONICAL_AUTONOMOUS_SECURITY_AUTHORITY = "ZERO"

    def __init__(self) -> None:
        self.last_validation = None

        print("[SECURITY CONTROL CONSISTENCY VALIDATOR READY]")

    def status(self) -> Dict[str, Any]:
        return {
            "module": self.MODULE,
            "loaded": True,
            "canonical_authority": self.CANONICAL_AUTHORITY,
            "canonical_direction": self.CANONICAL_DIRECTION,
            "canonical_autonomous_security_authority":
                self.CANONICAL_AUTONOMOUS_SECURITY_AUTHORITY,
            "last_validation": self.last_validation,
        }

    def _validate_control(
        self,
        name: str,
        control: Any,
    ) -> Dict[str, Any]:

        result = {
            "status": "VALID",
            "valid": True,
            "name": name,
            "errors": [],
        }

        try:
            data = control.status()
        except Exception as exc:
            result["status"] = "INVALID"
            result["valid"] = False
            result["errors"].append(
                f"STATUS_READ_ERROR:{type(exc).__name__}"
            )
            return result

        if data.get("loaded") is not True:
            result["valid"] = False
            result["errors"].append("CONTROL_NOT_LOADED")

        if data.get("authority") != self.CANONICAL_AUTHORITY:
            result["valid"] = False
            result["errors"].append("INVALID_AUTHORITY")

        if data.get("direction") != self.CANONICAL_DIRECTION:
            result["valid"] = False
            result["errors"].append("INVALID_DIRECTION")

        if data.get("secret_backdoor") is not False:
            result["valid"] = False
            result["errors"].append("SECRET_BACKDOOR_DETECTED")

        if data.get("autonomous_access") is not False:
            result["valid"] = False
            result["errors"].append("AUTONOMOUS_ACCESS_DETECTED")

        if name == "AUTONOMY_OFF":
            if data.get("autonomous_execution_allowed") is not True:
                result["valid"] = False
                result["errors"].append(
                    "AUTONOMOUS_EXECUTION_STATE_INVALID"
                )

        if result["valid"]:
            result["status"] = "VALID"
        else:
            result["status"] = "INVALID"

        result["control_status"] = data

        return result

    def validate(self) -> Dict[str, Any]:

        from ai.security.sovereign_escape import sovereign_escape
        from ai.security.emergency_stop import emergency_stop
        from ai.security.autonomy_off import autonomy_off
        from ai.security.master_lock import master_security_lock

        controls = [
            ("SOVEREIGN_ESCAPE", sovereign_escape),
            ("EMERGENCY_STOP", emergency_stop),
            ("AUTONOMY_OFF", autonomy_off),
            ("MASTER_SECURITY_LOCK", master_security_lock),
        ]

        results = []

        for name, control in controls:
            results.append(
                self._validate_control(name, control)
            )

        invalid_controls = [
            result
            for result in results
            if not result["valid"]
        ]

        result = {
            "status": (
                "VALID"
                if not invalid_controls
                else "INVALID"
            ),
            "valid": not invalid_controls,
            "module": self.MODULE,
            "canonical_authority": self.CANONICAL_AUTHORITY,
            "canonical_direction": self.CANONICAL_DIRECTION,
            "canonical_autonomous_security_authority":
                self.CANONICAL_AUTONOMOUS_SECURITY_AUTHORITY,
            "controls_checked": len(results),
            "controls_invalid": len(invalid_controls),
            "results": results,
        }

        self.last_validation = result

        return result


security_control_consistency_validator = (
    SecurityControlConsistencyValidator()
)
