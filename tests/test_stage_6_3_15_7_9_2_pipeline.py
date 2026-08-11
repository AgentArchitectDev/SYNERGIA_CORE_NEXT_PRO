# =========================================================
# SYNERGIA CORE NEXT PRO
#
# STAGE 6.3.15.7.9.2
#
# REAL AUTONOMOUS BUSINESS PIPELINE
#
# END TO END EXECUTION TEST
#
# =========================================================


from datetime import datetime


from ai.business.business_generator import (
    create_business_project
)


from ai.memory.runtime_memory import (
    runtime_memory
)



print("=" * 70)

print(
    "[SYNERGIA STAGE 6.3.15.7.9.2]"
)

print(
    "[REAL AUTONOMOUS BUSINESS PIPELINE]"
)

print("=" * 70)



# =========================================================
# MEMORY BEFORE
# =========================================================


print()

print(
    "[MEMORY BEFORE EXECUTION]"
)


print(
    runtime_memory.status()
)



# =========================================================
# REAL BUSINESS PROMPT
# =========================================================


business_prompt = """

Crear una empresa de servicios digitales
basada en inteligencia artificial.

Debe incluir:

- sitio web profesional
- identidad visual
- estrategia de redes sociales
- documentación comercial

El objetivo es vender soluciones
de automatización para pequeñas empresas.

"""


print()

print(
    "[BUSINESS PROMPT]"
)

print(
    business_prompt
)



# =========================================================
# PROGRESS CALLBACK
# =========================================================


def progress(
    value,
    message
):

    print()

    print(
        f"[PROGRESS {value}%]"
    )

    print(
        message
    )



# =========================================================
# EXECUTE AUTONOMOUS PIPELINE
# =========================================================


started = datetime.now()



print()

print(
    "[PIPELINE START]"
)



result = create_business_project(

    prompt=business_prompt,

    progress_callback=progress

)



finished = datetime.now()



# =========================================================
# RESULT
# =========================================================


print()

print(
    "[PIPELINE FINISHED]"
)



print()

print(
    "STATUS:"
)

print(
    result["status"]
)



print()

print(
    "PROJECT:"
)

print(
    result["project"]
)



print()

print(
    "[VALIDATION]"
)


print(
    result["validation"]
)



# =========================================================
# MEMORY AFTER
# =========================================================


print()

print(
    "[MEMORY AFTER EXECUTION]"
)


print(
    runtime_memory.status()
)



# =========================================================
# SUMMARY
# =========================================================


print()

print("=" * 70)

print(
    "[STAGE 6.3.15.7.9.2 COMPLETE TEST]"
)

print("=" * 70)


print()

print(
    "START:"
)

print(
    started
)


print()

print(
    "END:"
)

print(
    finished
)


print()

print(
    "DURATION:"
)

print(
    finished-started
)
