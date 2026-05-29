# SYNERGIA OS v3 — Architecture Map

---

# CORE

## cognitive_kernel
STATUS: LEGACY -> MIGRATE
DESTINATION: core/kernel

FILES:
- event_bus.py
- kernel.py
- runtime_manager.py
- state_engine.py
- task_engine.py

---

# AI

## ai_layer
STATUS: LEGACY -> MIGRATE
DESTINATION: ai/

MODULES:
- agents/
- memory/
- orchestrator/
- ai_engine.py

---

# VISUAL

## visual_os
STATUS: LEGACY UI
DESTINATION: apps/visual_os

## visual_os_v2
STATUS: ACTIVE DEMO
DESTINATION: apps/visual_os

---

# BUILD SYSTEM

## builder_engine
STATUS: ACTIVE
DESTINATION: core/orchestrator OR builders/

---

# OUTPUT

## output_engine
STATUS: ACTIVE
DESTINATION: outputs/

---

# CONTROL

## control_center
STATUS: ACTIVE
DESTINATION: apps/control_center

---

# DATA

## memory/
STATUS: ACTIVE
DESTINATION: runtime_data/memory

## logs/
STATUS: ACTIVE
DESTINATION: runtime_data/logs

## projects/
STATUS: ACTIVE
DESTINATION: runtime_data/projects

---

# NEXT PHASE

1. normalize imports
2. move runtime systems
3. create centralized config
4. create websocket runtime
5. live agent communication layer
6. persistent runtime memory
7. distributed runtime execution
