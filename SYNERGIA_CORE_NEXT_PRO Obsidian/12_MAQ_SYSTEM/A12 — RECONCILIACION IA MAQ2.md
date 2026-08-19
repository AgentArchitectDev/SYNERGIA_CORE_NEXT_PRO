# A12 — RECONCILIACIÓN IA MAQ2

## SYNERGIA_CORE_NEXT_PRO

Auditoría documental del ecosistema real de modelos IA de MAQ2.

---

# A12.9 — MATRIZ DE RECONCILIACIÓN IA MAQ2 ↔ VAULT

## Objetivo

Reconciliar el inventario real de modelos IA disponibles en MAQ2 con:

- documentación Obsidian;
- Registry;
- Ollama Provider;
- MultiModelEngine;
- AIOrchestrator;
- Business Generators;
- ModelService;
- StateManager;
- Runtime;
- Memory.

Esta fase es documental y forense.

No se modifica el CORE durante esta etapa.

---

# A12.10 — METADATOS REALES DE MODELOS IA

## Ollama

Versión detectada:

`0.18.2`

## Modelos detectados

Se identificaron los siguientes tags:

- `llama3.2:3b`
- `deepseek-coder-v2:16b`
- `qwen2.5-coder:7b`
- `llama3.1:latest`
- `phi3:3.8b`
- `deepseek-coder:6.7b`
- `gemma3:4b`
- `llama3:8b`
- `mistral:latest`
- `phi3:latest`
- `phi3:mini`
- `codellama:7b`
- `codellama:latest`
- `llama3:latest`

---

# A12.10.1 — METADATOS DIRECTOS OLLAMA

## llama3.2:3b

- architecture: `llama`
- parameters: `3.2B`
- context length: `131072`
- embedding length: `3072`
- quantization: `Q4_K_M`
- capabilities: completion, tools

## deepseek-coder-v2:16b

- architecture: `deepseek2`
- parameters: `15.7B`
- context length: `163840`
- embedding length: `2048`
- quantization: `Q4_0`
- capabilities: completion, insert

## qwen2.5-coder:7b

- architecture: `qwen2`
- parameters: `7.6B`
- context length: `32768`
- embedding length: `3584`
- quantization: `Q4_K_M`
- capabilities: completion, tools, insert
- license: Apache License 2.0

## codellama:7b

- architecture: `llama`
- parameters: `7B`
- context length: `16384`
- embedding length: `4096`
- quantization: `Q4_0`
- capabilities: completion

## llama3:8b

- architecture: `llama`
- parameters: `8.0B`
- context length: `8192`
- embedding length: `4096`
- quantization: `Q4_0`
- capabilities: completion

## mistral:latest

- architecture: `llama`
- parameters: `7.2B`
- context length: `32768`
- embedding length: `4096`
- quantization: `Q4_K_M`
- capabilities: completion, tools
- license: Apache License 2.0

## phi3:latest

- architecture: `phi3`
- parameters: `3.8B`
- context length: `131072`
- embedding length: `3072`
- quantization: `Q4_0`
- capabilities: completion

## phi3:mini

- architecture: `phi3`
- parameters: `3.8B`
- context length: `131072`
- embedding length: `3072`
- quantization: `Q4_0`
- capabilities: completion

## codellama:latest

- architecture: `llama`
- parameters: `7B`
- context length: `16384`
- embedding length: `4096`
- quantization: `Q4_0`
- capabilities: completion

## deepseek-coder:6.7b

- architecture: `llama`
- parameters: `7B`
- context length: `16384`
- embedding length: `4096`
- quantization: `Q4_0`
- capabilities: completion

## gemma3:4b

- architecture: `gemma3`
- parameters: `4.3B`
- context length: `131072`
- embedding length: `2560`
- quantization: `Q4_K_M`
- capabilities: completion, vision

## llama3:latest

- architecture: `llama`
- parameters: `8.0B`
- context length: `8192`
- embedding length: `4096`
- quantization: `Q4_0`
- capabilities: completion

## llama3.1:latest

- architecture: `llama`
- parameters: `8.0B`
- context length: `131072`
- embedding length: `4096`
- quantization: `Q4_K_M`
- capabilities: completion, tools

## phi3:3.8b

- architecture: `phi3`
- parameters: `3.8B`
- context length: `131072`
- embedding length: `3072`
- quantization: `Q4_0`
- capabilities: completion

---

# A12.10.2 — USO REAL DE MODELOS EN SYNERGIA

## Modelos referenciados en documentación

El Vault contiene referencias a:

- Llama3
- Llama3.1
- Mistral
- Phi3
- DeepSeek-Coder
- CodeLlama
- Gemma3

Archivos identificados:

`12_MAQ_SYSTEM/MAQ docs.md`

`02_AI_SYETEM/🤖 01 — AI.md`

`02_AI_SYETEM/10_AI_MODELS.md`

## Modelos referenciados directamente por el CORE

También aparecen:

- `llama3.2:3b`
- `deepseek-coder-v2:16b`
- `qwen2.5-coder:7b`

Por lo tanto existe una diferencia entre documentación histórica y referencias funcionales actuales del CORE.

---

# A12.10.3 — MAPA FUNCIONAL REAL DE MODELOS SYNERGIA

## Registry

Archivo:

`ai/providers/registry.py`

Contenido auditado:

```python
MODELS = {
    "frontend": "qwen2.5-coder:7b",
    "backend": "deepseek-coder-v2:16b",
    "copy": "llama3:8b",
    "seo": "mistral:latest",
    "light": "phi3:mini",
    "ux": "gemma3:4b"
}
