from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass(frozen=True)
class ExecutionGrant:
    authorization_id: str
    envelope_id: str
    requested_action: str
    action_parameters: Dict[str, Any]
    execution_scope: set
    authorized_by: str
    authorized_at: datetime
    expires_at: datetime
    revocation_state: str = "ACTIVE"

    AUTHORITY = "HUMAN_ADMINISTRATOR"

    def valid(self, envelope) -> bool:
        if envelope is None:
            return False
        if self.authorized_by != self.AUTHORITY:
            return False
        if not self.authorization_id or self.envelope_id != envelope.envelope_id:
            return False
        if self.requested_action != envelope.requested_action:
            return False
        if self.action_parameters != envelope.action_parameters:
            return False
        if self.execution_scope != envelope.execution_scope:
            return False
        if self.revocation_state != "ACTIVE":
            return False
        now = datetime.now(timezone.utc)
        if self.expires_at.tzinfo is None or self.expires_at <= now:
            return False
        if self.authorized_at.tzinfo is None or self.authorized_at > now:
            return False
        return True
