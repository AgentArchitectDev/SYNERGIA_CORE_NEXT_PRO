from pathlib import Path

from ai.providers.ollama_provider import (
    OllamaProvider
)

from ai.core_system.core.ai_orchestrator import (
    ai_orchestrator
)


# =========================================================
# BRANDING GENERATOR
# SYNERGIA CORE NEXT PRO
#
# STAGE 6.3.8.2
# AI ORCHESTRATOR INTEGRATION
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

    model=None

):


    provider = OllamaProvider()



    # =====================================================
    # ADAPTIVE MODEL SELECTION
    # =====================================================


    if model is None:

        model = ai_orchestrator.select_model(
            "branding"
        )



    print()

    print(
        f"[BRANDING MODEL] {model}"
    )



    # =====================================================
    # AI PROMPT
    # =====================================================


    ai_prompt = f"""

Crear identidad de marca profesional para:

{prompt}


Generar:

- Nombre de marca
- Concepto
- Identidad visual
- Colores sugeridos
- Tipografía
- Personalidad de marca
- Diferenciación comercial
- Eslogan


Responder con estructura clara.

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

        / "branding"

        / "branding.txt"

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
        "[BRANDING GENERATED]"
    )

    print(
        output_file
    )



    return {

        "module": "branding",

        "model": model,

        "file": str(output_file),

        "status": "completed"

    }
