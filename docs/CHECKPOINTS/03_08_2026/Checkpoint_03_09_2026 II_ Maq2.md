Se ha pausado el análisis
from pathlib import Path
content = r"""# SYNERGIA OS – AI New Generation
## CHECKPOINT OFICIAL — MAQ2 — 03_08_2026

**Fecha:** 03/08/2026  
**Nodo:** MAQ2 — Trabajo  
**Hostname:** `gerardoalbertobergoglio-H510M-S2H`  
**Proyecto activo:** `/mnt/71392f5d/SYNERGIA_CORE_NEXT_PRO`  
**Rama Git:** `synergia_v3_core_restructure`  
**Estado:** DIAGNÓSTICO DE MAQ2 COMPLETADO — CORRECCIÓN MÍNIMA PENDIENTE

---

# 1. OBJETIVO DE ESTE CHECKPOINT

Este documento permite retomar el proyecto desde:

- otro perfil de ChatGPT;
- otra IA;
- una conversación nueva;
- cualquier asistente técnico.

No reiniciar fases anteriores. No redefinir la arquitectura. Continuar exactamente desde el punto indicado en la sección **PUNTO DE REANUDACIÓN OFICIAL**.

---

# 2. ESTADO GLOBAL DEL PROYECTO

## Fases previamente validadas

- ✅ **STAGE 6.1T — Recuperación Técnica:** COMPLETADO y VALIDADO.
- ✅ **STAGE 6.1O — Ollama:** COMPLETADO y VALIDADO.
- 🟡 **STAGE 6.2 — AI BUSINESS:** avanzado y validado parcialmente en MAQ1.

## Estado conocido de STAGE 6.2 en MAQ1

- ✅ Project Builder
- ✅ Website Generator
- ✅ Branding Generator
- ✅ Social Generator
- ⏳ Docs Generator
- ⏳ Integración final de Business Generator
- ⏳ Prueba end-to-end completa

Prueba real previamente validada:

- Modelo MAQ1: `llama3.2:1b`
- Ollama Provider: OK
- Social Generator: OK
- Project Builder: OK
- Tiempo: 85.16 segundos
- Salida: `outputs/stage_6_2_social_test/social/social.txt`
- Tamaño: 2491 bytes

---

# 3. ESTADO DE MAQ2

MAQ2 tiene una copia completa y estable de la arquitectura V3, pero no está en el directorio recuperado de MAQ1.

Directorio actual:

```bash
/mnt/71392f5d/SYNERGIA_CORE_NEXT_PRO

No se encontró:

SYNERGIA_CORE_NEXT_RECOVERY

La copia de MAQ2 está vinculada al checkpoint del 20/07/2026 y parece anterior a los ajustes realizados posteriormente durante STAGE 6.1T, STAGE 6.1O y STAGE 6.2.

4. RESULTADO DE GIT

Rama:

synergia_v3_core_restructure

Commit:

b25909e3

Descripción:

feat: add Incident Manager ACEA and FASE 6.13 node cluster checkpoint

Tag:

SYNERGIA_OMEGA_NODE_SYNC_READY_20_07_2026

Remote:

origin git@github.com:AgentArchitectDev/SYNERGIA_CORE_NEXT_PRO.git

Cambios locales sin seguimiento:

docs/CHECKPOINTS/20_07_2026/BIBLIA SYNERGIA
TOMO 20_07_2026
OMEGA NODE EVOLUTION.md

docs/CHECKPOINTS/20_07_2026/MANUAL_INGRESO_NODO_SYNERGIA_OMEGA_20_07_2026.md

docs/CHECKPOINTS/20_07_2026/TOMO_20_07_2026_SYNERGIA_OMEGA_NODE_EVOLUTION.md
Restricción

NO ejecutar:

git reset
git clean

NO borrar los archivos locales anteriores.

NO hacer git pull ni sincronización masiva hasta comparar y proteger el estado local.

5. PYTHON Y ENTORNOS

Python del sistema:

/usr/bin/python3
Python 3.12.3

Entornos detectados:

.venv
venv

El entorno activado y confirmado fue:

source .venv/bin/activate

Python activo:

/mnt/71392f5d/SYNERGIA_CORE_NEXT_PRO/.venv/bin/python
Python 3.12.3

El .venv existe y funciona, pero está incompleto para el runtime AI.

6. OLLAMA EN MAQ2

Versión:

ollama version is 0.18.2

Modelos instalados:

llama3.2:3b
deepseek-coder-v2:16b
qwen2.5-coder:7b
llama3:latest
llama3.1:latest
mistral:latest
llama3:8b
phi3:3.8b
phi3:latest
phi3:mini
codellama:7b
codellama:latest
deepseek-coder:6.7b
gemma3:4b

Observación:

MAQ2 NO tiene llama3.2:1b.
MAQ2 sí tiene llama3.2:3b, configurado en los archivos de MAQ1 y MAQ2.
MAQ2 tiene modelos más grandes para tareas de desarrollo, análisis y validación.
7. MÓDULOS AI BUSINESS DETECTADOS

Archivos presentes:

ai/business/branding_generator.py
ai/business/business_generator.py
ai/business/docs_generator.py
ai/business/project_builder.py
ai/business/social_generator.py
ai/business/website_generator.py

También existen varios orquestadores:

ai/agents/orchestrator.py
ai/core/orchestrator.py
ai/core/orchestrator_core/orchestrator.py
ai/core_system/core/ai_orchestrator.py
ai/node/node_orchestrator.py
ai/runtime/orchestrator.py
8. HALLAZGO IMPORTANTE: API FUNCIONAL, NO BASADA EN CLASES

El intento de importar:

from ai.business.project_builder import ProjectBuilder

falló con:

ImportError: cannot import name 'ProjectBuilder'

Esto NO significa que el módulo esté roto.

project_builder.py usa una función:

create_project_structure(project_name)

No existe una clase ProjectBuilder.

La función:

crea outputs/<nombre_proyecto>;
crea las carpetas:
website
branding
social
docs
exports
business_plan
devuelve el Path raíz.

La interfaz correcta es:

from ai.business.project_builder import create_project_structure
9. BUSINESS GENERATOR

El archivo ai/business/business_generator.py tampoco define una clase BusinessGenerator.

La función principal es:

create_business_project(prompt)

Flujo actual:

create_business_project(prompt)
        |
        +-- create_project_structure()
        |
        +-- WEBSITE
        |      +-- generate_website()
        |
        +-- BRANDING
        |      +-- generate_branding()
        |
        +-- SOCIAL
        |      +-- generate_social()
        |
        +-- DOCS
               +-- generate_docs()

El generador:

crea un timestamp;
genera un nombre de proyecto a partir del prompt;
crea la estructura de salida;
selecciona modelos mediante ai_orchestrator.select_model(...);
agrega tareas a task_engine;
ejecuta las tareas;
devuelve la ruta del proyecto generado.
10. PROBLEMA REAL N.º 1 — DEPENDENCIAS FALTANTES

Al importar el proveedor apareció:

ModuleNotFoundError: No module named 'requests'

La cadena fue:

ai.integration.providers.__init__
    |
    +-- ollama_connector.py
            |
            +-- import requests

El .venv no tiene requests.

Tampoco se confirmó instalado el paquete Python ollama.

El requirements.txt actual contiene únicamente:

PySide6==6.11.1
PySide6_Addons==6.11.1
PySide6_Essentials==6.11.1
shiboken6==6.11.1

Por lo tanto, requirements.txt está incompleto para el runtime AI.

Aún NO se instaló nada

No ejecutar instalaciones hasta revisar el resto de los módulos y definir la corrección mínima.

11. PROBLEMA REAL N.º 2 — RUTAS DE PROVEEDOR INCONSISTENTES

Los generadores AI BUSINESS importan:

from ai.providers.ollama_provider import OllamaProvider

Pero en MAQ2 no existe:

ai/providers/

El proveedor real está en:

ai/integration/providers/ollama_provider.py

Además existen:

ai/integration/providers/__init__.py
ai/integration/providers/ollama_connector.py
ai/integration/providers/ollama_provider.py
ai/integration/providers/registry.py
ai/integration/providers/gemini_provider.py
ai/integration/providers/groq_provider.py
ai/integration/providers/openai_provider.py

Esto indica una inconsistencia de rutas o un puente de compatibilidad faltante, probablemente corregido en MAQ1 durante STAGE 6.1T.

12. CONFIGURACIÓN DE MODELOS

Se detectó:

config/maq2_dev.json
ollama_model = llama3.2:3b
provider = ollama

También:

config/maq1_dev.json
ollama_model = llama3.2:3b
provider = ollama

El proveedor real ai/integration/providers/ollama_provider.py tiene por defecto:

def generate(self, prompt, model="llama3.2:3b"):
13. DIAGNÓSTICO CONSOLIDADO

MAQ2:

✅ Hardware y nodo operativo.
✅ Python 3.12.3.
✅ .venv activable.
✅ Ollama 0.18.2.
✅ Modelos locales disponibles.
✅ Arquitectura V3 completa.
✅ Archivos AI BUSINESS presentes.
✅ Project Builder implementado.
✅ Business Generator implementado.
⚠️ API basada en funciones, no clases.
⚠️ .venv incompleto.
⚠️ Falta requests.
⚠️ Posiblemente falta el paquete Python ollama.
⚠️ requirements.txt no representa las dependencias AI.
⚠️ Falta o está rota la ruta ai.providers.
⚠️ No se debe ejecutar todavía el pipeline completo.
⚠️ No se debe sincronizar masivamente desde MAQ1.
⚠️ No se deben borrar los tres documentos locales no rastreados.
14. PUNTO DE REANUDACIÓN OFICIAL
CHECKPOINT_03_08_2026_MAQ2_AI_BUSINESS_DIAGNOSTIC

Continuar desde:

Inspección de los cuatro generadores AI BUSINESS, del ai_orchestrator, del task_engine y del proveedor Ollama real, antes de instalar dependencias o modificar rutas.

Ejecutar exactamente este bloque:

echo "===== WEBSITE GENERATOR ====="
sed -n '1,220p' ai/business/website_generator.py

echo
echo "===== BRANDING GENERATOR ====="
sed -n '1,220p' ai/business/branding_generator.py

echo
echo "===== SOCIAL GENERATOR ====="
sed -n '1,220p' ai/business/social_generator.py

echo
echo "===== DOCS GENERATOR ====="
sed -n '1,220p' ai/business/docs_generator.py

echo
echo "===== AI ORCHESTRATOR ====="
sed -n '1,280p' ai/core/ai_orchestrator.py

echo
echo "===== TASK ENGINE ====="
sed -n '1,260p' ai/core/task_engine.py

echo
echo "===== OLLAMA PROVIDER REAL ====="
sed -n '1,180p' ai/integration/providers/ollama_provider.py

Pegar la salida completa en la nueva conversación o nueva IA.

15. PLAN INMEDIATO DESPUÉS DE LA INSPECCIÓN

La siguiente IA debe:

revisar las interfaces reales de los cuatro generadores;
revisar cómo se importa OllamaProvider;
revisar ai_orchestrator.select_model(...);
revisar el funcionamiento de task_engine;
definir una corrección mínima y reversible;
completar las dependencias faltantes del .venv;
corregir o restaurar el puente:
ai.providers
        ->
ai.integration.providers
validar imports reales;
probar primero Social Generator;
probar Docs Generator;
integrar Business Generator;
ejecutar una prueba end-to-end;
guardar un nuevo checkpoint.
16. RESTRICCIONES DE CONTINUIDAD

La nueva IA debe respetar:

NO reiniciar SYNERGIA.
NO volver a fases anteriores.
NO rediseñar la arquitectura V3.
NO reemplazar todo MAQ2 con MAQ1.
NO ejecutar git reset.
NO ejecutar git clean.
NO borrar los documentos locales.
NO hacer git pull sin analizar primero divergencias.
NO editar código antes de terminar la inspección pendiente.
NO asumir clases donde la arquitectura usa funciones.
Mantener MAQ2 como nodo principal de validación y referencia estable.
Aplicar cambios pequeños, verificables y reversibles.
17. CONTEXTO DE NODOS
MAQ1 — Casa: 8 GB RAM, notebook más antigua, nodo de recuperación y pruebas livianas.
MAQ2 — Trabajo: 16 GB RAM, nodo principal de validación y referencia estable.
MAQ3 — Casa: 16 GB RAM, candidata a AI LAB y pruebas de modelos.
18. FRASE DE ARRANQUE PARA OTRA IA

Copiar y pegar:

Estamos retomando SYNERGIA OS – AI New Generation en MAQ2. No reinicies ni redefinas la arquitectura. Lee el checkpoint CHECKPOINT_03_08_2026_MAQ2_AI_BUSINESS_DIAGNOSTIC.md y continúa exactamente desde la sección “PUNTO DE REANUDACIÓN OFICIAL”. Primero ejecutaremos la inspección pendiente de los generadores, ai_orchestrator, task_engine y OllamaProvider. No hacer git pull, git reset, git clean, instalaciones ni cambios de código antes de analizar esa salida.

FIN DEL CHECKPOINT — 03/08/2026
"""
path = Path("/mnt/data/CHECKPOINT_03_08_2026_MAQ2_AI_BUSINESS_DIAGNOSTIC.md")
path.write_text(content, encoding="utf-8")
print(path)

