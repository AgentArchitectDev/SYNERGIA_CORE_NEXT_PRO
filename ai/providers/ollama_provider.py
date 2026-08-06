# =========================================================
# SYNERGIA OLLAMA PROVIDER COMPATIBILITY BRIDGE
# =========================================================
#
# Los módulos históricos de AI BUSINESS importan:
#
#     ai.providers.ollama_provider
#
# El proveedor real está en:
#
#     ai.integration.providers.ollama_provider
#
# Este archivo conserva ambas rutas.
# =========================================================

from ai.integration.providers.ollama_provider import (
    OllamaProvider,
)

__all__ = [
    "OllamaProvider",
]
