# ============================================
# SYNERGIA VISUAL OS BRIDGE v1 (STABLE CORE)
# ============================================

import sys
import os

# ============================================
# FIX: ROOT PATH DEL SISTEMA SYNERGIA
# ============================================

ROOT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../")
)

if ROOT_PATH not in sys.path:
    sys.path.insert(0, ROOT_PATH)

# ============================================
# IMPORT DEL BOOT (CORE SYSTEM)
# ============================================

try:
    from synergia_boot import SynergiaBoot
except Exception as e:
    print("❌ ERROR IMPORTANDO SYNERGIA BOOT:", e)
    SynergiaBoot = None


# ============================================
# SYNERGIA VISUAL EXECUTION BRIDGE
# ============================================

def run_synergia(task: str, mode: str):
    """
    Conecta Visual OS → Synergia Boot Engine
    """

    print("\n====================================")
    print("🚀 SYNERGIA VISUAL EXECUTION ENGINE")
    print("====================================\n")

    # Si el boot no está disponible
    if SynergiaBoot is None:
        return {
            "status": "ERROR",
            "message": "SynergiaBoot no disponible (problema de import)"
        }

    # Inicializar sistema
    system = SynergiaBoot()

    # ============================================
    # MODO AUTÓNOMO
    # ============================================
    if mode == "AUTONOMOUS":
        print("🤖 MODE: AUTONOMOUS")
        return system.start(task)

    # ============================================
    # MODO HÍBRIDO
    # ============================================
    elif mode == "HYBRID":
        print("🧠 MODE: HYBRID (Human + AI)")

        result = system.start(task)

        return {
            "mode": "HYBRID",
            "task": task,
            "result": result,
            "status": "completed"
        }

    # ============================================
    # MODO MANUAL
    # ============================================
    elif mode == "MANUAL":
        print("👤 MODE: MANUAL (no execution)")

        return {
            "mode": "MANUAL",
            "task_saved": task,
            "status": "waiting human approval"
        }

    # ============================================
    # MODO INVALIDO
    # ============================================
    else:
        return {
            "status": "ERROR",
            "message": f"Modo inválido: {mode}"
        }
