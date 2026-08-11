# =========================================================
# SYNERGIA ADAPTIVE LEARNING SCORE TEST
#
# STAGE 6.3.15.7.7.4
# =========================================================

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT)
)

print("==============================")
print("[ADAPTIVE LEARNING SCORE TEST]")
print("==============================")


from ai.business.adaptive_model_router import (
    AdaptiveModelRouter
)

from ai.memory.runtime_memory import (
    runtime_memory
)



print("\n[MEMORY BEFORE]")
print(
    runtime_memory.status()
)



print("\n[ADDING EXPERIENCES]")


runtime_memory.add_experience(
    task="WEBSITE",
    model="llama3.2:3b",
    status="SUCCESS",
    duration_seconds=120
)


runtime_memory.add_experience(
    task="WEBSITE",
    model="gemma3:4b",
    status="SUCCESS",
    duration_seconds=250
)


runtime_memory.add_experience(
    task="WEBSITE",
    model="llama3.2:3b",
    status="SUCCESS",
    duration_seconds=110
)



print(
    runtime_memory.status()
)



print("\n[ROUTER TEST]")


router = AdaptiveModelRouter()


result = router.select_model(
    task="WEBSITE",
    default_model="mistral:latest"
)



print(result)



print("\n[TEST COMPLETE]")
