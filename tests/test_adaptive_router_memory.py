# =========================================================
# SYNERGIA CORE NEXT PRO
#
# TEST:
# STAGE 6.3.15.7.7.3
#
# ADAPTIVE MODEL ROUTER
# +
# RUNTIME MEMORY INTEGRATION
#
# PURPOSE:
# Validar conexión entre:
#
# AdaptiveModelRouter
#        |
#        ↓
# RuntimeMemory
#        |
#        ↓
# Experiencias acumuladas
#
# =========================================================


import sys

from pathlib import Path


# =========================================================
# ROOT PROJECT PATH FIX
# Permite ejecutar:
#
# python tests/test_adaptive_router_memory.py
#
# =========================================================


ROOT = Path(__file__).resolve().parent.parent


sys.path.insert(
    0,
    str(ROOT)
)



print("==============================")
print("[ADAPTIVE ROUTER MEMORY TEST]")
print("==============================")



# =========================================================
# IMPORTS SYNERGIA
# =========================================================


from ai.business.adaptive_model_router import (
    AdaptiveModelRouter
)


from ai.memory.runtime_memory import (
    runtime_memory
)



print("\n[MODULES LOADED]")

print(
    "[OK] AdaptiveModelRouter"
)

print(
    "[OK] RuntimeMemory"
)



# =========================================================
# MEMORY BEFORE
# =========================================================


print("\n==============================")
print("[MEMORY STATUS BEFORE]")
print("==============================")


print(
    runtime_memory.status()
)



# =========================================================
# ADD EXPERIENCES
# =========================================================


print("\n==============================")
print("[ADDING RUNTIME EXPERIENCES]")
print("==============================")


runtime_memory.add_experience(

    task="WEBSITE",

    model="llama3.2:3b",

    status="SUCCESS",

    duration_seconds=120.5

)



runtime_memory.add_experience(

    task="WEBSITE",

    model="mistral:latest",

    status="SUCCESS",

    duration_seconds=300.0

)



runtime_memory.add_experience(

    task="BRANDING",

    model="gemma3:4b",

    status="SUCCESS",

    duration_seconds=240.0

)



print(
    runtime_memory.status()
)



# =========================================================
# ROUTER INITIALIZATION
# =========================================================


print("\n==============================")
print("[INITIALIZING ROUTER]")
print("==============================")


router = AdaptiveModelRouter()



print(
    router
)



# =========================================================
# MODEL SELECTION TEST
# =========================================================


print("\n==============================")
print("[MODEL SELECTION TEST]")
print("==============================")


decision_website = router.select_model(

    task="WEBSITE",

    default_model="gemma3:4b"

)



print(
    decision_website
)



decision_branding = router.select_model(

    task="BRANDING",

    default_model="llama3.2:3b"

)



print(
    decision_branding
)



# =========================================================
# FINAL MEMORY STATUS
# =========================================================


print("\n==============================")
print("[FINAL MEMORY STATUS]")
print("==============================")


print(
    runtime_memory.status()
)



print("\n==============================")
print("[TEST COMPLETE]")
print("==============================")


print("[EXIT CODE] 0")
