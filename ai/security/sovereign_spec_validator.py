#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
SYNERGIA — SOVEREIGN SECURITY SPEC VALIDATOR

STAGE 6.3.15.7.11.3-S5.3-A

Purpose:

Validate the canonical Sovereign Security Specification.

This validator is intentionally:

- visible
- documented
- auditable
- deterministic

It does NOT grant authority.

It does NOT activate security controls.

It does NOT modify the security specification.

It only validates the specification.
"""

from pathlib import Path
import hashlib


class SovereignSpecValidator:

    SPEC_PATH = Path(
        "docs/SECURITY/SOVEREIGN_SECURITY_SPEC.md"
    )

    REQUIRED_SECTIONS = [
        "1. SOVEREIGN AUTHORITY",
        "2. FORBIDDEN DIRECTION",
        "3. PROTECTED COMPONENTS",
        "4. AUTONOMOUS RESTRICTIONS",
        "5. VISIBILITY",
        "6. EMERGENCY PRINCIPLES",
        "7. SECURITY INTEGRITY",
        "8. NODE CONSISTENCY",
        "9. NO HIDDEN AUTHORITY",
        "10. PRINCIPLE",
        "11. ADMINISTRATIVE PRINCIPLE",
    ]

    REQUIRED_RULES = [
        "HUMAN ADMINISTRATOR",
        "ADMIN -> SYNERGIA ONLY",
        "SYNERGIA -> ADMIN",
        "SOVEREIGN_ESCAPE",
        "EMERGENCY_STOP",
        "AUTONOMY_OFF",
        "MASTER_SECURITY_LOCK",
        "SOVEREIGN_SECURITY_CORE",
        "ZERO sovereign authority",
        "CAPABILITY != AUTHORITY",
        "INTELLIGENCE != SOVEREIGNTY",
        "AUTONOMY != ADMINISTRATOR",
    ]

    def __init__(self, spec_path=None):

        self.spec_path = Path(
            spec_path
            if spec_path
            else self.SPEC_PATH
        )

        self.last_validation = None

        print(
            "[SOVEREIGN SPEC VALIDATOR READY]"
        )

    # =====================================================
    # HASH
    # =====================================================

    def calculate_hash(self, content):

        return hashlib.sha256(
            content.encode("utf-8")
        ).hexdigest()

    # =====================================================
    # VALIDATE
    # =====================================================

    def validate(self):

        if not self.spec_path.exists():

            result = {
                "status": "INVALID",
                "valid": False,
                "reason": "SPECIFICATION_NOT_FOUND",
                "path": str(self.spec_path),
            }

            self.last_validation = result

            return result

        content = self.spec_path.read_text(
            encoding="utf-8"
        )

        missing_sections = [
            section
            for section in self.REQUIRED_SECTIONS
            if section not in content
        ]

        missing_rules = [
            rule
            for rule in self.REQUIRED_RULES
            if rule not in content
        ]

        file_hash = self.calculate_hash(
            content
        )

        valid = (
            len(missing_sections) == 0
            and len(missing_rules) == 0
        )

        result = {

            "status":
                "VALID"
                if valid
                else "INVALID",

            "valid":
                valid,

            "module":
                "SOVEREIGN_SPEC_VALIDATOR",

            "specification":
                str(self.spec_path),

            "sections_required":
                len(self.REQUIRED_SECTIONS),

            "sections_missing":
                missing_sections,

            "rules_required":
                len(self.REQUIRED_RULES),

            "rules_missing":
                missing_rules,

            "sha256":
                file_hash,

        }

        self.last_validation = result

        return result

    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        return {

            "module":
                "SOVEREIGN_SPEC_VALIDATOR",

            "loaded":
                True,

            "specification":
                str(self.spec_path),

            "last_validation":
                self.last_validation,

        }


sovereign_spec_validator = (
    SovereignSpecValidator()
)