Pensó durante 39s

GAB, quedó generado el checkpoint completo y autocontenido con todo el estado de MAQ2, diagnósticos, resultados, errores, arquitectura detectada, restricciones, punto exacto de reanudación y el bloque de comandos pendiente.

📄 
CHECKPOINT_03_08_2026_MAQ2_AI_BUSINESS_DIAGNOSTIC.md

Para continuar en otro perfil o en otra IA, subí ese archivo y escribí:

Estamos retomando SYNERGIA OS – AI New Generation en MAQ2. Leé el checkpoint completo y continuá exactamente desde el PUNTO DE REANUDACIÓN OFICIAL. No reinicies ni redefinas la arquitectura.

El checkpoint deja establecido como punto de retorno:

CHECKPOINT_03_08_2026_MAQ2_AI_BUSINESS_DIAGNOSTIC

La próxima tarea es inspeccionar los cuatro generadores, ai_orchestrator, task_engine y el proveedor real de Ollama. Todavía no se instalaron dependencias ni se modificó código.

CHECKPOINT_03_08_2026_MAQ2_AI_BUSINESS_DIAGNOSTIC.md
Documento
seguir  el analisis

Perfecto, GAB. Retomamos exactamente desde el checkpoint del 03/08/2026, en MAQ2, sin reiniciar nada y sin modificar código todavía.

