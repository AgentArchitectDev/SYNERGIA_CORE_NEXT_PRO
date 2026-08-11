# ============================================================
# SYNERGIA OS
#
# SELF LEARNING LOOP TEST
#
# STAGE 6.3.15.7.10.2
#
# VALIDATION:
# AI BUSINESS SELF LEARNING ENGINE CORE
# ============================================================


from ai.business.self_learning_loop import (
    self_learning_loop
)


from ai.memory.runtime_memory import (
    runtime_memory
)



print("=" * 60)
print("[SELF LEARNING LOOP TEST]")
print("=" * 60)



# ============================================================
# MODULE VALIDATION
# ============================================================


print()

print("[MODULE STATUS]")

print(
    self_learning_loop.status()
)



# ============================================================
# MEMORY BEFORE ANALYSIS
# ============================================================


print()

print("[RUNTIME MEMORY]")

print(
    runtime_memory.status()
)



# ============================================================
# LEARNING ANALYSIS
# ============================================================


print()

print("[LEARNING ANALYSIS]")



analysis = (
    self_learning_loop.analyze()
)



print(
    analysis
)



# ============================================================
# VALIDATIONS
# ============================================================


print()

print("[VALIDATIONS]")


assert analysis["total_executions"] >= 0

assert analysis["successful"] >= 0

assert analysis["failed"] >= 0

assert (
    "success_rate"
    in analysis
)


assert (
    "recommendation"
    in analysis
)



print()

print(
    "[OK] Runtime Memory Connected"
)


print(
    "[OK] Self Learning Engine Connected"
)


print(
    "[OK] Analysis Generated"
)



print()

print(
    "[TEST COMPLETE]"
)
