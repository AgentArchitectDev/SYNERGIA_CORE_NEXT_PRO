from pathlib import Path

from ai.providers.ollama_provider import (
    OllamaProvider
)

from ai.core_system.core.ai_orchestrator import (
    ai_orchestrator
)


# =========================================================
# DOCS GENERATOR
# SYNERGIA CORE NEXT PRO
#
# STAGE 6.3.8.4
# AI ORCHESTRATOR INTEGRATION
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

    model=None

):


    provider = OllamaProvider()



    # =====================================================
    # ADAPTIVE MODEL SELECTION
    # =====================================================


    if model is None:

        model = ai_orchestrator.select_model(
            "docs"
        )



    print()

    print(
        f"[DOCS MODEL] {model}"
    )



    # =====================================================
    # AI PROMPT
    # =====================================================


    ai_prompt = f"""

Crear documentación profesional para:

{prompt}


Generar:

- Descripción general
- Objetivos
- Características principales
- Arquitectura
- Guía de uso
- Recomendaciones
- Conclusión


Responder con formato documental claro.

"""



    # =====================================================
    # GENERATE
    # =====================================================


    response = provider.generate(

        prompt=ai_prompt,

        model=model

    )



    # =====================================================
    # SAVE OUTPUT
    # =====================================================


    output_file = (

        Path(project_path)

        / "docs"

        / "docs.txt"

    )


    output_file.parent.mkdir(

        parents=True,

        exist_ok=True

    )



    with open(

        output_file,

        "w",

        encoding="utf-8"

    ) as f:

        f.write(response)



    print()

    print(
        "[DOCS GENERATED]"
    )

    print(
        output_file
    )



    return {

        "module": "docs",

        "model": model,

        "file": str(output_file),

        "status": "completed"

    }