Estamos en este punto:

MAQ2
└── /mnt/71392f5d/SYNERGIA_CORE_NEXT_PRO
    ├── rama: synergia_v3_core_restructure
    ├── Python 3.12.3
    ├── .venv activo
    ├── Ollama 0.18.2
    ├── llama3.2:3b disponible
    ├── AI BUSINESS presente
    ├── requirements.txt incompleto
    └── posible puente faltante:
        ai.providers → ai.integration.providers

Ahora necesitamos ver cómo están implementados realmente los generadores y el núcleo que los coordina. Ejecutá este bloque completo, sin cambiar nada:

echo "===== WEBSITE GENERATOR ====="
sed -n '1,220p' ai/business/website_generator.py

echo
echo "===== BRANDING GENERATOR ====="
sed -n '1,220p' ai/business/branding_generator.py

echo
echo "===== SOCIAL GENERATOR ====="
sed -n '1,220p' ai/business/social_generator.py

echo
echo "===== DOCS GENERATOR ====="
sed -n '1,220p' ai/business/docs_generator.py

echo
echo "===== AI ORCHESTRATOR ====="
sed -n '1,280p' ai/core/ai_orchestrator.py

echo
echo "===== TASK ENGINE ====="
sed -n '1,260p' ai/core/task_engine.py

