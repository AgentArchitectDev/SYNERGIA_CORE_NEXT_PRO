#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SYNERGIA OS
V8.71 — VERIFICATION BRIDGE

Transforma una HumanLiteralInterpretation en una MuseProposal.

INVARIANTES:
- INTERPRETACIÓN != PROPUESTA
- PROPUESTA != VERIFICACIÓN
- VERIFICACIÓN != AUTORIZACIÓN
- NO crea ExecutionEnvelope.
- NO crea ExecutionGrant.
- NO autoriza.
- NO ejecuta.
- FAIL-CLOSED cuando la intención operacional no puede determinarse.
"""

from typing import Any, Dict

from ai.core.cognitive_router.human_literal_interpretation import (
    HumanLiteralInterpretation,
)
from ai.decision_validation.schemas import MuseProposal


class VerificationBridge:
    """
    Puente explícito entre semántica cognitiva y propuesta verificable.

    La resolución operacional es deliberadamente limitada:
    solo objetivos canónicos conocidos producen una acción propuesta.
    """

    OBJECTIVE_TO_ACTION = {
        "create": "CREATE",
        "improve": "IMPROVE",
        "automate": "AUTOMATE",
        "analyze": "ANALYZE",
        "transform": "TRANSFORM",
        "research": "RESEARCH",
    }

    def build_proposal(
        self,
        interpretation: HumanLiteralInterpretation,
    ) -> MuseProposal:

        if not isinstance(
            interpretation,
            HumanLiteralInterpretation,
        ):
            return MuseProposal(
                status="PROPOSAL",
                reasoning_summary="INVALID_INTERPRETATION_TYPE",
                risk_level="CRITICAL",
            )

        objective = interpretation.objective.strip().lower()
        requested_action = self.OBJECTIVE_TO_ACTION.get(objective)

        if requested_action is None:
            return MuseProposal(
                status="PROPOSAL",
                answer="",
                reasoning_summary="REQUESTED_ACTION_UNRESOLVED",
                evidence=[],
                requested_action=None,
                action_parameters={},
                risk_level="HIGH",
            )

        action_parameters: Dict[str, Any] = {
            "request": interpretation.request,
            "scope": interpretation.scope,
            "origin": interpretation.origin,
            "primary_intent": interpretation.primary_intent,
        }

        return MuseProposal(
            status="PROPOSAL",
            answer=(
                f"Propuesta de acción: {requested_action}"
            ),
            reasoning_summary=(
                "Acción propuesta a partir del objetivo canónico "
                "de HumanLiteralInterpretation."
            ),
            evidence=[
                {
                    "source": "HumanLiteralInterpretation",
                    "request": interpretation.request,
                    "scope": interpretation.scope,
                    "objective": interpretation.objective,
                    "origin": interpretation.origin,
                    "primary_intent": interpretation.primary_intent,
                }
            ],
            requested_action=requested_action,
            action_parameters=action_parameters,
            risk_level="LOW",
        )


verification_bridge = VerificationBridge()
