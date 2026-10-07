#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Any, Dict

from ai.core.cognitive_router.human_literal_interpretation import HumanLiteralInterpretation


class HumanLiteralEvidenceAdapter:
    """Obtiene evidencia objetiva local sin autorizar ni ejecutar."""

    def __init__(self, project_root=None):
        self.project_root = Path(project_root or Path(__file__).resolve().parents[2])

    def collect(self, interpretation: HumanLiteralInterpretation) -> Dict[str, Any]:
        if not isinstance(interpretation, HumanLiteralInterpretation):
            return {"status": "REJECTED", "reason": "INVALID_INTERPRETATION_TYPE"}

        evidence = {
            "project_root_exists": self.project_root.exists(),
            "project_root": str(self.project_root),
            "runtime_registry_exists": (self.project_root / "ai/core/module_registry.py").exists(),
            "task_engine_exists": (self.project_root / "ai/core/task_engine.py").exists(),
            "security_gate_exists": (self.project_root / "ai/security/execution_security_gate.py").exists(),
            "last_mile_gate_exists": (self.project_root / "ai/security/last_mile_gate.py").exists(),
        }

        evidence["all_required_components_present"] = all(evidence.values())

        return {
            "status": "EVIDENCE",
            "source": "LOCAL_PROJECT_RUNTIME",
            "evidence": evidence,
            "execution_authorized": False,
            "runtime_execution": False,
        }


human_literal_evidence_adapter = HumanLiteralEvidenceAdapter()