echo
echo "===== OLLAMA PROVIDER REAL ====="
sed -n '1,180p' ai/integration/providers/ollama_provider.py

Pegame la salida completa.

Con esa salida vamos a determinar si el problema es solamente:

dependencias faltantes
+
ruta de importación antigua

o si además hay diferencias en las firmas de las funciones.

Después haremos la corrección en este orden:

Validar las firmas reales de generate_website, generate_branding, generate_social y generate_docs.
Revisar cómo ai_orchestrator.select_model() elige el modelo.
Confirmar que task_engine ejecuta las cuatro tareas correctamente.
Instalar únicamente las dependencias necesarias dentro de .venv.
Crear un puente de compatibilidad mínimo para ai.providers, si corresponde.
Ejecutar una prueba aislada de Social Generator.
Validar Docs Generator.
Ejecutar el pipeline completo con create_business_project().

Por ahora, el sistema está en una etapa de auditoría técnica controlada. El objetivo es recuperar la ejecución AI BUSINESS de MAQ2 sin reemplazar su arquitectura V3 ni mezclar código de manera masiva.

(.venv) gerardoalbertobergoglio@gerardoalbertobergoglio-H510M-S2H:/mnt/71392f5d/SYNERGIA_CORE_NEXT_PRO$ echo "===== WEBSITE GENERATOR ====="
sed -n '1,220p' ai/business/website_generator.py

