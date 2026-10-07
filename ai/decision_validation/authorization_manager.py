"""
SYNERGIA OS
Authorization Manager

Responsabilidad:
    Crear autorizaciones formales emitidas exclusivamente por
    HUMAN_ADMINISTRATOR.

Este componente NO ejecuta acciones.
Este componente NO reemplaza DVC, Safety, Security Gate
ni LastMileGate.

Produce ExecutionGrant.
"""

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional
from uuid import uuid4

from .execution_grant import ExecutionGrant


class AuthorizationManager:
    """
    Productor controlado de ExecutionGrant.

    PRINCIPIO:

        HUMAN_ADMINISTRATOR
                ↓
        AuthorizationManager
                ↓
        ExecutionGrant

    No ejecuta Runtime.
    """

    AUTHORITY = ExecutionGrant.AUTHORITY
    DEFAULT_EXPIRATION_SECONDS = 300

    def __init__(self):
        self.executions = 0
        self.authorizations = 0
        self.last_authorization = None

    def authorize(
        self,
        envelope,
        authorized_by: str,
        expiration_seconds: int = DEFAULT_EXPIRATION_SECONDS,
    ) -> ExecutionGrant:
        """
        Crea un ExecutionGrant formal.

        La autorización requiere:

        - envelope válido como objeto;
        - autoridad HUMAN_ADMINISTRATOR;
        - requested_action;
        - action_parameters;
        - execution_scope;
        - expiración positiva.

        Este método NO ejecuta la acción.
        """

        self.executions += 1

        if envelope is None:
            raise ValueError("AUTHORIZATION_ENVELOPE_MISSING")

        if authorized_by != self.AUTHORITY:
            raise PermissionError("AUTHORIZATION_AUTHORITY_INVALID")

        if not getattr(envelope, "envelope_id", None):
            raise ValueError("AUTHORIZATION_ENVELOPE_ID_MISSING")

        if not getattr(envelope, "requested_action", None):
            raise ValueError("AUTHORIZATION_ACTION_MISSING")

        if getattr(envelope, "action_parameters", None) is None:
            raise ValueError("AUTHORIZATION_PARAMETERS_MISSING")

        execution_scope = getattr(envelope, "execution_scope", None)

        if execution_scope is None:
            raise ValueError("AUTHORIZATION_SCOPE_MISSING")

        if not isinstance(expiration_seconds, int):
            raise TypeError("AUTHORIZATION_EXPIRATION_INVALID")

        if expiration_seconds <= 0:
            raise ValueError("AUTHORIZATION_EXPIRATION_INVALID")

        now = datetime.now(timezone.utc)
        expires_at = now + timedelta(seconds=expiration_seconds)

        authorization_id = f"AUTH-{uuid4().hex}"

        grant = ExecutionGrant(
            authorization_id=authorization_id,
            envelope_id=envelope.envelope_id,
            requested_action=envelope.requested_action,
            action_parameters=dict(envelope.action_parameters),
            execution_scope=set(execution_scope),
            authorized_by=self.AUTHORITY,
            authorized_at=now,
            expires_at=expires_at,
            revocation_state="ACTIVE",
        )

        self.authorizations += 1
        self.last_authorization = grant

        return grant

    def revoke(self, grant: ExecutionGrant) -> ExecutionGrant:
        """
        Revoca una autorización existente.

        ExecutionGrant es frozen, por lo que se genera una nueva
        instancia con estado REVOKED.
        """

        if not isinstance(grant, ExecutionGrant):
            raise TypeError("AUTHORIZATION_GRANT_INVALID")

        return ExecutionGrant(
            authorization_id=grant.authorization_id,
            envelope_id=grant.envelope_id,
            requested_action=grant.requested_action,
            action_parameters=dict(grant.action_parameters),
            execution_scope=set(grant.execution_scope),
            authorized_by=grant.authorized_by,
            authorized_at=grant.authorized_at,
            expires_at=grant.expires_at,
            revocation_state="REVOKED",
        )

    def status(self) -> Dict[str, Any]:
        return {
            "component": "AuthorizationManager",
            "authority": self.AUTHORITY,
            "executions": self.executions,
            "authorizations": self.authorizations,
            "last_authorization_id": (
                self.last_authorization.authorization_id
                if self.last_authorization
                else None
            ),
        }


authorization_manager = AuthorizationManager()
