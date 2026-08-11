# ============================================================
# SYNERGIA OS
#
# TEST AUTONOMOUS LEARNING OPTIMIZER
#
# STAGE 6.3.15.7.11.1
#
# ============================================================


import sys
from pathlib import Path


sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)


from ai.business.autonomous_learning_optimizer import (
    autonomous_learning_optimizer
)


print("")
print("# [AUTONOMOUS LEARNING OPTIMIZER TEST]")
print("")


print("[MODULE STATUS]")

print(
    autonomous_learning_optimizer.status()
)


print("")
print("[OPTIMIZATION RESULT]")


result = (
    autonomous_learning_optimizer.optimize()
)


print(result)



print("")
print("[VALIDATIONS]")
print("")


assert (
    result["source"]
    ==
    "AUTONOMOUS_LEARNING_OPTIMIZER"
)

print(
    "[OK] Optimizer Connected"
)


assert (
    "decision"
    in result
)

print(
    "[OK] Decision Generated"
)


assert (
    result["success_rate"]
    >= 0
)

print(
    "[OK] Learning Score Valid"
)


assert (
    result["decision"]["strategy"]
    is not None
)

print(
    "[OK] Strategy Generated"
)



print("")
print("[TEST COMPLETE]")