echo
echo "===== BRANDING GENERATOR ====="
sed -n '1,220p' ai/business/branding_generator.py

echo
echo "===== SOCIAL GENERATOR ====="
sed -n '1,220p' ai/business/social_generator.py

echo
echo "===== DOCS GENERATOR ====="
sed -n '1,220p' ai/business/docs_generator.py

echo
echo "===== AI ORCHESTRATOR ====="
sed -n '1,280p' ai/core/ai_orchestrator.py

echo
echo "===== TASK ENGINE ====="
sed -n '1,260p' ai/core/task_engine.py

echo
echo "===== OLLAMA PROVIDER REAL ====="
sed -n '1,180p' ai/integration/providers/ollama_provider.py
===== WEBSITE GENERATOR =====
from pathlib import Path

from ai.providers.ollama_provider import (
    OllamaProvider
)


# =========================================================
# WEBSITE GENERATOR
# =========================================================

print(

    "[WEBSITE GENERATOR LOADED]"
)


# =========================================================
# GENERATE WEBSITE
# =========================================================

def generate_website(

    prompt,

    project_path,

    model
):

    provider = OllamaProvider()

    # =====================================================
    # AI PROMPT
    # =====================================================

    ai_prompt = f"""

    Crear estructura web profesional para:

    {prompt}

    Generar:

    - Landing page
    - Secciones
    - SEO
    - CTA
    - Diseño moderno
    - Estrategia web

    """

    # =====================================================
    # GENERATE
    # =====================================================

    response = provider.generate(

        prompt=ai_prompt,

        model=model
    )

    # =====================================================
    # SAVE
    # =====================================================

    output_file = (

        Path(project_path)

        / "website"

        / "website.txt"
    )

    with open(

        output_file,

        "w",

        encoding="utf-8"
    ) as f:

        f.write(response)

    print(

        f"\n[WEBSITE GENERATED]\n{output_file}"
    )

===== BRANDING GENERATOR =====
from pathlib import Path

from ai.providers.ollama_provider import (
    OllamaProvider
)


# =========================================================
# BRANDING GENERATOR
# =========================================================

print(

    "[BRANDING GENERATOR LOADED]"
)


# =========================================================
# GENERATE BRANDING
# =========================================================

def generate_branding(

    prompt,

    project_path,

    model
):

    provider = OllamaProvider()

    # =====================================================
    # AI PROMPT
    # =====================================================

    ai_prompt = f"""

    Crear branding profesional para:

    {prompt}

    Generar:

    - naming
    - slogans
    - identidad visual
    - colores
    - branding moderno
    - concepto de marca
    - estilo visual
    - tono comunicacional

    """

    # =====================================================
    # GENERATE
    # =====================================================

    response = provider.generate(

        prompt=ai_prompt,

        model=model
    )

    # =====================================================
    # SAVE TXT
    # =====================================================

    output_file = (

        Path(project_path)

        / "branding"

        / "branding.txt"
    )

    with open(

        output_file,

        "w",

        encoding="utf-8"
    ) as f:

        f.write(response)

    print(

        f"\n[BRANDING GENERATED]\n{output_file}"
    )

===== SOCIAL GENERATOR =====
from pathlib import Path

from ai.providers.ollama_provider import (
    OllamaProvider
)


# =========================================================
# SOCIAL GENERATOR
# =========================================================

print(

    "[SOCIAL GENERATOR LOADED]"
)


# =========================================================
# GENERATE SOCIAL
# =========================================================

def generate_social(

    prompt,

    project_path,

    model
):

    provider = OllamaProvider()

    # =====================================================
    # AI PROMPT
    # =====================================================

    ai_prompt = f"""

    Crear estrategia completa de redes sociales para:

    {prompt}

    Generar:

    - Instagram
    - TikTok
    - Facebook
    - campañas
    - hashtags
    - reels
    - copies
    - calendario contenido
    - ideas virales
    - automatización social

    """

    # =====================================================
    # GENERATE
    # =====================================================

    response = provider.generate(

        prompt=ai_prompt,

        model=model
    )

    # =====================================================
    # SAVE TXT
    # =====================================================

    output_file = (

        Path(project_path)

        / "social"

        / "social.txt"
    )

    with open(

        output_file,

        "w",

        encoding="utf-8"
    ) as f:

        f.write(response)

    print(

        f"\n[SOCIAL GENERATED]\n{output_file}"
    )

