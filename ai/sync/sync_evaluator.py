"""
============================================================
SYNERGIA OS — SYNC EVALUATOR
============================================================
SYNERGIA SYNC — Mecanismo de Control de Coherencia

Responsabilidad:
    Evaluar las observaciones producidas por SyncComparator.

Estados oficiales:
    SYNC_PASS
    SYNC_PENDING
    SYNC_CONFLICT
    SYNC_UNKNOWN

NO:
    - modifica archivos
    - corrige inconsistencias
    - realiza commits
    - realiza push
    - autoriza ejecución
    - concede permisos
    - ejecuta agentes

Principio:
    COLLECT ≠ COMPARE ≠ EVALUATE ≠ AUTHORIZE ≠ EXECUTE
"""

from typing import Any, Dict


SYNC_PASS = "SYNC_PASS"
SYNC_PENDING = "SYNC_PENDING"
SYNC_CONFLICT = "SYNC_CONFLICT"
SYNC_UNKNOWN = "SYNC_UNKNOWN"


class SyncEvaluator:
    """Evaluador conservador del estado de coherencia."""

    def evaluate(
        self,
        comparison: Dict[str, Any],
    ) -> Dict[str, Any]:
        if not comparison:
            return {
                "status": SYNC_UNKNOWN,
                "reason": "comparison_missing",
            }

        required_checks = (
            "repository",
            "master",
            "git",
            "checkpoints",
            "security",
        )

        missing = [
            name
            for name in required_checks
            if name not in comparison
        ]

        if missing:
            return {
                "status": SYNC_UNKNOWN,
                "reason": "comparison_sections_missing",
                "missing": missing,
            }

        repository = comparison["repository"]
        master = comparison["master"]
        git = comparison["git"]
        checkpoints = comparison["checkpoints"]
        security = comparison["security"]

        if (
            repository.get("status") == "UNKNOWN"
            or master.get("status") == "UNKNOWN"
            or git.get("status") == "UNKNOWN"
            or checkpoints.get("status") == "UNKNOWN"
            or security.get("status") == "UNKNOWN"
        ):
            return {
                "status": SYNC_UNKNOWN,
                "reason": "insufficient_evidence",
            }

        if (
            repository.get("status") != "PASS"
            or master.get("status") not in {"OBSERVED", "PASS"}
            or git.get("status") not in {"OBSERVED", "PASS"}
            or checkpoints.get("status") not in {
                "OBSERVED",
                "PASS",
            }
            or security.get("status") == "CONFLICT"
        ):
            return {
                "status": SYNC_CONFLICT,
                "reason": "explicit_evidence_inconsistency",
            }

        git_status_lines = git.get("status_lines", 0)

        if git_status_lines > 0:
            return {
                "status": SYNC_PENDING,
                "reason": "uncommitted_repository_changes",
                "git_status_lines": git_status_lines,
            }

        return {
            "status": SYNC_PASS,
            "reason": "required_evidence_consistent",
        }


sync_evaluator = SyncEvaluator()
