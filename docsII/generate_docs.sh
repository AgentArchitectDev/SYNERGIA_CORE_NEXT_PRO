#!/bin/bash

BASE="docs"

declare -A FILES=(
  ["00_OVERVIEW/SYNERGIA_OVERVIEW.md"]="# SYNERGIA OVERVIEW\nSistema base del proyecto SYNERGIA CORE NEXT"
  
  ["01_ARCHITECTURE/CORE_ARCHITECTURE.md"]="# CORE ARCHITECTURE\nArquitectura central del sistema"
  ["01_ARCHITECTURE/DEPENDENCY_GRAPH.md"]="# DEPENDENCY GRAPH\nRelaciones entre módulos"
  ["01_ARCHITECTURE/FOLDER_STRUCTURE.md"]="# FOLDER STRUCTURE\nEstructura completa del sistema"

  ["02_AI_SYSTEM/AI_ORCHESTRATOR.md"]="# AI ORCHESTRATOR\nMotor principal de IA"
  ["02_AI_SYSTEM/AI_PIPELINE.md"]="# AI PIPELINE\nFlujo de generación IA"
  ["02_AI_SYSTEM/OLLAMA_SYSTEM.md"]="# OLLAMA SYSTEM\nIntegración modelos locales"
  ["02_AI_SYSTEM/PROMPTS_SYSTEM.md"]="# PROMPTS SYSTEM\nSistema de prompts"

  ["03_RENDER_ENGINE/RENDER_ENGINE.md"]="# RENDER ENGINE\nMotor de render HTML"
  ["03_RENDER_ENGINE/LIVE_RENDER.md"]="# LIVE RENDER\nRender en tiempo real"
  ["03_RENDER_ENGINE/TEMPLATE_BINDING.md"]="# TEMPLATE BINDING\nUnión JSON → HTML"

  ["04_BLOCK_SYSTEM/BLOCKS_ARCHITECTURE.md"]="# BLOCK SYSTEM\nSistema de bloques UI"
  ["04_BLOCK_SYSTEM/BLOCK_TYPES.md"]="# BLOCK TYPES\nTipos de bloques"
  ["04_BLOCK_SYSTEM/BLOCK_META_SYSTEM.md"]="# BLOCK META\nMetadatos de bloques"

  ["05_VISUAL_EDITOR/VISUAL_EDITOR_CORE.md"]="# VISUAL EDITOR\nEditor visual principal"
  ["05_VISUAL_EDITOR/DRAG_DROP_SYSTEM.md"]="# DRAG DROP\nSistema drag & drop"
  ["05_VISUAL_EDITOR/LIVE_PREVIEW_SYSTEM.md"]="# LIVE PREVIEW\nVista en vivo"
  ["05_VISUAL_EDITOR/UI_SYSTEM.md"]="# UI SYSTEM\nInterfaz del editor"
  ["05_VISUAL_EDITOR/VISUAL_PROPERTIES.md"]="# VISUAL PROPERTIES\nPropiedades visuales"
  ["05_VISUAL_EDITOR/AI_ASSISTANT.md"]="# AI ASSISTANT\nAsistente IA del editor"

  ["06_JSON_ENGINE/JSON_STRUCTURE.md"]="# JSON ENGINE\nEstructura de datos"
  ["06_JSON_ENGINE/DYNAMIC_DATA.md"]="# DYNAMIC DATA\nDatos dinámicos"
  ["06_JSON_ENGINE/CLIENT_DATA_SYSTEM.md"]="# CLIENT DATA\nDatos clientes"

  ["07_STORAGE/STORAGE_SYSTEM.md"]="# STORAGE SYSTEM\nSistema de almacenamiento"
  ["07_STORAGE/OUTPUT_SYSTEM.md"]="# OUTPUT SYSTEM\nOutputs generados"
  ["07_STORAGE/PROJECT_SYSTEM.md"]="# PROJECT SYSTEM\nGestión de proyectos"

  ["08_API_BACKEND/API_SYSTEM.md"]="# API SYSTEM\nBackend API"
  ["08_API_BACKEND/ENDPOINTS.md"]="# ENDPOINTS\nRutas del sistema"

  ["09_TEMPLATES/TEMPLATE_ENGINE.md"]="# TEMPLATE ENGINE\nMotor de templates"
  ["09_TEMPLATES/CINEMATIC_TEMPLATES.md"]="# CINEMATIC TEMPLATES\nTemplates avanzados"
  ["09_TEMPLATES/TEMPLATE_MARKETPLACE.md"]="# TEMPLATE MARKETPLACE\nMercado de templates"

  ["10_WORKFLOW/AUTOMATION_PIPELINE.md"]="# AUTOMATION PIPELINE\nAutomatización"
  ["10_WORKFLOW/CLIENT_FLOW.md"]="# CLIENT FLOW\nFlujo cliente"

  ["11_FUTURE/SAAS_VISION.md"]="# SAAS VISION\nVisión del sistema"
  ["11_FUTURE/AI_AGENCY.md"]="# AI AGENCY\nAgencia IA"
  ["11_FUTURE/SYNERGIA_FUTURE.md"]="# FUTURE\nEvolución del sistema"

  ["12_SYSTEM_MAP/GRAPH_SYSTEM.md"]="# GRAPH SYSTEM\nGrafo del sistema"
  ["12_SYSTEM_MAP/DEPENDENCY_MAP.md"]="# DEPENDENCY MAP\nMapa dependencias"
  ["12_SYSTEM_MAP/AUTO_MAP_GENERATOR.md"]="# AUTO MAP\nGenerador de mapa"
  ["12_SYSTEM_MAP/OBSIDIAN_GRAPH.md"]="# OBSIDIAN GRAPH\nVisual tipo Obsidian"

  ["99_MASTER_BOOK/SYNERGIA_MASTER_BOOK.md"]="# MASTER BOOK\nDocumento maestro del sistema"
)

echo "Generando estructura SYNERGIA..."

for file in "${!FILES[@]}"; do
  path="$BASE/$file"
  mkdir -p "$(dirname "$path")"
  echo -e "${FILES[$file]}" > "$path"
  echo "creado: $path"
done

echo "DONE ✔"
