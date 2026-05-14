# 🧠 SYNERGIA BRAIN SYSTEM v1 (LOG COMPLETO)

## 📅 Fecha
2026-05-14

---

# 🚀 CONTEXTO GENERAL

SYNERGIA CORE NEXT PRO evolucionó hacia un sistema de:

- AI LAB local (PyQt6)
- integración con Ollama
- sistema de memoria persistente
- multi-modelo IA
- exportación de respuestas
- comparación de modelos
- arquitectura tipo “AI Operating System”

---

# 🧠 OBJETIVO DEL SISTEMA

Transformar SYNERGIA en un:

> AI Operating System local con agentes, memoria global, routing inteligente y generación automática de conocimiento.

---

# 🧩 COMPONENTES ACTUALES

## 1. UI LAYER
- PyQt6 AI Lab Panel
- input prompt
- selector de modelo
- output streaming
- botones:
  - ejecutar IA
  - exportar historial
  - ver historial
  - comparar modelos

---

## 2. MEMORY SYSTEM

### MemoryManager (actual)
- guarda prompts
- guarda sesiones
- guarda conversaciones en JSON
- exporta historial

### Evolución futura:
- memoria global persistente
- ranking de respuestas
- memoria cross-modelo

---

## 3. PROVIDERS

### OllamaConnector
- streaming real con /api/chat
- conexión local HTTP 11434
- soporte multi-modelo

Modelos disponibles:
- llama3.2:3b
- llama3:8b
- mistral:latest
- phi3:mini
- deepseek-coder-v2
- qwen2.5-coder
- gemma3

---

## 4. MODELS MANAGER
- detecta modelos desde Ollama API
- lista dinámica para UI

---

# 🧠 BRAIN SYSTEM (NUEVO NIVEL)

## 🔥 Brain Router

Decide automáticamente el modelo:

```python
code → deepseek-coder-v2
marketing → mistral
general → llama3
light → phi3
