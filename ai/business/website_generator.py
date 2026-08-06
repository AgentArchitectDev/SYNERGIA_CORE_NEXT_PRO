from pathlib import Path

from ai.providers.ollama_provider import (
    OllamaProvider
)

from ai.core_system.core.ai_orchestrator import (
    ai_orchestrator
)


# =========================================================
# WEBSITE GENERATOR
# SYNERGIA CORE NEXT PRO
#
# STAGE 6.3.8.1
# AI ORCHESTRATOR INTEGRATION
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

    model=None

):


    provider = OllamaProvider()



    # =====================================================
    # ADAPTIVE MODEL SELECTION
    # =====================================================


    if model is None:

        model = ai_orchestrator.select_model(
            "website"
        )



    print()

    print(
        f"[WEBSITE MODEL] {model}"
    )



    # =====================================================
    # AI PROMPT
    # =====================================================


    ai_prompt = f"""

Crear estructura web profesional para:

{prompt}


Generar:

- Landing page
- Secciones principales
- SEO
- CTA
- Diseño moderno
- Experiencia usuario
- Estrategia web


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

        / "website"

        / "website.txt"

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
        "[WEBSITE GENERATED]"
    )

    print(
        output_file
    )



    return {

        "module": "website",

        "model": model,

        "file": str(output_file),

        "status": "completed"

    }
