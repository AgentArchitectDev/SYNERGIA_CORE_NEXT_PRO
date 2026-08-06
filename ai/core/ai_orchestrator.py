# =========================================================
# SYNERGIA AI ORCHESTRATOR COMPATIBILITY BRIDGE
# =========================================================
#
# AI BUSINESS espera:
#
#     from ai.core.ai_orchestrator import ai_orchestrator
#
# La implementación real se conserva en:
#
#     ai.core_system.core.ai_orchestrator
#
# Este puente evita duplicar lógica y mantiene
# compatibilidad con la arquitectura histórica.
# =========================================================

from ai.core_system.core.ai_orchestrator import (
    AIOrchestrator,
    ai_orchestrator,
)

__all__ = [
    "AIOrchestrator",
    "ai_orchestrator",
]
