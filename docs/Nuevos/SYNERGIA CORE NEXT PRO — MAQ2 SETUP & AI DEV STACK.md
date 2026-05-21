SYNERGIA CORE NEXT PRO — MAQ2 SETUP & AI DEV STACK
Estado consolidado — Mayo 2026
🧠 OBJETIVO

Convertir MAQ2 en un nodo completo de desarrollo IA industrial para SYNERGIA V4 OS.

Arquitectura basada en:

Ollama
+
Aider
+
Modelos Locales
+
GitHub
+
PyQt6
+
AI LAB
+
Sistema Multi-MAQ
📁 UBICACIÓN REAL DEL PROYECTO (MAQ2)
/mnt/71392f5d/SYNERGIA_CORE_NEXT_PRO
🔥 ESTRUCTURA PRINCIPAL DETECTADA
ai/
api/
backend/
blocks/
core/
docs/
editor/
frontend/
json_engine/
legacy/
outputs/
projects/
render/
storage/
templates/
tests/
tools/
venv/
🧠 COMPONENTES IMPORTANTES DEL PROYECTO
ai/

Núcleo IA del sistema.

Contiene:

providers/
memory/
core_ai/
prompts/
image/
orchestrator.py

Funciones:

conexión Ollama
memoria persistente
agentes
streaming
prompts
modelos
backend/

Backend central del sistema.

editor/

Sistema CMS / editor visual.

core/

Núcleo lógico de SYNERGIA.

venv/

Entorno virtual Python principal.

🧠 MODELOS OLLAMA DISPONIBLES EN MAQ2
🔥 Industrial
deepseek-coder-v2:16b

Uso:

arquitectura
refactor complejo
multiarchivo
razonamiento profundo
🔥 Mejor equilibrio
qwen2.5-coder:7b

Uso:

Aider
desarrollo diario
velocidad + calidad
⚡ Ultra rápido
llama3.2:3b

Uso:

navegación repo
pruebas rápidas
agentes rápidos
Otros disponibles
gemma3:4b
mistral
phi3
codellama
llama3
deepseek-coder:6.7b
🧠 INSTALACIÓN Y CONFIGURACIÓN AIDER
Activar entorno virtual
source venv/bin/activate
Instalar Aider
pip install aider-chat --default-timeout=1000
Verificar instalación
aider --version

Resultado:

aider 0.86.2
🧠 CONFIGURAR OLLAMA PARA AIDER
export OLLAMA_API_BASE=http://localhost:11434
🚀 EJECUTAR AIDER
Modelo recomendado
aider --model ollama/qwen2.5-coder:7b
⚠ PROBLEMA DETECTADO

SYNERGIA es un repo MUY grande:

4970 archivos

El escaneo completo puede consumir:

RAM
CPU
tiempo de análisis
🔥 SOLUCIÓN INDUSTRIAL

Usar:

--subtree-only
🚀 EJEMPLOS RECOMENDADOS
SOLO AI LAB
aider --model ollama/qwen2.5-coder:7b --subtree-only ai
SOLO BACKEND
aider --model ollama/qwen2.5-coder:7b --subtree-only backend
SOLO CORE
aider --model ollama/qwen2.5-coder:7b --subtree-only core
🧠 PROMPTS DE PRUEBA
Analizar estructura
Lista las carpetas principales y explica la arquitectura
Analizar provider
Analiza ai/providers/ollama_provider.py y explica cómo funciona
Analizar memoria
Explica el sistema de memoria persistente
Analizar AI LAB
Analiza la arquitectura del AI LAB
🔥 DESCUBRIMIENTO CLAVE

Repos IA enormes deben dividirse por contexto.

Esto es exactamente lo que hacen:

Cursor
Aider
Claude Code
Devin
OpenHands
🧠 CONCEPTO MAQ1 vs MAQ2
MAQ1
DEV NODE
pruebas
desarrollo liviano
experimentación
MAQ2
AI CORE NODE
análisis pesado
IA principal
AI LAB REAL
modelos grandes
🚀 VISIÓN FUTURA — SYNERGIA V4 OS
FASE ACTUAL
Terminal AI Development

Con:

Aider
+
Ollama
+
Repo real
+
Modelos locales
SIGUIENTE ETAPA

Crear:

AI DEV PANEL

con:

Explorador de archivos
Proyecto visual
Chat IA
Streaming tipo ChatGPT
Editor integrado
Código + IA
Selector de modelos
Ollama local
Agentes IA
Dev
Business
Research
Automation
🔥 IDEA CENTRAL

Convertir SYNERGIA en:

Visual AI Operating System
🧠 OBJETIVO FINAL

Un sistema propio tipo:

Cursor
Windsurf
Claude Code
OpenHands

pero:

LOCAL
MODULAR
MULTI-MODELO
MULTI-MAQ

y completamente integrado en:

SYNERGIA_CORE_NEXT_PRO

🔥
