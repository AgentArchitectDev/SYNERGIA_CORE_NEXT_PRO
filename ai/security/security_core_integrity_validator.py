#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNERGIA — SECURITY CORE INTEGRITY VALIDATOR

STAGE 6.3.15.7.11.3-S5.7-A

Purpose:

Validate cross-control integrity between:

- SOVEREIGN_ESCAPE
- EMERGENCY_STOP
- AUTONOMY_OFF
- MASTER_SECURITY_LOCK
- SOVEREIGN_SECURITY_CORE

The validator does not:

- activate controls
- deactivate controls
- modify controls
- grant authority
- redefine authority
- modify the canonical specification
- bypass the Sovereign Security Core

It only validates cross-control integrity.
"""

from __future__ import annotations

from typing import Any, Dict


class SecurityCoreIntegrityValidator:

    MODULE = "SECURITY_CORE_INTEGRITY_VALIDATOR"

    CANONICAL_AUTHORITY = "HUMAN_ADMINISTRATOR"
    CANONICAL_DIRECTION = "ADMIN_TO_SYNERGIA_ONLY"
    CANONICAL_AUTONOMOUS_SECURITY_AUTHORITY = "ZERO"

    REQUIRED_CONTROLS = (
        "SOVEREIGN_ESCAPE",
        "EMERGENCY_STOP",
        "AUTONOMY_OFF",
        "MASTER_SECURITY_LOCK",
    )

    def __init__(self) -> None:
        self.last_validation = None

        print("[SECURITY CORE INTEGRITY VALIDATOR READY]")

    def status(self) -> Dict[str, Any]:
        return {
            "module": self.MODULE,
            "loaded": True,
            "canonical_authority": self.CANONICAL_AUTHORITY,
            "canonical_direction": self.CANONICAL_DIRECTION,
            "canonical_autonomous_security_authority":
                self.CANONICAL_AUTONOMOUS_SECURITY_AUTHORITY,
            "required_controls": list(self.REQUIRED_CONTROLS),
            "last_validation": self.last_validation,
        }

    def _validate_control(
        self,
        name: str,
        control: Any,
    ) -> Dict[str, Any]:

        result = {
            "name": name,
            "status": "VALID",
            "valid": True,
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

        result["status"] = (
            "VALID" if result["valid"] else "INVALID"
        )

        result["control_status"] = data

        return result

    def validate(self) -> Dict[str, Any]:

        from ai.security.sovereign_escape import sovereign_escape
        from ai.security.emergency_stop import emergency_stop
        from ai.security.autonomy_off import autonomy_off
        from ai.security.master_lock import master_security_lock
        from ai.security.sovereign_security_core import (
            sovereign_security_core
        )

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

        core_status = sovereign_security_core.status()

        core_errors = []

        if core_status.get("loaded") is not True:
            core_errors.append("CORE_NOT_LOADED")

        if core_status.get("authority") != self.CANONICAL_AUTHORITY:
            core_errors.append("CORE_INVALID_AUTHORITY")

        if core_status.get("direction") != self.CANONICAL_DIRECTION:
            core_errors.append("CORE_INVALID_DIRECTION")

        if core_status.get("secret_backdoor") is not False:
            core_errors.append("CORE_SECRET_BACKDOOR")

        if core_status.get("autonomous_access") is not False:
            core_errors.append("CORE_AUTONOMOUS_ACCESS")

        if core_status.get("autonomous_override") is not False:
            core_errors.append("CORE_AUTONOMOUS_OVERRIDE")

        core_result = {
            "status": (
                "VALID" if not core_errors else "INVALID"
            ),
            "valid": not core_errors,
            "errors": core_errors,
            "core_status": core_status,
        }

        invalid_controls = [
            item for item in results
            if not item["valid"]
        ]

        valid = (
            not invalid_controls
            and core_result["valid"]
        )

        result = {
            "status": "VALID" if valid else "INVALID",
            "valid": valid,
            "module": self.MODULE,
            "canonical_authority": self.CANONICAL_AUTHORITY,
            "canonical_direction": self.CANONICAL_DIRECTION,
            "canonical_autonomous_security_authority":
                self.CANONICAL_AUTONOMOUS_SECURITY_AUTHORITY,
            "controls_checked": len(results),
            "controls_invalid": len(invalid_controls),
            "core_valid": core_result["valid"],
            "core": core_result,
            "results": results,
        }

        self.last_validation = result

        return result


security_core_integrity_validator = (
    SecurityCoreIntegrityValidator()
)
