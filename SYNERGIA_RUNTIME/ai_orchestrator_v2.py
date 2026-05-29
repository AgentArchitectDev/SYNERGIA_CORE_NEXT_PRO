import json
import os
import subprocess
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))

STATE_FILE = os.path.join(BASE, "system_state.json")
REGISTRY_FILE = os.path.join(BASE, "module_registry.json")

KERNEL_PATH = os.path.join(BASE, "kernel_loader.py")
SYNC_PATH = "/mnt/71392f5d/synergia-core/synergia_sync_system.sh"


class AIOrchestratorV2:

    def __init__(self):
        self.state = self.load_json(STATE_FILE)
        self.registry = self.load_json(REGISTRY_FILE)

    def load_json(self, path):
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
        return {}

    # =========================
    # ANALYSIS ENGINE
    # =========================
    def analyze(self):
        modules = self.registry.get("modules", [])
        status = self.state.get("status", "UNKNOWN")

        print("\n🧠 ORCHESTRATOR v2 ANALYSIS")
        print("STATE:", status)
        print("MODULES:", len(modules))

        if len(modules) == 0:
            return "INIT_MODULES"

        if status != "KERNEL_COMPLETED":
            return "RUN_KERNEL"

        return "SYNC_ONLY"

    # =========================
    # ACTION ENGINE (NEW)
    # =========================
    def execute_action(self, action):

        print("\n⚙️ EXECUTING ACTION:", action)

        # 1. INIT MODULES (fallback)
        if action == "INIT_MODULES":
            print("⚠ Modules missing → running kernel first")
            self.run_kernel()

        # 2. RUN KERNEL
        elif action == "RUN_KERNEL":
            self.run_kernel()

        # 3. SYNC ONLY
        elif action == "SYNC_ONLY":
            self.run_sync()

        else:
            print("❌ Unknown action")

    # =========================
    # KERNEL EXECUTION
    # =========================
    def run_kernel(self):
        print("\n🚀 STARTING KERNEL...")

        try:
            subprocess.run(["python3", KERNEL_PATH])
        except Exception as e:
            print("❌ Kernel error:", e)

    # =========================
    # SYNC EXECUTION
    # =========================
    def run_sync(self):
        print("\n🔄 RUNNING SYNC SYSTEM...")

        try:
            if os.path.exists(SYNC_PATH):
                subprocess.run(["bash", SYNC_PATH])
            else:
                print("❌ Sync script not found:", SYNC_PATH)
        except Exception as e:
            print("❌ Sync error:", e)

    # =========================
    # ORCHESTRATION FLOW
    # =========================
    def run(self):
        print("\n==============================")
        print(" SYNERGIA AI ORCHESTRATOR v2")
        print("==============================")

        action = self.analyze()
        self.execute_action(action)

        print("\n==============================")
        print(" ORCHESTRATION COMPLETE v2")
        print("==============================\n")


if __name__ == "__main__":
    orchestrator = AIOrchestratorV2()
    orchestrator.run()
