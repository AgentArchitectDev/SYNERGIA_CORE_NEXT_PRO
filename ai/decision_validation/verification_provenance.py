#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
import hashlib
import json
from uuid import uuid4

from ai.decision_validation.schemas import MuseProposal, ValidationResult

@dataclass(frozen=True)
class VerificationProvenance:
    proposal_id: str
    validation_id: str
    evidence_id: str
    validator_id: str


class VerificationProvenanceBuilder:
    VALIDATOR_ID = "SYNERGIA_V8_71_HUMAN_LITERAL_VALIDATOR"

    def build(self, proposal: MuseProposal, validation: ValidationResult) -> VerificationProvenance:

        if not isinstance(proposal, MuseProposal):
            raise TypeError("proposal must be MuseProposal")

        if not isinstance(validation, ValidationResult):
            raise TypeError("validation must be ValidationResult")

        if not proposal.evidence:
            raise ValueError("EVIDENCE_MISSING")

        proposal_payload = {
            "requested_action": proposal.requested_action,
            "action_parameters": proposal.action_parameters,
            "risk_level": proposal.risk_level,
        }

        evidence_payload = {
            "evidence": proposal.evidence,
            "validation": {
                "decision": validation.decision,
                "reason": validation.reason,
                "confidence": validation.confidence,
            },
        }

        proposal_digest = hashlib.sha256(
            json.dumps(
                proposal_payload,
                sort_keys=True,
                ensure_ascii=False,
            ).encode("utf-8")
        ).hexdigest()

        evidence_digest = hashlib.sha256(
            json.dumps(
                evidence_payload,
                sort_keys=True,
                ensure_ascii=False,
            ).encode("utf-8")
        ).hexdigest()

        return VerificationProvenance(
            proposal_id=f"PROP-{proposal_digest}",
            validation_id=f"VAL-{uuid4().hex}",
            evidence_id=f"EVID-{evidence_digest}",
            validator_id=self.VALIDATOR_ID,
        )


verification_provenance_builder = VerificationProvenanceBuilder()
