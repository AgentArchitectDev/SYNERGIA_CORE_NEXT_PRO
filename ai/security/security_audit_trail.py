#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNERGIA — SECURITY AUDIT TRAIL

STAGE 6.3.15.7.11.3-S5.8-A

Purpose:

Provide a passive and auditable security event trail.

IMPORTANT:

This module records security events.

It does NOT:

- grant authority
- revoke authority
- activate security controls
- deactivate security controls
- modify security controls
- modify the Sovereign Security Core
- modify the canonical security specification
- modify node identity
- authorize autonomous components
- create sovereign authority
- bypass security validation

AUDIT TRAIL RECORDING != SECURITY AUTHORITY
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List
import json
import platform
import socket


class SecurityAuditTrail:

    MODULE = "SECURITY_AUDIT_TRAIL"

    CANONICAL_AUTHORITY = "HUMAN_ADMINISTRATOR"
    CANONICAL_DIRECTION = "ADMIN_TO_SYNERGIA_ONLY"
    CANONICAL_AUTONOMOUS_SECURITY_AUTHORITY = "ZERO"

    AUDIT_PATH = Path(
        "docs/SECURITY/AUDIT/security_audit_trail.jsonl"
    )

    def __init__(self) -> None:
        self.last_event: Dict[str, Any] | None = None

        print("[SECURITY AUDIT TRAIL READY]")

    def status(self) -> Dict[str, Any]:

        return {
            "module": self.MODULE,
            "loaded": True,
            "authority": self.CANONICAL_AUTHORITY,
            "direction": self.CANONICAL_DIRECTION,
            "autonomous_security_authority":
                self.CANONICAL_AUTONOMOUS_SECURITY_AUTHORITY,
            "audit_path": str(self.AUDIT_PATH),
            "recording_only": True,
            "grants_authority": False,
            "autonomous_access": False,
            "secret_backdoor": False,
            "last_event": self.last_event,
        }

    def record(
        self,
        event: str,
        stage: str,
        status: str = "VALIDATED",
        details: Dict[str, Any] | None = None,
    ) -> Dict[str, Any]:

        record: Dict[str, Any] = {
            "timestamp":
                datetime.now(timezone.utc).isoformat(),
            "stage": stage,
            "event": event,
            "authority":
                self.CANONICAL_AUTHORITY,
            "direction":
                self.CANONICAL_DIRECTION,
            "autonomous_security_authority":
                self.CANONICAL_AUTONOMOUS_SECURITY_AUTHORITY,
            "node":
                socket.gethostname(),
            "platform":
                platform.system(),
            "status":
                status,
            "audit_only":
                True,
            "grants_authority":
                False,
            "autonomous_access":
                False,
            "secret_backdoor":
                False,
        }

        if details:
            record["details"] = details

        self.AUDIT_PATH.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with self.AUDIT_PATH.open(
            "a",
            encoding="utf-8",
        ) as handle:

            handle.write(
                json.dumps(
                    record,
                    ensure_ascii=False,
                    sort_keys=True,
                )
            )

            handle.write("\n")

        self.last_event = record

        return record

    def read_events(self) -> List[Dict[str, Any]]:

        if not self.AUDIT_PATH.exists():
            return []

        events: List[Dict[str, Any]] = []

        with self.AUDIT_PATH.open(
            "r",
            encoding="utf-8",
        ) as handle:

            for line in handle:

                line = line.strip()

                if not line:
                    continue

                events.append(
                    json.loads(line)
                )

        return events


security_audit_trail = SecurityAuditTrail()
