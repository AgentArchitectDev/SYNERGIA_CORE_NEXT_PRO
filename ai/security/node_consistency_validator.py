#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNERGIA — NODE CONSISTENCY VALIDATOR

STAGE 6.3.15.7.11.3-S5.5-C

Purpose:

Validate that an authorized SYNERGIA node conforms to the
canonical Sovereign Security Specification.

This validator:

- does NOT grant authority
- does NOT activate security controls
- does NOT modify nodes
- does NOT modify the Router
- does NOT modify autonomous execution
- does NOT redefine administrator authority

It only validates consistency.

Canonical authority remains:

HUMAN_ADMINISTRATOR

Direction:

ADMIN_TO_SYNERGIA_ONLY
"""

from pathlib import Path
import hashlib
import json


class NodeConsistencyValidator:

    SPEC_PATH = Path(
        "docs/SECURITY/SOVEREIGN_SECURITY_SPEC.md"
    )

    NODES_PATH = Path(
        "docs/SECURITY/NODES"
    )

    CANONICAL_AUTHORITY = (
        "HUMAN_ADMINISTRATOR"
    )

    CANONICAL_DIRECTION = (
        "ADMIN_TO_SYNERGIA_ONLY"
    )

    CANONICAL_AUTONOMOUS_AUTHORITY = (
        "ZERO"
    )

    EXPECTED_FLAGS = {
        "secret_backdoor": False,
        "autonomous_access": False,
    }

    def __init__(self):

        self.last_validation = None

        print(
            "[NODE CONSISTENCY VALIDATOR READY]"
        )

    def specification_hash(self):

        if not self.SPEC_PATH.exists():

            return None

        return hashlib.sha256(
            self.SPEC_PATH.read_bytes()
        ).hexdigest()

    def validate_identity(self, identity):

        errors = []

        current_hash = (
            self.specification_hash()
        )

        if current_hash is None:

            errors.append(
                "SECURITY_SPECIFICATION_MISSING"
            )

        if identity.get("authority") != (
            self.CANONICAL_AUTHORITY
        ):

            errors.append(
                "INVALID_AUTHORITY"
            )

        if identity.get("direction") != (
            self.CANONICAL_DIRECTION
        ):

            errors.append(
                "INVALID_DIRECTION"
            )

        if identity.get(
            "autonomous_security_authority"
        ) != self.CANONICAL_AUTONOMOUS_AUTHORITY:

            errors.append(
                "AUTONOMOUS_SECURITY_AUTHORITY_NOT_ZERO"
            )

        for key, expected in (
            self.EXPECTED_FLAGS.items()
        ):

            if identity.get(key) != expected:

                errors.append(
                    f"INVALID_{key.upper()}"
                )

        if current_hash is not None:

            if identity.get(
                "security_specification_sha256"
            ) != current_hash:

                errors.append(
                    "SECURITY_SPECIFICATION_HASH_MISMATCH"
                )

        if not identity.get("node"):

            errors.append(
                "NODE_IDENTITY_MISSING"
            )

        if errors:

            return {
                "status": "INVALID",
                "valid": False,
                "node": identity.get("node"),
                "errors": errors,
            }

        return {
            "status": "VALID",
            "valid": True,
            "node": identity.get("node"),
            "authority":
                identity.get("authority"),
            "direction":
                identity.get("direction"),
            "autonomous_security_authority":
                identity.get(
                    "autonomous_security_authority"
                ),
            "security_specification_sha256":
                current_hash,
        }

    def validate_file(self, path):

        path = Path(path)

        if not path.exists():

            return {
                "status": "INVALID",
                "valid": False,
                "reason":
                    "NODE_IDENTITY_FILE_MISSING",
                "file": str(path),
            }

        try:

            identity = json.loads(
                path.read_text(
                    encoding="utf-8"
                )
            )

        except Exception as exc:

            return {
                "status": "INVALID",
                "valid": False,
                "reason":
                    "NODE_IDENTITY_FILE_INVALID",
                "file": str(path),
                "error": str(exc),
            }

        result = self.validate_identity(
            identity
        )

        result["file"] = str(path)

        return result

    def validate_all(self):

        if not self.NODES_PATH.exists():

            result = {
                "status": "INVALID",
                "valid": False,
                "reason":
                    "NODES_DIRECTORY_MISSING",
                "nodes": [],
            }

            self.last_validation = result

            return result

        files = sorted(
            self.NODES_PATH.glob(
                "*_SECURITY_IDENTITY.json"
            )
        )

        if not files:

            result = {
                "status": "INVALID",
                "valid": False,
                "reason":
                    "NO_NODE_IDENTITIES_FOUND",
                "nodes": [],
            }

            self.last_validation = result

            return result

        results = []

        for path in files:

            results.append(
                self.validate_file(path)
            )

        invalid = [
            item
            for item in results
            if not item["valid"]
        ]

        result = {
            "status":
                "VALID"
                if not invalid
                else "INVALID",

            "valid":
                not invalid,

            "canonical_authority":
                self.CANONICAL_AUTHORITY,

            "canonical_direction":
                self.CANONICAL_DIRECTION,

            "canonical_autonomous_security_authority":
                self.CANONICAL_AUTONOMOUS_AUTHORITY,

            "canonical_specification_sha256":
                self.specification_hash(),

            "nodes_checked":
                len(results),

            "nodes_invalid":
                len(invalid),

            "results":
                results,
        }

        self.last_validation = result

        return result

    def status(self):

        return {
            "module":
                "NODE_CONSISTENCY_VALIDATOR",

            "loaded":
                True,

            "canonical_authority":
                self.CANONICAL_AUTHORITY,

            "canonical_direction":
                self.CANONICAL_DIRECTION,

            "canonical_autonomous_security_authority":
                self.CANONICAL_AUTONOMOUS_AUTHORITY,

            "specification":
                str(self.SPEC_PATH),

            "nodes_directory":
                str(self.NODES_PATH),

            "last_validation":
                self.last_validation,
        }


node_consistency_validator = (
    NodeConsistencyValidator()
)
