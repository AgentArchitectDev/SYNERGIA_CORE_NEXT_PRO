from pathlib import Path

from ai.providers.ollama_provider import (
    OllamaProvider
)

from ai.core_system.core.ai_orchestrator import (
    ai_orchestrator
)


# =========================================================
# SOCIAL GENERATOR
# SYNERGIA CORE NEXT PRO
#
# STAGE 6.3.8.3
# AI ORCHESTRATOR INTEGRATION
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

    model=None

):


    provider = OllamaProvider()



    # =====================================================
    # ADAPTIVE MODEL SELECTION
    # =====================================================


    if model is None:

        model = ai_orchestrator.select_model(
            "social"
        )



    print()

    print(
        f"[SOCIAL MODEL] {model}"
    )



    # =====================================================
    # AI PROMPT
    # =====================================================


    ai_prompt = f"""

Crear estrategia de redes sociales profesional para:

{prompt}


Generar:

- Publicaciones iniciales
- Calendario de contenido
- Tono de comunicación
- Hashtags
- Estrategia de crecimiento
- Llamados a la acción
- Ideas para campañas


Responder con estructura organizada.

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

        / "social"

        / "social.txt"

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
        "[SOCIAL GENERATED]"
    )

    print(
        output_file
    )



    return {

        "module": "social",

        "model": model,

        "file": str(output_file),

        "status": "completed"

    }
