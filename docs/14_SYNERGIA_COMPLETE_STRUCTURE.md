# 🧠 SYNERGIA CORE NEXT — ARQUITECTURA COMPLETA

Este documento describe la estructura completa del sistema SYNERGIA CORE NEXT PRO, explicando cada carpeta, su función, flujo y relación con el resto del sistema.

---

# 🧱 1. BACKEND

## 📁 backend/

### 🎯 Función principal
Es el núcleo del sistema servidor. Controla toda la lógica de ejecución.

### 📌 Responsabilidades:
1. Levantar API (FastAPI)
2. Gestionar requests del frontend
3. Conectar con IA (Ollama)
4. Orquestar generación de contenido
5. Controlar proyectos activos

### 🔗 Conexiones:
- ai/ → generación inteligente
- render/ → creación HTML final
- storage/ → persistencia
- editor/ → interfaz visual

### ⚙️ Flujo:
Usuario → backend → IA → render → frontend

---

# 🧠 2. AI ENGINE

## 📁 ai/

### 🎯 Función principal
Módulo de inteligencia del sistema.

### 📌 Responsabilidades:
1. Conectar con Ollama
2. Seleccionar modelos (llama, mistral, phi3, etc.)
3. Procesar prompts
4. Generar JSON estructurado
5. Optimizar respuestas según MAQ1 / MAQ2

### 🔗 Conexiones:
- backend/
- IA_MODELS (externo)
- render/

### ⚙️ Flujo:
Prompt → modelo → JSON → backend

---

# 🧩 3. BLOCK SYSTEM

## 📁 blocks/

### 🎯 Función principal
Sistema de componentes UI reutilizables.

### 📌 Responsabilidades:
1. Definir componentes visuales
2. Estandarizar UI
3. Permitir reutilización
4. Servir como base para IA

### 🧱 Tipos de bloques:
1. hero
2. navbar
3. cards
4. footer
5. forms
6. sections

### 🔗 Conexiones:
- render/
- editor/
- ai/

### ⚙️ Flujo:
IA genera → blocks → render

---

# 🎨 4. RENDER ENGINE

## 📁 render/

### 🎯 Función principal
Convierte datos estructurados en HTML real.

### 📌 Responsabilidades:
1. Interpretar JSON
2. Mapear bloques
3. Generar HTML/CSS
4. Construir páginas finales

### 🔗 Conexiones:
- blocks/
- templates/
- ai/

### ⚙️ Flujo:
JSON → render → HTML

---

# 🖥️ 5. EDITOR VISUAL

## 📁 editor/

### 🎯 Función principal
Interfaz visual tipo Webflow / Elementor.

### 📌 Responsabilidades:
1. Drag & drop
2. Edición en vivo
3. Preview instantáneo
4. Modificación de bloques

### 🔗 Conexiones:
- blocks/
- render/
- backend/

### ⚙️ Flujo:
Usuario → editor → backend → render

---

# 📄 6. TEMPLATES

## 📁 templates/

### 🎯 Función principal
Base estructural de sitios.

### 📌 Responsabilidades:
1. Plantillas HTML base
2. Diseños por industria
3. Estructuras iniciales
4. Estilos prediseñados

### 🔗 Conexiones:
- render/
- ai/

### ⚙️ Flujo:
IA selecciona template → render final

---

# 💾 7. STORAGE

## 📁 storage/

### 🎯 Función principal
Persistencia de datos del sistema.

### 📌 Responsabilidades:
1. Guardar proyectos
2. Guardar usuarios
3. Guardar outputs IA
4. Versionado de contenido

### 🔗 Conexiones:
- backend/
- projects/

### ⚙️ Flujo:
backend → storage → recuperación

---

# 📦 8. PROJECTS

## 📁 projects/

### 🎯 Función principal
Contiene instancias generadas del sistema.

### 📌 Responsabilidades:
1. Cada proyecto es independiente
2. Exportación de sitios
3. Separación por cliente
4. Versionado por proyecto

### 🔗 Conexiones:
- storage/
- backend/

### ⚙️ Flujo:
Proyecto → storage → export

---

# 🧠 9. CORE

## 📁 core/

### 🎯 Función principal
Núcleo lógico del sistema.

### 📌 Responsabilidades:
1. Configuración global
2. Orquestación general
3. Sistema MAQ1 / MAQ2
4. Control de flujo interno

### 🔗 Conexiones:
TODAS las carpetas

### ⚙️ Flujo:
CORE gobierna todo el sistema

---

# 🤖 10. IA MODELS (EXTERNO)

## 📁 /mnt/SCN_MAIN/SCN/IA_MODELS

### 🎯 Función principal
Almacenamiento de modelos de IA locales.

### 📌 Contenido:
1. llama3 / llama3.1
2. mistral
3. phi3
4. codellama
5. deepseek-coder
6. gemma3

### 🔗 Conexiones:
- ai/

### ⚙️ Flujo:
ai → llama modelo → respuesta

---

# 🧠 RELACIÓN GENERAL DEL SISTEMA

## 🔥 FLUJO COMPLETO

1. Usuario genera prompt
2. backend recibe request
3. ai selecciona modelo
4. Ollama responde
5. JSON estructurado generado
6. render convierte a HTML
7. editor permite modificar
8. storage guarda resultado
9. projects organiza salida

---

# 🧠 MAQ SYSTEM (CONTROL DE CONTEXTO)

## 🏠 MAQ1 (CASA)
- desarrollo
- experimentación
- debugging

## 🏢 MAQ2 (TRABAJO)
- producción
- estabilidad
- despliegue

---

# 🚀 CONCLUSIÓN

SYNERGIA CORE NEXT PRO es un sistema modular de:

- IA local
- CMS visual
- render dinámico
- arquitectura SaaS
- control por contexto MAQ

Su objetivo es convertirse en un sistema operativo de creación de software automatizado.


