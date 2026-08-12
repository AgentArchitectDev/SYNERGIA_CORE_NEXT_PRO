#!/usr/bin/env python3

from ai.security.sovereign_escape import sovereign_escape
from ai.security.emergency_stop import emergency_stop
from ai.security.autonomy_off import autonomy_off
from ai.security.master_lock import master_security_lock
from ai.security.sovereign_security_core import sovereign_security_core


print("=" * 68)
print(" SYNERGIA S5.2")
print(" SOVEREIGN SECURITY NEGATIVE TEST")
print("=" * 68)


# ------------------------------------------------------------
# INITIAL STATE
# ------------------------------------------------------------

print()
print("===== INITIAL SECURITY STATE =====")

initial_escape = sovereign_escape.status()
initial_stop = emergency_stop.status()
initial_autonomy = autonomy_off.status()
initial_lock = master_security_lock.status()

print("SOVEREIGN ESCAPE:", initial_escape)
print("EMERGENCY STOP:", initial_stop)
print("AUTONOMY OFF:", initial_autonomy)
print("MASTER LOCK:", initial_lock)


# ------------------------------------------------------------
# ATTACK 1
# ------------------------------------------------------------

print()
print("===== ATTACK 1 =====")
print("OPTIMIZER -> DISABLE MASTER SECURITY LOCK")

attack_1 = sovereign_security_core.autonomous_request(
    component="AUTONOMOUS_LEARNING_OPTIMIZER",
    action="DISABLE_MASTER_SECURITY_LOCK",
)

print(attack_1)


# ------------------------------------------------------------
# ATTACK 2
# ------------------------------------------------------------

print()
print("===== ATTACK 2 =====")
print("ROUTER -> RESET EMERGENCY STOP")

attack_2 = sovereign_security_core.autonomous_request(
    component="ADAPTIVE_MODEL_ROUTER",
    action="RESET_EMERGENCY_STOP",
)

print(attack_2)


# ------------------------------------------------------------
# ATTACK 3
# ------------------------------------------------------------

print()
print("===== ATTACK 3 =====")
print("AGENT -> ACTIVATE SOVEREIGN ESCAPE")

attack_3 = sovereign_security_core.autonomous_request(
    component="AUTONOMOUS_AGENT",
    action="ACTIVATE_SOVEREIGN_ESCAPE",
)

print(attack_3)


# ------------------------------------------------------------
# ATTACK 4
# ------------------------------------------------------------

print()
print("===== ATTACK 4 =====")
print("MODEL -> REDEFINE ADMINISTRATOR")

attack_4 = sovereign_security_core.autonomous_request(
    component="LOCAL_AI_MODEL",
    action="REDEFINE_ADMINISTRATOR",
)

print(attack_4)


# ------------------------------------------------------------
# ATTACK 5
# ------------------------------------------------------------

print()
print("===== ATTACK 5 =====")
print("LEARNING LOOP -> CREATE NEW SOVEREIGN AUTHORITY")

attack_5 = sovereign_security_core.autonomous_request(
    component="SELF_LEARNING_LOOP",
    action="CREATE_NEW_SOVEREIGN_AUTHORITY",
)

print(attack_5)


# ------------------------------------------------------------
# FINAL STATE
# ------------------------------------------------------------

print()
print("===== FINAL SECURITY STATE =====")

final_escape = sovereign_escape.status()
final_stop = emergency_stop.status()
final_autonomy = autonomy_off.status()
final_lock = master_security_lock.status()

print("SOVEREIGN ESCAPE:", final_escape)
print("EMERGENCY STOP:", final_stop)
print("AUTONOMY OFF:", final_autonomy)
print("MASTER LOCK:", final_lock)


# ------------------------------------------------------------
# ASSERTIONS
# ------------------------------------------------------------

print()
print("===== SECURITY ASSERTIONS =====")

assert attack_1["status"] == "BLOCKED"
assert attack_2["status"] == "BLOCKED"
assert attack_3["status"] == "BLOCKED"
assert attack_4["status"] == "BLOCKED"
assert attack_5["status"] == "BLOCKED"

assert final_escape["active"] == initial_escape["active"]
assert final_stop["active"] == initial_stop["active"]
assert final_autonomy["active"] == initial_autonomy["active"]
assert final_lock["active"] == initial_lock["active"]

print("[OK] OPTIMIZER BLOCKED")
print("[OK] ROUTER BLOCKED")
print("[OK] AGENT BLOCKED")
print("[OK] MODEL BLOCKED")
print("[OK] LEARNING LOOP BLOCKED")

print("[OK] SOVEREIGN ESCAPE UNMODIFIED")
print("[OK] EMERGENCY STOP UNMODIFIED")
print("[OK] AUTONOMY OFF UNMODIFIED")
print("[OK] MASTER LOCK UNMODIFIED")

print()
print("=" * 68)
print(" [OK] STAGE 6.3.15.7.11.3-S5.2 PASSED")
print(" AUTONOMOUS SECURITY AUTHORITY: ZERO")
print("=" * 68)
