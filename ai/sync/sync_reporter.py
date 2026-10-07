"""
============================================================
SYNERGIA OS — SYNC REPORTER
============================================================
SYNERGIA SYNC — Mecanismo de Control de Coherencia

Responsabilidad:
    Presentar el diagnóstico producido por SYNERGIA SYNC.

NO:
    - recopila evidencia
    - compara directamente archivos
    - modifica archivos
    - corrige inconsistencias
    - realiza commits
    - realiza push
    - autoriza ejecución
    - concede permisos

Principio:
    COLLECT ≠ COMPARE ≠ EVALUATE ≠ REPORT ≠ AUTHORIZE ≠ EXECUTE
"""

from typing import Any, Dict


class SyncReporter:
    """Presentador del estado estructurado de SYNERGIA SYNC."""

    def to_dict(
        self,
        evidence: Dict[str, Any],
        comparison: Dict[str, Any],
        evaluation: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Construye una representación estructurada del diagnóstico."""

        return {
            "system": "SYNERGIA SYNC",
            "component": "SyncReporter",
            "mode": "READ_ONLY",
            "status": evaluation.get("status"),
            "reason": evaluation.get("reason"),
            "master": {
                "reference": comparison["master"].get("reference"),
                "next": comparison["master"].get("next"),
                "date": comparison["master"].get("date"),
                "state": comparison["master"].get("state"),
            },
            "repository": {
                "path": evidence["repository"].get("path"),
                "exists": evidence["repository"].get("exists"),
                "is_git_repository": evidence["repository"].get(
                    "is_git_repository"
                ),
            },
            "git": {
                "branch": comparison["git"].get("branch"),
                "head": comparison["git"].get("head"),
                "status_lines": comparison["git"].get(
                    "status_lines"
                ),
            },
            "checkpoints": {
                "count": comparison["checkpoints"].get("count"),
            },
            "security": {
                "status": comparison["security"].get("status"),
                "node_valid": comparison["security"].get(
                    "node_valid"
                ),
                "controls_valid": comparison["security"].get(
                    "controls_valid"
                ),
                "core_valid": comparison["security"].get(
                    "core_valid"
                ),
            },
        }

    def to_text(
        self,
        evidence: Dict[str, Any],
        comparison: Dict[str, Any],
        evaluation: Dict[str, Any],
    ) -> str:
        """Genera un informe legible para operadores humanos."""

        report = self.to_dict(
            evidence,
            comparison,
            evaluation,
        )

        master = report["master"]
        repository = report["repository"]
        git = report["git"]
        checkpoints = report["checkpoints"]
        security = report["security"]

        return "\n".join(
            [
                "===== SYNERGIA SYNC =====",
                f"STATUS: {report['status']}",
                f"REASON: {report['reason']}",
                "",
                "--- MASTER ---",
                f"REFERENCE: {master['reference']}",
                f"NEXT: {master['next']}",
                f"DATE: {master['date']}",
                f"STATE: {master['state']}",
                "",
                "--- REPOSITORY ---",
                f"PATH: {repository['path']}",
                f"EXISTS: {repository['exists']}",
                f"IS_GIT_REPOSITORY: "
                f"{repository['is_git_repository']}",
                "",
                "--- GIT ---",
                f"BRANCH: {git['branch']}",
                f"HEAD: {git['head']}",
                f"STATUS_LINES: {git['status_lines']}",
                "",
                "--- CHECKPOINTS ---",
                f"COUNT: {checkpoints['count']}",
                "",
                "--- SECURITY ---",
                f"STATUS: {security['status']}",
                f"NODE_VALID: {security['node_valid']}",
                f"CONTROLS_VALID: {security['controls_valid']}",
                f"CORE_VALID: {security['core_valid']}",
                "",
                "--- MODE ---",
                f"{report['mode']}",
            ]
        )


sync_reporter = SyncReporter()
