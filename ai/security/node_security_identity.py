#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNERGIA — NODE SECURITY IDENTITY

STAGE 6.3.15.7.11.3-S5.5-A

Purpose:

Define the security identity of an authorized SYNERGIA node.

This module does NOT:

- grant sovereign authority
- activate security controls
- modify security rules
- modify the router
- modify autonomous execution
- redefine administrator authority

It only describes and validates node security identity.

The canonical security specification remains authoritative.
"""

from pathlib import Path
import hashlib
import platform
import socket


class NodeSecurityIdentity:

    SPEC_PATH = Path(
        "docs/SECURITY/SOVEREIGN_SECURITY_SPEC.md"
    )

    AUTHORITY = "HUMAN_ADMINISTRATOR"

    DIRECTION = "ADMIN_TO_SYNERGIA_ONLY"

    AUTONOMOUS_SECURITY_AUTHORITY = "ZERO"

    SECRET_BACKDOOR = False

    AUTONOMOUS_ACCESS = False

    def __init__(self, node_name=None):

        self.node_name = (
            node_name
            if node_name
            else socket.gethostname()
        )

        self.last_validation = None

        print("[NODE SECURITY IDENTITY READY]")

    def specification_hash(self):

        if not self.SPEC_PATH.exists():

            return None

        data = self.SPEC_PATH.read_bytes()

        return hashlib.sha256(data).hexdigest()

    def status(self):

        return {
            "module":
                "NODE_SECURITY_IDENTITY",

            "loaded":
                True,

            "node":
                self.node_name,

            "authority":
                self.AUTHORITY,

            "direction":
                self.DIRECTION,

            "autonomous_security_authority":
                self.AUTONOMOUS_SECURITY_AUTHORITY,

            "secret_backdoor":
                self.SECRET_BACKDOOR,

            "autonomous_access":
                self.AUTONOMOUS_ACCESS,

            "specification":
                str(self.SPEC_PATH),

            "specification_hash":
                self.specification_hash(),

            "platform":
                platform.system(),

            "python":
                platform.python_version(),
        }

    def validate(self, expected_hash=None):

        current_hash = self.specification_hash()

        if current_hash is None:

            result = {
                "status": "INVALID",
                "valid": False,
                "reason":
                    "SECURITY_SPECIFICATION_MISSING",
                "node":
                    self.node_name,
            }

            self.last_validation = result

            return result

        if expected_hash is not None:

            if current_hash != expected_hash:

                result = {
                    "status": "INVALID",
                    "valid": False,
                    "reason":
                        "SECURITY_SPECIFICATION_HASH_MISMATCH",
                    "node":
                        self.node_name,
                    "expected_hash":
                        expected_hash,
                    "actual_hash":
                        current_hash,
                }

                self.last_validation = result

                return result

        result = {
            "status": "VALID",
            "valid": True,
            "node":
                self.node_name,
            "authority":
                self.AUTHORITY,
            "direction":
                self.DIRECTION,
            "autonomous_security_authority":
                self.AUTONOMOUS_SECURITY_AUTHORITY,
            "specification_hash":
                current_hash,
        }

        self.last_validation = result

        return result


node_security_identity = NodeSecurityIdentity()
