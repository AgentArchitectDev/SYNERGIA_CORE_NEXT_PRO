#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNERGIA OS
DECISION & VALIDATION CONTRACT v1.0
CONTRACT VALIDATOR

Modo: READ-ONLY / SIMULATION / AUDIT
"""

from typing import Any, Dict

from .schemas import MuseProposal, ValidationResult


class DecisionValidationContract:

    VERSION = "1.0"

    def validate_proposal(
        self,
        proposal: MuseProposal,
    ) -> Dict[str, Any]:

        if not isinstance(proposal, MuseProposal):
            return {
                "status": "REJECTED",
                "reason": "INVALID_PROPOSAL_TYPE",
            }

        if not proposal.is_valid():
            return {
                "status": "REJECTED",
                "reason": "INVALID_PROPOSAL_STRUCTURE",
            }

        return {
            "status": "VALID",
            "contract_version": self.VERSION,
        }

    def validate_result(
        self,
        validation: ValidationResult,
    ) -> Dict[str, Any]:

        if not isinstance(validation, ValidationResult):
            return {
                "status": "REJECTED",
                "reason": "INVALID_VALIDATION_TYPE",
            }

        if not validation.is_valid():
            return {
                "status": "REJECTED",
                "reason": "INVALID_VALIDATION_STRUCTURE",
            }

        if validation.decision != "APPROVED":
            return {
                "status": "REJECTED",
                "reason": "VALIDATION_REJECTED",
            }

        if not validation.can_pass_validation():
            return {
                "status": "REJECTED",
                "reason": "VALIDATION_CONDITIONS_FAILED",
            }

        return {
            "status": "VALID",
            "contract_version": self.VERSION,
        }

    def audit(
        self,
        proposal: MuseProposal,
        validation: ValidationResult,
    ) -> Dict[str, Any]:

        proposal_check = self.validate_proposal(proposal)
        validation_check = self.validate_result(validation)

        return {
            "contract_version": self.VERSION,
            "mode": "READ_ONLY/SIMULATION/AUDIT",
            "proposal": proposal_check,
            "validation": validation_check,

            # Contract invariant:
            # validation never grants execution authority.
            "execution_authorized": False,
            "runtime_execution": False,
        }


decision_validation_contract = DecisionValidationContract()
