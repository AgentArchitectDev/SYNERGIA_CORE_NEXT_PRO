import subprocess
import json
import os
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))

RUNTIME_FILE = os.path.join(BASE, "system_state.json")
REGISTRY_FILE = os.path.join(BASE, "module_registry.json")

SYNC_SCRIPT = "/mnt/71392f5d/synergia-core/synergia_sync_system.sh"


class KernelLoader:

    def __init__(self):
        self.state = self.load_json(RUNTIME_FILE)
        self.registry = self.load_json(REGISTRY_FILE)

    # =========================
    # JSON SAFE LOAD/SAVE
    # =========================
    def load_json(self, path):
        if os.path.exists(path):
            with open(path, "r") as f:
                try:
                    return json.load(f)
                except:
                    return {}
        return {}

    def save_json(self, path, data):
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    # =========================
    # BOOT SYSTEM
    # =========================
    def boot_runtime(self):
        print("\n==============================")
        print(" SYNERGIA KERNEL LOADER v2.1")
        print("==============================\n")

        self.state["kernel_boot"] = str(datetime.now())
        self.state["status"] = "KERNEL_RUNNING"

        self.save_json(RUNTIME_FILE, self.state)

        print("✔ Runtime loaded")
        print("✔ Kernel initialized")
        print("✔ Mode:", self.state.get("mode", "UNKNOWN"))
        print("✔ Time:", self.state["kernel_boot"])

    # =========================
    # HEALTH CHECK
    # =========================
    def health_check(self):
        print("\n🧠 SYSTEM HEALTH CHECK")

        state_ok = isinstance(self.state, dict)
        modules = self.registry.get("modules", [])

        print("State:", "OK" if state_ok else "FAIL")
        print("Modules:", len(modules), "loaded")

        if len(modules) == 0:
            print("⚠ WARNING: No modules registered")

        return state_ok and len(modules) > 0

    # =========================
    # MODULES
    # =========================
    def list_modules(self):
        print("\n📦 ACTIVE MODULES:")
        for m in self.registry.get("modules", []):
            print(" -", m)

    # =========================
    # SYNC SYSTEM (FIXED PATH)
    # =========================
    def run_sync_system(self):
        print("\n🚀 RUNNING SYNERGIA SYNC SYSTEM...\n")

        try:
            if not os.path.exists(SYNC_SCRIPT):
                print("❌ SYNC SCRIPT NOT FOUND:")
                print(SYNC_SCRIPT)
                return

            result = subprocess.run(
                ["bash", SYNC_SCRIPT],
                capture_output=True,
                text=True
            )

            print(result.stdout)

            if result.stderr:
                print("⚠ ERRORS:")
                print(result.stderr)

        except Exception as e:
            print("❌ Sync system failed:", e)

    # =========================
    # KERNEL FLOW
    # =========================
    def start(self):
        self.boot_runtime()

        healthy = self.health_check()

        if not healthy:
            print("\n❌ SYSTEM NOT HEALTHY - KERNEL STOPPED")
            return

        self.list_modules()
        self.run_sync_system()

        self.state["status"] = "KERNEL_COMPLETED"
        self.save_json(RUNTIME_FILE, self.state)

        print("\n==============================")
        print(" KERNEL RUN COMPLETE (V2.1)")
        print("==============================\n")


# =========================
# BOOT ENTRY
# =========================
if __name__ == "__main__":
    kernel = KernelLoader()
    kernel.start()
