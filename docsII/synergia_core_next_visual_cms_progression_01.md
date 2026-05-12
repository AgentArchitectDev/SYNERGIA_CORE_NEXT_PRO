# SYNERGIA_CORE_NEXT_(Generation_IA_CMS)

## Estado Actual del Proyecto

SYNERGIA evolucionó desde un generador de templates HTML hacia una arquitectura moderna de CMS visual modular basado en bloques.

---

# Evolución Arquitectónica

## Antes

```text
Template HTML completo
→ replace()
→ output final
```

Sistema rígido.

---

## Ahora

```text
JSON PAGE
→ BLOCK ENGINE
→ ENSAMBLA BLOQUES
→ HTML FINAL
```

Sistema modular y componible.

---

# Nueva Arquitectura

```text
SYNERGIA_CORE_NEXT/
│
├── ai/
├── backend/
├── blocks/
├── core/
├── docs/
├── editor/
├── frontend/
├── json_engine/
├── legacy/
├── projects/
├── render/
├── storage/
├── templates/
└── tests/
```

---

# Sistema de Bloques

Cada bloque posee:

```text
blocks/<block_name>/
├── block.html
├── block.css
├── block.json
└── meta.json
```

---

# Bloques Actuales

## hero

Render principal.

## navbar

Barra superior.

## footer

Pie del sitio.

## cards

Contenido modular.

---

# meta.json

El archivo más importante para el futuro editor visual.

Ejemplo:

```json
{
  "name": "Hero Modern",
  "editable": true,
  "category": "hero",
  "fields": [
    {
      "id": "title",
      "type": "text"
    },
    {
      "id": "subtitle",
      "type": "textarea"
    },
    {
      "id": "button",
      "type": "text"
    }
  ]
}
```

---

# Block Engine

Archivo:

```text
render/block_engine.py
```

Responsabilidades:

- leer projects/demo_site/page.json
- detectar bloques
- cargar HTML
- cargar CSS
- reemplazar variables
- ensamblar página
- generar output final

---

# Render Modular Funcionando

Render exitoso:

```text
navbar
+ hero
→ HTML FINAL
```

Resultado generado correctamente en:

```text
storage/output/demo_site/index.html
```

---

# Block Registry

Archivo:

```text
core/block_registry.py
```

Responsabilidades:

- escanear blocks/
- leer meta.json
- detectar bloques automáticamente
- construir metadata dinámica

---

# Validación Exitosa

Comando ejecutado:

```python
from core.block_registry import registry
registry.get_blocks()
```

Resultado:

✔ lectura automática de bloques
✔ lectura de metadata
✔ detección de fields
✔ arquitectura dinámica funcionando

---

# Nuevo Paradigma del CMS

## Antes

```text
1 template = 1 web
```

## Ahora

```text
bloques infinitos = webs infinitas
```

---

# Estado Técnico Actual

## Funcionando

✔ backend FastAPI
✔ render engine
✔ block engine
✔ proyectos JSON
✔ templates modulares
✔ outputs dinámicos
✔ registry automático
✔ lectura metadata
✔ arquitectura componible

---

# Próxima Etapa

## PANEL VISUAL DINÁMICO

Objetivo:

```text
leer meta.json
→ construir inputs automáticamente
→ editar bloques visualmente
```

---

# Objetivos Inmediatos

## 1. Mejorar meta.json

Agregar:

- labels
- defaults
- categories
- tipos avanzados

---

## 2. Crear más bloques

Pendientes:

- gallery
- pricing
- contact
- faq
- testimonials
- services

---

## 3. Editor Visual Automático

Futuro:

```text
registry.get_blocks()
→ generar sidebar
→ generar formularios
→ editar page.json
→ re-render automático
```

---

# Objetivo Final

Construir:

```text
CMS VISUAL + IA + TEMPLATE ENGINE + SAAS
```

Arquitectura inspirada en:

- Elementor
- Webflow
- Wix Studio
- Builder.io
- Framer AI

---

# Estado Filosófico del Proyecto

SYNERGIA dejó de ser:

```text
un generador HTML
```

Y comenzó a convertirse en:

```text
UN SISTEMA VISUAL MODULAR INTELIGENTE
```

---

# Próximo Paso Crítico

## Dynamic Editor Panel

Construcción automática del editor visual desde meta.json.

