import json
import os
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))

STATE_FILE = os.path.join(BASE, "system_state.json")
REGISTRY_FILE = os.path.join(BASE, "module_registry.json")


class AIOrchestrator:

    def __init__(self):
        self.state = self.load_json(STATE_FILE)
        self.registry = self.load_json(REGISTRY_FILE)

    # =========================
    # LOAD SYSTEM DATA
    # =========================
    def load_json(self, path):
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
        return {}

    # =========================
    # SYSTEM ANALYSIS
    # =========================
    def analyze_system(self):

        print("\n🧠 AI ORCHESTRATOR ANALYSIS\n")

        state_status = self.state.get("status", "UNKNOWN")
        modules = self.registry.get("modules", [])

        print("📊 STATE:", state_status)
        print("📦 MODULES:", len(modules))

        # decisiones base
        if len(modules) == 0:
            return "INIT_MODULES"

        if state_status != "KERNEL_COMPLETED":
            return "RUN_KERNEL"

        return "SYSTEM_STABLE"

    # =========================
    # DECISION ENGINE
    # =========================
    def decide(self):

        decision = self.analyze_system()

        print("\n🧭 DECISION:", decision)

        if decision == "INIT_MODULES":
            print("➡ ACTION: Register modules required")

        elif decision == "RUN_KERNEL":
            print("➡ ACTION: Kernel needs execution")

        elif decision == "SYSTEM_STABLE":
            print("➡ ACTION: System stable - idle mode")

        return decision

    # =========================
    # FUTURE HOOK (AI LAYER)
    # =========================
    def ai_hook(self):
        print("\n🤖 AI LAYER (placeholder)")
        print("→ Ready for Ollama integration")

    # =========================
    # RUN ORCHESTRATOR
    # =========================
    def run(self):

        print("\n==============================")
        print(" SYNERGIA AI ORCHESTRATOR v1")
        print("==============================")

        decision = self.decide()
        self.ai_hook()

        print("\n==============================")
        print(" ORCHESTRATION COMPLETE")
        print("==============================\n")

        return decision


if __name__ == "__main__":
    orchestrator = AIOrchestrator()
    orchestrator.run()
