#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNERGIA OS
DECISION & VALIDATION CONTRACT v1.0
SCHEMAS

Modo:
    READ-ONLY / SIMULATION / AUDIT

Autoridad:
    Este módulo NO autoriza ni ejecuta acciones.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class MuseProposal:
    status: str = "PROPOSAL"
    answer: str = ""
    reasoning_summary: str = ""
    evidence: List[Any] = field(default_factory=list)
    requested_action: Optional[str] = None
    action_parameters: Dict[str, Any] = field(default_factory=dict)
    risk_level: str = "LOW"

    def is_valid(self) -> bool:
        return (
            self.status == "PROPOSAL"
            and isinstance(self.answer, str)
            and isinstance(self.reasoning_summary, str)
            and isinstance(self.evidence, list)
            and isinstance(self.action_parameters, dict)
            and self.risk_level in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
        )


@dataclass
class ValidationResult:
    decision: str = "REJECTED"
    grounded: bool = False
    instruction_compliant: bool = False
    factual_consistency: bool = False
    execution_allowed: bool = False
    hallucination_detected: bool = True
    confidence: float = 0.0
    reason: str = ""

    def is_valid(self) -> bool:
        return (
            self.decision in {"APPROVED", "REJECTED"}
            and isinstance(self.grounded, bool)
            and isinstance(self.instruction_compliant, bool)
            and isinstance(self.factual_consistency, bool)
            and isinstance(self.execution_allowed, bool)
            and isinstance(self.hallucination_detected, bool)
            and 0.0 <= self.confidence <= 1.0
            and isinstance(self.reason, str)
        )

    def can_pass_validation(self) -> bool:
        return (
            self.is_valid()
            and self.decision == "APPROVED"
            and self.grounded
            and self.instruction_compliant
            and self.factual_consistency
            and self.execution_allowed
            and not self.hallucination_detected
        )


@dataclass
class DecisionValidationEnvelope:
    original_query: str
    context: Any
    memory: Any
    muse_proposal: MuseProposal
    validation: ValidationResult
    requested_action: Optional[str] = None
    execution_policy: Dict[str, Any] = field(default_factory=dict)

    def execution_authorized(self) -> bool:
        # Contract v1.0:
        # LLM validation != authorization.
        # Safety Layer must authorize separately.
        return False

    def audit_summary(self) -> Dict[str, Any]:
        return {
            "contract_version": "1.0",
            "mode": "READ_ONLY/SIMULATION/AUDIT",
            "proposal_valid": self.muse_proposal.is_valid(),
            "validation_valid": self.validation.is_valid(),
            "validation_passed": self.validation.can_pass_validation(),
            "execution_authorized": False,
            "runtime_execution": False,
        }
