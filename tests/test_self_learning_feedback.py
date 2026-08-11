# ============================================================
# SYNERGIA OS
#
# TEST SELF LEARNING FEEDBACK ENGINE
#
# STAGE 6.3.15.7.10.3
#
# ============================================================


import sys
from pathlib import Path


# Permitir importar SYNERGIA desde /tests
sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)


from ai.business.self_learning_feedback import (
    self_learning_feedback
)



print("")
print("# [SELF LEARNING FEEDBACK TEST]")
print("")


# ============================================================
# MODULE STATUS
# ============================================================

print("[MODULE STATUS]")

print(
    self_learning_feedback.status()
)


# ============================================================
# GENERATE FEEDBACK
# ============================================================

print("")
print("[FEEDBACK GENERATION]")

feedback = (
    self_learning_feedback.generate()
)


print(feedback)



# ============================================================
# VALIDATIONS
# ============================================================

print("")
print("[VALIDATIONS]")
print("")


assert (
    feedback["source"]
    ==
    "SELF_LEARNING_LOOP"
)

print(
    "[OK] Learning Loop Connected"
)


assert (
    "router_feedback"
    in feedback
)

print(
    "[OK] Router Feedback Generated"
)


assert (
    feedback["success_rate"]
    >= 0
)

print(
    "[OK] Success Rate Valid"
)



print("")
print("[TEST COMPLETE]")
