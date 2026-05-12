# SYNERGIA_CORE_NEXT — FASE CONSOLIDACIÓN MVP

Fecha: 2026-05-06
Autor: Gerardo Bergoglio
Proyecto: SYNERGIA_CORE_NEXT_(Generation_IA_CMS)

---

# OBJETIVO DE ESTA ETAPA

Transformar el ecosistema anterior de SYNERGIA_MASTER en una arquitectura limpia, modular y orientada a producto real.

La meta dejó de ser:
- experimentar,
- acumular módulos,
- crear estructuras teóricas.

La nueva meta es:

```txt
CONSOLIDAR UN CMS IA FUNCIONAL
```

---

# TRANSICIÓN DE PROYECTO

## Proyecto anterior

```txt
SYNERGIA_MASTER
```

Funcionó como:
- laboratorio,
- exploración,
- pruebas,
- generación de templates,
- experimentación CMS/IA.

---

## Nuevo núcleo

```txt
SYNERGIA_CORE_NEXT
```

Objetivo:
- arquitectura limpia,
- CMS IA real,
- motor template profesional,
- producto evolucionable,
- base SaaS futura.

---

# FASES REALIZADAS

## 1. Migración inicial

Se generó:

```bash
migrar_synergia.sh
```

Funciones:
- separar legacy,
- crear estructura nueva,
- evitar contaminación del core,
- migrar documentación base.

---

## 2. Limpieza arquitectónica

Se generó:

```bash
clean_synergia.sh
```

Funciones:
- eliminar basura Python,
- eliminar __pycache__,
- eliminar librerías copiadas desde venv,
- renombrar estructura al nuevo modelo.

Resultado:

```txt
SYNERGIA_CORE_NEXT
│
├── ai
├── backend
├── core
├── docs
├── editor
├── frontend
├── json_engine
├── render
├── storage
├── templates
├── legacy
└── tests
```

---

## 3. Refactor V1

Se generó:

```bash
refactor_v1_synergia.sh
```

Funciones:
- crear storage profesional,
- migrar outputs,
- migrar clientes,
- migrar projects,
- actualizar rutas internas,
- actualizar imports.

Storage final:

```txt
storage/
├── clientes
├── output
└── projects
```

---

# ARQUITECTURA ACTUAL

## templates

```txt
templates/core_templates
```

Contiene:
- templates HTML premium,
- templates cinematográficos,
- estilos reutilizables,
- layouts visuales.

---

## editor

```txt
editor/cms_editor
```

Contiene:
- interfaz CMS,
- formulario dinámico,
- preview,
- conexión API.

Archivos:

```txt
app.js
index.html
styles.css
config.json
```

---

## frontend

```txt
frontend/dashboard
```

Contiene:
- dashboard general,
- accesos,
- panel visual.

---

## ai

```txt
ai/core_ai
```

Objetivo:
- generación IA,
- prompts,
- contenido dinámico,
- automatización.

---

## render

```txt
render/render_engine
```

Contiene el motor principal.

Archivo principal:

```txt
engine.py
```

---

# FUNCIONAMIENTO DEL ENGINE

El engine actualmente:

1. Lee templates HTML.
2. Reemplaza variables dinámicas.
3. Genera outputs finales.
4. Exporta index.html.

Código central:

```python
for k, v in data.items():
    html = html.replace("{{" + k.upper() + "}}", str(v))
```

Pipeline actual:

```txt
TEMPLATE
↓
DATA
↓
RENDER
↓
OUTPUT HTML
```

---

# BACKEND FASTAPI

Archivo:

```txt
backend/api/app.py
```

Estado actual:

```txt
ONLINE
```

Comando usado:

```bash
uvicorn backend.api.app:app --reload
```

Resultado:

```txt
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

FastAPI funcionando correctamente.

---

# CMS EDITOR

El CMS ya realiza:

## ✔ carga templates

Endpoint:

```txt
/templates
```

---

## ✔ carga clientes

Endpoint:

```txt
/clientes
```

---

## ✔ envía datos dinámicos

Ejemplo:

```json
{
  "brand_name": "Empresa",
  "hero_title": "Titulo",
  "hero_subtitle": "Subtitulo"
}
```

---

## ✔ genera proyectos

Endpoint:

```txt
/generate_cms
```

---

## ✔ preview dinámico

Usa iframe conectado al output generado.

---

# ESTADO REAL DEL PROYECTO

## YA EXISTE

✔ CMS base
✔ FastAPI
✔ Render engine
✔ Templates
✔ Output system
✔ Preview
✔ Arquitectura limpia
✔ Storage profesional
✔ API funcional
✔ OpenAPI/docs

---

# LO QUE FALTA

## ETAPA SIGUIENTE

```txt
VALIDACION FUNCIONAL DEL MVP
```

---

# PIPELINE OBJETIVO

```txt
EDITOR
↓
API
↓
ENGINE
↓
TEMPLATE
↓
OUTPUT
↓
PREVIEW
```

---

# OBJETIVO DEL MVP

El MVP funcional mínimo será:

```txt
1. Elegir template
2. Completar contenido
3. IA genera texto
4. Renderizar HTML
5. Preview
6. Exportar
```

---

# CONCLUSIONES TÉCNICAS

El proyecto ya no está en etapa de exploración.

Ahora se encuentra en:

```txt
CONSOLIDACION DE PRODUCTO
```

El núcleo funcional ya existe.

La arquitectura quedó:
- entendible,
- mantenible,
- modular,
- escalable.

---

# PRINCIPALES LOGROS

## 1. Separación de legacy

Se aisló el sistema anterior sin perder información.

---

## 2. Creación de arquitectura limpia

El nuevo CORE ya posee estructura profesional.

---

## 3. Detección del núcleo real

Se identificaron:
- templates,
- render engine,
- CMS,
- backend,
- IA,
- outputs.

---

## 4. Consolidación del pipeline

Por primera vez:

```txt
EDITOR → API → ENGINE → OUTPUT
```

existe de forma clara.

---

# PRÓXIMA ETAPA

## PASO CRÍTICO

```txt
PROBAR EL PIPELINE COMPLETO
```

Objetivos:

1. Abrir el CMS editor.
2. Verificar carga de templates.
3. Verificar carga de clientes.
4. Generar output real.
5. Validar preview.
6. Detectar errores reales.
7. Ajustar rutas finales.
8. Consolidar MVP.

---

# COMANDOS IMPORTANTES

## Levantar FastAPI

```bash
uvicorn backend.api.app:app --reload
```

---

## Abrir CMS

```bash
xdg-open editor/cms_editor/index.html
```

---

# VISIÓN FINAL

SYNERGIA_CORE_NEXT ya no es solamente un experimento.

Ahora es:

```txt
CMS IA + GENERADOR WEB + MOTOR TEMPLATE
```

con potencial real de evolucionar a:
- plataforma SaaS,
- generador automático de sitios,
- editor visual IA,
- sistema multi-template,
- constructor web cinematográfico.

