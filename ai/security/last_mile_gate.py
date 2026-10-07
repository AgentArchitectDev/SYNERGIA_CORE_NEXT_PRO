#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNERGIA OS
LAST-MILE EXECUTION GATE v1.0

Punto final de verificación antes del Runtime.

THINK != VERIFY != AUTHORIZE != EXECUTE

Este componente:
    - NO concede autorización humana.
    - NO crea Execution Grants.
    - NO ejecuta acciones.
    - NO llama modelos.
    - NO modifica DVC.
    - NO modifica Safety.
    - NO reemplaza Security.

FAIL-CLOSED:
    FALSE / UNKNOWN / MISSING / UNVERIFIABLE
    => BLOCKED
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Optional

from ai.decision_validation.execution_envelope import ExecutionEnvelope
from ai.decision_validation.execution_grant import ExecutionGrant
from ai.security.execution_security_gate import ExecutionSecurityGate


class LastMileGate:
    """Enforcement central previo al Runtime."""

    FAIL_CLOSED = True

    def __init__(
        self,
        security_gate: Optional[ExecutionSecurityGate] = None,
    ) -> None:
        self.security_gate = security_gate

    def check(
        self,
        envelope: ExecutionEnvelope,
        execution_name: str = "UNKNOWN",
        requested_scope: Optional[str] = None,
        grant: Optional[ExecutionGrant] = None,
        now: Optional[datetime] = None,
    ) -> Dict[str, Any]:

        if not isinstance(envelope, ExecutionEnvelope):
            return self._block(
                execution_name,
                "ENVELOPE_INVALID_TYPE",
            )

        if grant is None:
            return self._block(execution_name, "EXECUTION_GRANT_MISSING")
        if not isinstance(grant, ExecutionGrant) or not grant.valid(envelope):
            return self._block(execution_name, "EXECUTION_GRANT_INVALID")

        if not envelope.envelope_valid():
            return self._block(
                execution_name,
                "ENVELOPE_INVALID",
            )

        if self.security_gate is not None:
            try:
                security_decision = self.security_gate.check_execution(
                    execution_name=execution_name
                )
            except Exception:
                return self._block(
                    execution_name,
                    "SECURITY_GATE_ERROR",
                )

            if not isinstance(security_decision, dict):
                return self._block(
                    execution_name,
                    "SECURITY_DECISION_INVALID",
                )

            if security_decision.get("status") != "ALLOWED":
                return self._block(
                    execution_name,
                    "SECURITY_GATE_BLOCKED",
                    security_decision,
                )

            if security_decision.get("authorized") is not True:
                return self._block(
                    execution_name,
                    "SECURITY_GATE_NOT_AUTHORIZED",
                    security_decision,
                )


        elif envelope.security_gate_status != "ALLOWED":
            return self._block(
                execution_name,
                "SECURITY_GATE_MISSING",
            )

        try:
            executable = envelope.executable(
                requested_scope=requested_scope,
                now=now,
            )
        except Exception:
            return self._block(
                execution_name,
                "ENVELOPE_EXECUTABILITY_ERROR",
            )

        if not executable:
            return self._block(
                execution_name,
                "ENVELOPE_NOT_EXECUTABLE",
                envelope.audit(
                    requested_scope=requested_scope,
                    now=now,
                ),
            )

        return {
            "status": "EXECUTABLE",
            "execution": execution_name,
            "authorized": False,
            "execution_grant_verified": True,
            "fail_closed": self.FAIL_CLOSED,
            "reason": "LAST_MILE_ALL_CONTROLS_VALID",
            "runtime_execution": False,
        }

    def _block(
        self,
        execution_name: str,
        reason: str,
        details: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:

        decision: Dict[str, Any] = {
            "status": "BLOCKED",
            "execution": execution_name,
            "authorized": False,
            "fail_closed": self.FAIL_CLOSED,
            "reason": reason,
            "runtime_execution": False,
        }

        if details is not None:
            decision["details"] = details

        return decision


last_mile_gate = LastMileGate()
