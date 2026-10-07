"""
============================================================
SYNERGIA OS — SECURITY EVIDENCE ADAPTER
============================================================
SYNERGIA SYNC — Mecanismo de Control de Coherencia

Responsabilidad:
    Adaptar evidencia producida por los validadores de
    seguridad existentes para su consumo por SYNERGIA SYNC.

IMPORTANTE:
    SECURITY VALID ≠ SYNC_PASS

NO:
    - modifica controles de seguridad
    - activa/desactiva controles
    - concede autoridad
    - crea ExecutionGrant
    - ejecuta herramientas
    - corrige inconsistencias
    - reemplaza los validadores existentes

Principio:
    SECURITY EVIDENCE → SYNC
    SYNC ≠ AUTHORIZATION
"""

from typing import Any, Dict

from ai.security.node_consistency_validator import (
    node_consistency_validator,
)
from ai.security.security_control_consistency_validator import (
    security_control_consistency_validator,
)
from ai.security.security_core_integrity_validator import (
    security_core_integrity_validator,
)


class SecurityEvidenceAdapter:
    """Adaptador READ-ONLY de evidencia de seguridad."""

    def collect(self) -> Dict[str, Any]:
        """
        Ejecuta los validadores existentes y normaliza su salida.

        Los validadores siguen siendo la fuente de evidencia.
        Este componente no reproduce sus reglas.
        """

        node_result = (
            node_consistency_validator.validate_all()
        )

        control_result = (
            security_control_consistency_validator.validate()
        )

        core_result = (
            security_core_integrity_validator.validate()
        )

        return {
            "component": "SecurityEvidenceAdapter",
            "mode": "READ_ONLY",
            "node_consistency": node_result,
            "security_control_consistency": control_result,
            "security_core_integrity": core_result,
        }

    def summarize(
        self,
        evidence: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Genera un resumen sin convertirlo en autorización."""

        node = evidence.get("node_consistency", {})
        controls = evidence.get(
            "security_control_consistency",
            {},
        )
        core = evidence.get(
            "security_core_integrity",
            {},
        )

        return {
            "node_valid": node.get("valid"),
            "controls_valid": controls.get("valid"),
            "core_valid": core.get("valid"),
            "nodes_checked": node.get(
                "nodes_checked",
                0,
            ),
            "controls_checked": controls.get(
                "controls_checked",
                0,
            ),
            "core_controls_checked": core.get(
                "controls_checked",
                0,
            ),
            "canonical_authority": node.get(
                "canonical_authority"
            ),
            "canonical_direction": node.get(
                "canonical_direction"
            ),
            "canonical_autonomous_security_authority": (
                node.get(
                    "canonical_autonomous_security_authority"
                )
            ),
        }


security_evidence_adapter = SecurityEvidenceAdapter()
