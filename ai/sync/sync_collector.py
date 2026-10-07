"""
============================================================
SYNERGIA OS — SYNC COLLECTOR
============================================================
SYNERGIA SYNC — Mecanismo de Control de Coherencia

Responsabilidad:
    Recopilar evidencia técnica de forma READ-ONLY.

NO:
    - modifica archivos
    - elimina archivos
    - realiza commits
    - realiza push
    - autoriza ejecución
    - corrige inconsistencias
    - concede autoridad

Principio:
    COLLECT ≠ COMPARE ≠ AUTHORIZE ≠ EXECUTE
"""

from pathlib import Path
import subprocess
import re
from typing import Any, Dict, List

from ai.sync.security_evidence_adapter import (
    security_evidence_adapter,
)


class SyncCollector:
    """Recolector READ-ONLY de evidencia de coherencia."""

    def __init__(self, repository_root=None):
        self.repository_root = Path(
            repository_root
            if repository_root is not None
            else Path(__file__).resolve().parents[2]
        )

        self.master_path = (
            self.repository_root
            / "docs"
            / "SYNERGIA_OS_MASTER_CONTINUITY.md"
        )

        self.checkpoints_path = (
            self.repository_root
            / "docs"
            / "CHECKPOINTS"
        )

    def _git(self, *args) -> str:
        """Ejecuta únicamente comandos Git de lectura."""
        result = subprocess.run(
            ["git", *args],
            cwd=self.repository_root,
            capture_output=True,
            text=True,
            check=False,
        )

        return result.stdout.strip()

    def collect_git(self) -> Dict[str, Any]:
        """Recopila estado Git sin modificar el repositorio."""
        return {
            "branch": self._git(
                "branch",
                "--show-current",
            ),
            "head": self._git(
                "rev-parse",
                "--short",
                "HEAD",
            ),
            "status": self._git(
                "status",
                "--short",
            ),
        }

    def collect_master(self) -> Dict[str, Any]:
        """Recopila evidencia básica del MASTER."""
        if not self.master_path.exists():
            return {
                "exists": False,
                "path": str(self.master_path),
            }

        content = self.master_path.read_text(
            encoding="utf-8"
        )

        reference = None
        date = None
        next_step = None
        state = None

        patterns = {
            "reference": r"REFERENCE:\s*(.+)",
            "date": r"DATE:\s*(.+)",
            "next": r"NEXT:\s*(.+)",
            "state": r"STATE:\s*(.+)",
        }

        values = {}

        for key, pattern in patterns.items():
            matches = re.findall(
                pattern,
                content,
            )

            if matches:
                values[key] = matches[-1].strip()

        reference = values.get("reference")
        date = values.get("date")
        next_step = values.get("next")
        state = values.get("state")

        return {
            "exists": True,
            "path": str(self.master_path),
            "reference": reference,
            "date": date,
            "next": next_step,
            "state": state,
        }

    def collect_checkpoints(self) -> Dict[str, Any]:
        """Recopila existencia y rutas de checkpoints."""
        if not self.checkpoints_path.exists():
            return {
                "exists": False,
                "path": str(self.checkpoints_path),
                "files": [],
            }

        files: List[str] = []

        for path in sorted(
            self.checkpoints_path.rglob("*")
        ):
            if path.is_file():
                files.append(
                    str(
                        path.relative_to(
                            self.repository_root
                        )
                    )
                )

        return {
            "exists": True,
            "path": str(self.checkpoints_path),
            "count": len(files),
            "files": files,
        }

    def collect_repository(self) -> Dict[str, Any]:
        """Recopila identidad básica del repositorio."""
        return {
            "path": str(self.repository_root),
            "exists": self.repository_root.exists(),
            "is_git_repository": (
                (self.repository_root / ".git").exists()
            ),
        }

    def collect(self) -> Dict[str, Any]:
        """
        Recopila toda la evidencia básica.

        Este método NO determina el estado SYNC.
        """
        return {
            "collector": "SyncCollector",
            "mode": "READ_ONLY",
            "repository": self.collect_repository(),
            "git": self.collect_git(),
            "master": self.collect_master(),
            "checkpoints": self.collect_checkpoints(),
            "security": security_evidence_adapter.collect(),
        }


sync_collector = SyncCollector()
