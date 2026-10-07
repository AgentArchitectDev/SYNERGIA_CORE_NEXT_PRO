#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNERGIA OS
EXECUTION ENVELOPE BUILDER v1.0

Responsabilidad:
    Convertir una intención validada en un ExecutionEnvelope.

Reglas:
    - NO autoriza.
    - NO ejecuta.
    - NO crea ExecutionGrant.
    - NO llama Scheduler.
    - NO llama TaskEngine.
    - NO concede autoridad humana.

La autorización debe ocurrir posteriormente mediante
AuthorizationManager + ExecutionGrant.
"""

from datetime import datetime, timezone
from typing import Any, Dict, Iterable, Optional
from uuid import uuid4

from ai.decision_validation.execution_envelope import ExecutionEnvelope


class ExecutionEnvelopeBuilder:
    """Construye ExecutionEnvelope sin conceder autorización."""

    def build(
        self,
        *,
        original_query: str,
        requested_action: str,
        action_parameters: Optional[Dict[str, Any]],
        execution_scope: Iterable[str],
        proposal_id: str,
        validation_id: str,
        evidence_id: str,
        validator_id: str,
        dvc_status: str,
        safety_status: str = "UNKNOWN",
        security_gate_status: str = "UNKNOWN",
        created_at: Optional[datetime] = None,
    ) -> ExecutionEnvelope:
        now = created_at or datetime.now(timezone.utc)

        return ExecutionEnvelope(
            envelope_id=f"ENV-{uuid4().hex}",
            proposal_id=proposal_id,
            validation_id=validation_id,
            evidence_id=evidence_id,
            validator_id=validator_id,
            original_query=original_query,
            requested_action=requested_action,
            action_parameters=dict(action_parameters or {}),
            execution_scope=set(execution_scope),
            dvc_status=dvc_status,
            safety_status=safety_status,
            authorization_status="UNKNOWN",
            security_gate_status=security_gate_status,
            authorization_id=None,
            execution_grant=False,
            created_at=now,
            expires_at=None,
            revocation_state="UNKNOWN",
            integrity_hash=None,
        )


execution_envelope_builder = ExecutionEnvelopeBuilder()
