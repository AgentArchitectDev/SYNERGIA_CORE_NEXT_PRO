#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNERGIA OS
DVC v1.0 — INTEGRATION INTERFACE

READ-ONLY / SIMULATION / AUDIT

Esta interfaz:
- recibe Proposal + Validation;
- ejecuta las reglas del contrato;
- genera resultado de auditoría;
- NO autoriza ejecución;
- NO llama Runtime;
- NO modifica Safety.
"""

from typing import Any, Dict

from .schemas import MuseProposal, ValidationResult
from .contract_validator import DecisionValidationContract


class DVCIntegrationInterface:

    def __init__(self):
        self.contract = DecisionValidationContract()

    def evaluate(
        self,
        proposal: MuseProposal,
        validation: ValidationResult,
    ) -> Dict[str, Any]:

        audit = self.contract.audit(
            proposal,
            validation,
        )

        return {
            "status": (
                "APPROVED_FOR_NEXT_LAYER"
                if (
                    audit["proposal"]["status"] == "VALID"
                    and audit["validation"]["status"] == "VALID"
                )
                else "REJECTED"
            ),
            "contract_version": "1.0",
            "audit": audit,

            # INVARIANT DVC:
            "execution_authorized": False,
            "runtime_execution": False,
        }


dvc_integration = DVCIntegrationInterface()
