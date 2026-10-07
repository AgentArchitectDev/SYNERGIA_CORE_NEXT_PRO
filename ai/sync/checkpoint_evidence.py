"""
============================================================
SYNERGIA OS — CHECKPOINT EVIDENCE
============================================================
SYNERGIA SYNC — Evidencia estructurada de checkpoints.

Responsabilidad:
    Leer checkpoints y convertir metadatos documentales
    en evidencia estructurada READ-ONLY.

NO:
    - modifica checkpoints
    - modifica MASTER
    - modifica Git
    - autoriza ejecución
    - ejecuta agentes
    - determina autoridad
    - declara estado actual del sistema

Principio:
    EVIDENCE != AUTHORIZATION
    CHECKPOINT != CURRENT STATE
"""

from pathlib import Path
import re
from typing import Any, Dict, List


VALIDATED_CHECKPOINT = "VALIDATED_CHECKPOINT"
CHECKPOINT = "CHECKPOINT"
UNKNOWN = "UNKNOWN"


class CheckpointEvidenceCollector:
    """Extractor conservador de evidencia documental."""

    def __init__(self, checkpoints_path=None):
        self.checkpoints_path = Path(
            checkpoints_path
            if checkpoints_path is not None
            else Path(__file__).resolve().parents[2]
            / "docs"
            / "CHECKPOINTS"
        )

    def _extract(self, content: str, patterns: List[str]):
        for pattern in patterns:
            matches = re.findall(
                pattern,
                content,
                flags=re.IGNORECASE | re.MULTILINE,
            )
            if matches:
                return matches[-1].strip()
        return None

    def extract_file(self, path: Path) -> Dict[str, Any]:
        content = path.read_text(encoding="utf-8")

        checkpoint_section = None

        section_match = re.search(
            r"(?ms)^#\s+\d+\.\s+CHECKPOINT\s*$\n(.*?)(?=^#\s+\d+\.\s+|\Z)",
            content,
        )

        if section_match:
            checkpoint_section = section_match.group(1)

        metadata_content = (
            checkpoint_section
            if checkpoint_section is not None
            else content
        )

        checkpoint = self._extract(
            metadata_content,
            [
                r"^CHECKPOINT:\s*$\n\s*([^\n]+)",
            ],
        )

        version = self._extract(
            metadata_content,
            [
                r"^VERSION:\s*$\n\s*([^\n]+)",
            ],
        )

        date = self._extract(
            metadata_content,
            [
                r"^FECHA:\s*$\n\s*([^\n]+)",
                r"^DATE:\s*$\n\s*([^\n]+)",
            ],
        )

        state = self._extract(
            metadata_content,
            [
                r"^ESTADO:\s*$\n\s*([^\n]+)",
                r"^STATE:\s*$\n\s*([^\n]+)",
            ],
        )

        global_sync = self._extract(
            metadata_content,
            [
                r"^GLOBAL SYNC:\s*([^\n]+)",
            ],
        )

        security = self._extract(
            metadata_content,
            [
                r"^SECURITY:\s*([^\n]+)",
            ],
        )

        next_step = self._extract(
            metadata_content,
            [
                r"^NEXT:\s*([^\n]+)",
            ],
        )

        validated = bool(
            re.search(
                r"\bVALIDADO\b|\bVALIDATED\b|\bFULL_.*TEST:\s*PASS\b",
                content,
                flags=re.IGNORECASE,
            )
        )

        implemented = bool(
            re.search(
                r"\bIMPLEMENTADO\b|\bIMPLEMENTED\b",
                content,
                flags=re.IGNORECASE,
            )
        )

        pending_verification = bool(
            re.search(
                r"PENDIENTE DE VERIFICACIÓN|PENDING VERIFICATION",
                content,
                flags=re.IGNORECASE,
            )
        )

        if validated and checkpoint:
            classification = VALIDATED_CHECKPOINT
        elif checkpoint:
            classification = CHECKPOINT
        else:
            classification = UNKNOWN

        return {
            "path": str(path),
            "checkpoint": checkpoint,
            "version": version,
            "date": date,
            "state": state,
            "global_sync": global_sync,
            "security": security,
            "next": next_step,
            "validated": validated,
            "implemented": implemented,
            "pending_verification": pending_verification,
            "classification": classification,
        }

    def collect(self) -> Dict[str, Any]:
        if not self.checkpoints_path.exists():
            return {
                "collector": "CheckpointEvidenceCollector",
                "mode": "READ_ONLY",
                "exists": False,
                "count": 0,
                "files": [],
            }

        files = []

        for path in sorted(
            self.checkpoints_path.rglob("*.md")
        ):
            if path.is_file():
                files.append(
                    self.extract_file(path)
                )

        return {
            "collector": "CheckpointEvidenceCollector",
            "mode": "READ_ONLY",
            "exists": True,
            "count": len(files),
            "files": files,
        }


checkpoint_evidence_collector = CheckpointEvidenceCollector()