===== DOCS GENERATOR =====
from pathlib import Path

from ai.providers.ollama_provider import (
    OllamaProvider
)


# =========================================================
# DOCS GENERATOR
# =========================================================

print(

    "[DOCS GENERATOR LOADED]"
)


# =========================================================
# GENERATE DOCS
# =========================================================

def generate_docs(

    prompt,

    project_path,

    model
):

    provider = OllamaProvider()

    # =====================================================
    # AI PROMPT
    # =====================================================

    ai_prompt = f"""

    Crear documentación profesional para:

    {prompt}

    Generar:

    - propuesta comercial
    - pitch
    - presupuesto
    - documentación técnica
    - roadmap
    - objetivos
    - estrategia negocio
    - presentación profesional

    """

    # =====================================================
    # GENERATE
    # =====================================================

    response = provider.generate(

        prompt=ai_prompt,

        model=model
    )

    # =====================================================
    # SAVE TXT
    # =====================================================

    output_file = (

        Path(project_path)

        / "docs"

        / "docs.txt"
    )

    with open(

        output_file,

        "w",

        encoding="utf-8"
    ) as f:

        f.write(response)

    print(

        f"\n[DOCS GENERATED]\n{output_file}"
    )

===== AI ORCHESTRATOR =====
sed: no se puede leer ai/core/ai_orchestrator.py: No existe el archivo o el directorio

===== TASK ENGINE =====
class TaskEngine:

    def execute(self, user_input, context=None):

        text = user_input.lower()

        if "calcular" in text:
            return self._calc(user_input)

        if "estado" in text:
            return {"status": "system_ok"}

        return {
            "status": "executed",
            "task": user_input,
            "analysis": "generic_task_handled"
        }

    def _calc(self, text):
        return {
            "type": "calc",
            "result": "simulación de cálculo (placeholder)"
        }

===== OLLAMA PROVIDER REAL =====
import ollama
import time


# =========================================================
# OLLAMA PROVIDER
# =========================================================

print("[OLLAMA PROVIDER LOADED]")


