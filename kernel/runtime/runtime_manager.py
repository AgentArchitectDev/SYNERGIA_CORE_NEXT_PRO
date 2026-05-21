# =========================================================
# SYNERGIA CORE NEXT PRO
# RUNTIME MANAGER
# =========================================================

import time

from kernel.state.state_manager import StateManager


class RuntimeManager:

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        self.mode = "DEV"

    # =====================================================
    # INITIALIZE RUNTIME
    # =====================================================

    def initialize(self):

        print("\n========================================")
        print("⚡ SYNERGIA RUNTIME START")
        print("========================================")

        print("\n[RUNTIME] Initializing runtime...")

        time.sleep(1)

        print(f"[RUNTIME] MODE => {self.mode}")

        time.sleep(1)

        print("[RUNTIME] Runtime services online.")

        time.sleep(1)

        print("[RUNTIME] AI Kernel ready.")

        time.sleep(1)

        print("\n[RUNTIME] Loading State Engine...")

        time.sleep(1)

        StateManager.show()

        print("\n========================================")
        print("✅ RUNTIME FULLY INITIALIZED")
        print("========================================\n")

    # =====================================================
    # GET MODE
    # =====================================================

    def current_mode(self):

        return self.mode
