"""
============================================================
SYNERGIA OS — SYNC COMPARATOR
============================================================
SYNERGIA SYNC — Mecanismo de Control de Coherencia

Responsabilidad:
    Comparar evidencia recopilada por SyncCollector.

NO:
    - modifica archivos
    - corrige inconsistencias
    - realiza commits
    - realiza push
    - autoriza ejecución
    - concede permisos
    - determina autoridad

Principio:
    COLLECT ≠ COMPARE ≠ AUTHORIZE ≠ EXECUTE
"""

from typing import Any, Dict


class SyncComparator:
    """Comparador conservador de evidencia SYNERGIA SYNC."""

    def compare_repository(self, evidence: Dict[str, Any]) -> Dict[str, Any]:
        repository = evidence.get("repository", {})

        return {
            "check": "repository",
            "status": (
                "PASS"
                if repository.get("exists")
                and repository.get("is_git_repository")
                else "UNKNOWN"
            ),
            "exists": repository.get("exists"),
            "is_git_repository": repository.get(
                "is_git_repository"
            ),
        }

    def compare_master(self, evidence: Dict[str, Any]) -> Dict[str, Any]:
        master = evidence.get("master", {})

        if not master.get("exists"):
            return {
                "check": "master",
                "status": "UNKNOWN",
                "reason": "master_not_found",
            }

        reference = master.get("reference")
        next_step = master.get("next")

        if reference and next_step:
            status = "OBSERVED"
        else:
            status = "UNKNOWN"

        return {
            "check": "master",
            "status": status,
            "reference": reference,
            "next": next_step,
            "state": master.get("state"),
            "date": master.get("date"),
        }

    def compare_git(self, evidence: Dict[str, Any]) -> Dict[str, Any]:
        git = evidence.get("git", {})

        branch = git.get("branch")
        head = git.get("head")

        if branch and head:
            status = "OBSERVED"
        else:
            status = "UNKNOWN"

        return {
            "check": "git",
            "status": status,
            "branch": branch,
            "head": head,
            "status_lines": len(
                git.get("status", "").splitlines()
            ) if git.get("status") else 0,
        }

    def compare_security(
        self,
        evidence: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Compara evidencia de seguridad sin modificarla."""

        security = evidence.get("security", {})

        if not security:
            return {
                "check": "security",
                "status": "UNKNOWN",
                "reason": "security_evidence_missing",
            }

        node = security.get(
            "node_consistency",
            {},
        )
        controls = security.get(
            "security_control_consistency",
            {},
        )
        core = security.get(
            "security_core_integrity",
            {},
        )

        node_valid = node.get("valid")
        controls_valid = controls.get("valid")
        core_valid = core.get("valid")

        if (
            node_valid is None
            or controls_valid is None
            or core_valid is None
        ):
            return {
                "check": "security",
                "status": "UNKNOWN",
                "reason": "security_evidence_incomplete",
            }

        if (
            node_valid is True
            and controls_valid is True
            and core_valid is True
        ):
            status = "PASS"
        else:
            status = "CONFLICT"

        return {
            "check": "security",
            "status": status,
            "node_valid": node_valid,
            "controls_valid": controls_valid,
            "core_valid": core_valid,
        }

    def compare_checkpoints(
        self,
        evidence: Dict[str, Any],
    ) -> Dict[str, Any]:
        checkpoints = evidence.get("checkpoints", {})

        if not checkpoints.get("exists"):
            return {
                "check": "checkpoints",
                "status": "UNKNOWN",
                "reason": "checkpoints_not_found",
            }

        count = checkpoints.get("count", 0)

        return {
            "check": "checkpoints",
            "status": (
                "OBSERVED"
                if count > 0
                else "UNKNOWN"
            ),
            "count": count,
        }

    def compare(self, evidence: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ejecuta comparaciones independientes.

        IMPORTANTE:
            No genera todavía un veredicto global SYNC_PASS /
            SYNC_PENDING / SYNC_CONFLICT.

        Esa decisión requiere una capa de evaluación posterior.
        """
        return {
            "comparator": "SyncComparator",
            "mode": "READ_ONLY",
            "repository": self.compare_repository(evidence),
            "master": self.compare_master(evidence),
            "git": self.compare_git(evidence),
            "checkpoints": self.compare_checkpoints(evidence),
            "security": self.compare_security(evidence),
        }


sync_comparator = SyncComparator()