class OllamaProvider:

    # =====================================================
    # GENERATE (ROBUSTO + DEBUG + FALLBACK)
    # =====================================================

    def generate(self, prompt, model="llama3.2:3b"):

        try:
            print("\n[OLLAMA CALL]")
            print(f"MODEL: {model}")

            start_time = time.time()

            # =================================================
            # CALL OLLAMA
            # =================================================

            response = ollama.chat(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            end_time = time.time()

            duration = round(end_time - start_time, 2)

            print(f"[OLLAMA OK] time={duration}s")

            # =================================================
            # EXTRACT RESPONSE
            # =================================================

            content = response.get("message", {}).get("content", "")

            if not content:

                return "[OLLAMA ERROR] empty response"

            return content

        except Exception as e:

            print("\n[OLLAMA ERROR]")
            print(str(e))

            return f"[OLLAMA FAIL] {str(e)}"

    # =====================================================
    # SIMPLE GENERATE (compatibilidad futura)
    # =====================================================

    def simple(self, prompt):

        return self.generate(prompt)
(.venv) gerardoalbertobergoglio@gerardoalbertobergoglio-H510M-S2H:/mnt/71392f5d/SYNERGIA_CORE_NEXT_PRO$ 

GAB, esta salida permitió detectar el problema central de MAQ2. Ya no estamos ante una hipótesis: la cadena de fallas quedó localizada.

Diagnóstico técnico consolidado

Los cuatro generadores están bien alineados entre sí:

website_generator.py
branding_generator.py
social_generator.py
docs_generator.py

Todos usan la misma firma:

generate_xxx(
    prompt,
    project_path,
    model
)

Y todos llaman:

provider = OllamaProvider()

response = provider.generate(
    prompt=ai_prompt,
    model=model
)

El proveedor real también es compatible con esa llamada:

class OllamaProvider:

    def generate(
        self,
        prompt,
        model="llama3.2:3b"
    ):

Por lo tanto, las firmas son compatibles. No hay que reescribir los generadores.

El problema está en las capas que conectan esos módulos.

Problema A — puente de importación faltante

Los cuatro generadores hacen:

from ai.providers.ollama_provider import OllamaProvider

Pero ai/providers/ no existe.

El proveedor real está en:

ai/integration/providers/ollama_provider.py

La corrección más segura no es modificar los cuatro generadores. Es restaurar una capa de compatibilidad:

ai.providers.ollama_provider
             │
             ▼
ai.integration.providers.ollama_provider

Eso preserva la API existente y evita tocar cuatro archivos que ya están estructuralmente correctos.

Problema B — falta el paquete Python ollama

El proveedor comienza con:

import ollama

Y antes vimos que el .venv no mostró instalado ollama. Por lo tanto, debemos instalarlo dentro del entorno virtual.

Problema C — el orquestador esperado no está en esa ruta

El archivo:

ai/core/ai_orchestrator.py

no existe.

Pero business_generator.py intenta importar:

from ai.core.ai_orchestrator import ai_orchestrator

Esto es una segunda incompatibilidad de rutas.

En el inventario anterior sí apareció:

ai/core_system/core/ai_orchestrator.py

También existen otros orquestadores:

ai/core/orchestrator.py
ai/core/orchestrator_core/orchestrator.py
ai/agents/orchestrator.py
ai/runtime/orchestrator.py

Todavía no debemos elegir uno por nombre. Tenemos que encontrar cuál exporta exactamente:

ai_orchestrator
Problema D — task_engine.py no coincide con lo que necesita AI BUSINESS

El TaskEngine actual solo tiene:

execute(user_input, context=None)

y:

_calc(text)

Pero business_generator.py necesita:

task_engine.tasks = []

task_engine.add_task(...)

task_engine.run()

Esas funciones no aparecen en el archivo inspeccionado.

Esto significa que el pipeline completo fallaría incluso después de corregir Ollama y las rutas de importación.

La situación real queda así:

AI BUSINESS
│
├── Generadores ─────────────── OK
│
├── Firmas de funciones ─────── OK
│
├── OllamaProvider ──────────── OK en diseño
│       └── falta dependencia Python
│
├── ai.providers ────────────── FALTA puente
│
├── ai.core.ai_orchestrator ─── FALTA o cambió de ruta
│
└── task_engine ─────────────── API incompatible

El siguiente paso es identificar los módulos reales que ya existen en MAQ2, para reutilizarlos en lugar de inventar otra implementación.

Ejecutá este bloque:

echo "===== BUSCAR AI ORCHESTRATOR ====="
find ai -type f -name "*orchestrator*.py" -print

echo
echo "===== EXPORTACIONES AI_ORCHESTRATOR ====="
grep -Rni \
"ai_orchestrator" \
ai 2>/dev/null | head -100

echo
echo "===== BUSCAR TASK ENGINE ====="
find ai -type f \
\( -name "*task*engine*.py" -o -name "*task*.py" \) \
-print

echo
echo "===== add_task Y run ====="
grep -RniE \
"def add_task|def run|task_engine" \
ai 2>/dev/null | head -150

echo
echo "===== CONTENIDO DE POSIBLE ORQUESTADOR ====="
sed -n '1,320p' \
ai/core_system/core/ai_orchestrator.py \
2>/dev/null

echo
echo "===== CORE ORCHESTRATOR ====="
sed -n '1,320p' \
ai/core/orchestrator.py \
2>/dev/null

echo
echo "===== ESTRUCTURA DE AI/CORE ====="
find ai/core -maxdepth 3 -type f | sort

Pegame la salida completa.

Con eso vamos a decidir si:

existe un ai_orchestrator funcional que solo necesita un puente de compatibilidad;
existe un TaskEngine antiguo con add_task() y run();
o debemos crear dos adaptadores pequeños y reversibles.

La corrección probable será mediante compatibilidad, no mediante reescritura:

ai/business
      │
      ├── adaptador ai.providers
      │
      ├── adaptador ai.core.ai_orchestrator
      │
      └── adaptador TaskEngine

Así mantenemos intacta la arquitectura V3 de MAQ2 y recuperamos el pipeline AI BUSINESS de forma controlada.
