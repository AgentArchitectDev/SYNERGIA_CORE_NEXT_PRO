# ============================================
# MODE MANAGER
# ============================================

SYSTEM_MODE = "AUTONOMOUS"


def set_mode(mode: str):

    global SYSTEM_MODE
    SYSTEM_MODE = mode

    print(f"[SYNERGIA MODE] {SYSTEM_MODE}")


def get_mode():

    return SYSTEM_MODE
