#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNERGIA OS
EXECUTION ENVELOPE v2.0

Puente verificable entre validación/autorización y Runtime.

Este módulo:
    - NO ejecuta acciones.
    - NO llama modelos.
    - NO concede autoridad humana.
    - NO modifica Safety.
    - NO modifica Security.
    - NO llama al Scheduler.

Principio:

    DVC PASS
    AND SAFETY PASS
    AND AUTHORIZATION GRANTED
    AND ENVELOPE VALID
    AND INTEGRITY VALID
    AND NOT EXPIRED
    AND NOT REVOKED
    AND SECURITY GATE ALLOWED
    AND SCOPE VALID
    =
    EXECUTABLE

Fail-closed:
    FALSE / UNKNOWN / MISSING / UNVERIFIABLE
    => NOT_EXECUTABLE
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import hmac
import json
from typing import Any, Dict, Optional, Set


ENVELOPE_VERSION = "2.0"


@dataclass
class ExecutionEnvelope:
    """
    Envelope de ejecución verificable.

    La existencia del objeto NO implica autorización.

    La autorización debe estar explícitamente vinculada mediante:
        authorization_status == "GRANTED"
        authorization_id presente
        execution_grant == True
    """

    envelope_id: str
    proposal_id: str
    validation_id: str
    evidence_id: str
    validator_id: str

    original_query: str
    requested_action: Optional[str]

    action_parameters: Dict[str, Any] = field(default_factory=dict)

    execution_scope: Set[str] = field(default_factory=set)

    dvc_status: str = "UNKNOWN"
    safety_status: str = "UNKNOWN"
    authorization_status: str = "UNKNOWN"
    security_gate_status: str = "UNKNOWN"

    authorization_id: Optional[str] = None
    execution_grant: bool = False

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    expires_at: Optional[datetime] = None

    revocation_state: str = "UNKNOWN"

    integrity_hash: Optional[str] = None

    def _is_non_empty_string(self, value: Any) -> bool:
        return isinstance(value, str) and bool(value.strip())

    @staticmethod
    def _normalize_datetime(value: datetime) -> str:
        """
        Normaliza datetime para representación determinista UTC.
        """

        if not isinstance(value, datetime):
            raise TypeError("DATETIME_REQUIRED")

        if value.tzinfo is None:
            value = value.replace(tzinfo=timezone.utc)

        value = value.astimezone(timezone.utc)

        return value.isoformat()

    def envelope_valid(self) -> bool:
        """
        Valida la estructura mínima del envelope.

        Esta función NO determina autorización.
        """

        required_strings = (
            self.envelope_id,
            self.proposal_id,
            self.validation_id,
            self.evidence_id,
            self.validator_id,
            self.original_query,
        )

        if not all(self._is_non_empty_string(value) for value in required_strings):
            return False

        if self.requested_action is not None:
            if not self._is_non_empty_string(self.requested_action):
                return False

        if not isinstance(self.action_parameters, dict):
            return False

        if not isinstance(self.execution_scope, set):
            return False

        if not all(
            isinstance(item, str) and bool(item.strip())
            for item in self.execution_scope
        ):
            return False

        if self.dvc_status not in {
            "PASS",
            "FAIL",
            "UNKNOWN",
        }:
            return False

        if self.safety_status not in {
            "PASS",
            "BLOCKED",
            "FAIL",
            "UNKNOWN",
        }:
            return False

        if self.authorization_status not in {
            "GRANTED",
            "DENIED",
            "UNKNOWN",
        }:
            return False

        if self.security_gate_status not in {
            "ALLOWED",
            "BLOCKED",
            "UNKNOWN",
        }:
            return False

        if not isinstance(self.execution_grant, bool):
            return False

        if not isinstance(self.created_at, datetime):
            return False

        if self.expires_at is not None:
            if not isinstance(self.expires_at, datetime):
                return False

        if self.revocation_state not in {
            "ACTIVE",
            "REVOKED",
            "UNKNOWN",
        }:
            return False

        if self.integrity_hash is not None:
            if not self._is_non_empty_string(self.integrity_hash):
                return False

        return True

    def authorization_granted(self) -> bool:
        """
        Determina si existe autorización explícita y vinculada.
        """

        return (
            self.authorization_status == "GRANTED"
            and self.execution_grant is True
            and self._is_non_empty_string(self.authorization_id)
        )

    def dvc_pass(self) -> bool:
        return self.dvc_status == "PASS"

    def safety_pass(self) -> bool:
        return self.safety_status == "PASS"

    def security_gate_allowed(self) -> bool:
        return self.security_gate_status == "ALLOWED"

    def is_revoked(self) -> bool:
        return self.revocation_state == "REVOKED"

    def is_expired(self, now: Optional[datetime] = None) -> bool:
        """
        Sin expires_at:
            FAIL-CLOSED

        El envelope se considera expirado/no ejecutable.
        """

        if self.expires_at is None:
            return True

        if now is None:
            now = datetime.now(timezone.utc)

        if not isinstance(now, datetime):
            return True

        if now.tzinfo is None:
            now = now.replace(tzinfo=timezone.utc)

        expires_at = self.expires_at

        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)

        expires_at = expires_at.astimezone(timezone.utc)
        now = now.astimezone(timezone.utc)

        return now >= expires_at

    def scope_allows(self, requested_scope: Optional[str]) -> bool:
        """
        Verifica que el scope solicitado esté explícitamente autorizado.
        """

        if not self.execution_scope:
            return False

        if not self._is_non_empty_string(requested_scope):
            return False

        return requested_scope in self.execution_scope

    def protected_material(self) -> Dict[str, Any]:
        """
        Construye exactamente el material protegido por integridad.

        integrity_hash queda deliberadamente FUERA del material hash.

        El orden lógico de las claves se normaliza mediante JSON
        sort_keys=True en canonical_payload().
        """

        return {
            "envelope_id": self.envelope_id,
            "proposal_id": self.proposal_id,
            "validation_id": self.validation_id,
            "evidence_id": self.evidence_id,
            "validator_id": self.validator_id,
            "requested_action": self.requested_action,
            "action_parameters": self.action_parameters,
            "execution_scope": sorted(self.execution_scope),
            "dvc_status": self.dvc_status,
            "safety_status": self.safety_status,
            "authorization_status": self.authorization_status,
            "created_at": self._normalize_datetime(self.created_at),
            "expires_at": (
                self._normalize_datetime(self.expires_at)
                if self.expires_at is not None
                else None
            ),
            "authorization_id": self.authorization_id,
            "execution_grant": self.execution_grant,
        }

    def canonical_payload(self) -> str:
        """
        Serialización determinista UTF-8 compatible con el contrato 4.102.
        """

        material = self.protected_material()

        return json.dumps(
            material,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )

    def calculate_integrity_hash(self) -> str:
        """
        Calcula SHA-256 del material protegido.
        """

        payload = self.canonical_payload().encode("utf-8")

        return hashlib.sha256(payload).hexdigest()

    def seal(self) -> str:
        """
        Calcula y asigna el integrity_hash.

        No autoriza ni ejecuta.
        """

        self.integrity_hash = self.calculate_integrity_hash()

        return self.integrity_hash

    def integrity_valid(self) -> bool:
        """
        Verifica criptográficamente el hash almacenado.

        Fail-closed:
            hash ausente -> False
            hash incorrecto -> False
        """

        if not self._is_non_empty_string(self.integrity_hash):
            return False

        try:
            expected = self.calculate_integrity_hash()
        except (TypeError, ValueError, OverflowError):
            return False

        return hmac.compare_digest(
            self.integrity_hash,
            expected,
        )

    def executable(
        self,
        requested_scope: Optional[str] = None,
        now: Optional[datetime] = None,
    ) -> bool:
        """
        Determina si el envelope cumple TODAS las condiciones.

        No produce efectos secundarios.
        """

        if not self.envelope_valid():
            return False

        if not self.dvc_pass():
            return False

        if not self.safety_pass():
            return False

        if not self.authorization_granted():
            return False

        if not self.integrity_valid():
            return False

        if self.is_expired(now):
            return False

        if self.is_revoked():
            return False

        if not self.security_gate_allowed():
            return False

        if not self.scope_allows(requested_scope):
            return False

        return True

    def execution_state(
        self,
        requested_scope: Optional[str] = None,
        now: Optional[datetime] = None,
    ) -> str:
        """
        Estado final verificable.
        """

        if self.executable(
            requested_scope=requested_scope,
            now=now,
        ):
            return "EXECUTABLE"

        return "NOT_EXECUTABLE"

    def audit(
        self,
        requested_scope: Optional[str] = None,
        now: Optional[datetime] = None,
    ) -> Dict[str, Any]:
        """
        Genera evidencia estructurada.

        runtime_execution permanece siempre False:
        este componente NO ejecuta acciones.
        """

        return {
            "envelope_version": ENVELOPE_VERSION,
            "envelope_id": self.envelope_id,
            "proposal_id": self.proposal_id,
            "validation_id": self.validation_id,
            "evidence_id": self.evidence_id,
            "validator_id": self.validator_id,
            "dvc_pass": self.dvc_pass(),
            "safety_pass": self.safety_pass(),
            "authorization_granted": self.authorization_granted(),
            "envelope_valid": self.envelope_valid(),
            "integrity_valid": self.integrity_valid(),
            "expired": self.is_expired(now),
            "revoked": self.is_revoked(),
            "security_gate_allowed": self.security_gate_allowed(),
            "scope_allowed": self.scope_allows(requested_scope),
            "execution_grant": self.execution_grant,
            "execution_state": self.execution_state(
                requested_scope=requested_scope,
                now=now,
            ),
            "runtime_execution": False,
        }
