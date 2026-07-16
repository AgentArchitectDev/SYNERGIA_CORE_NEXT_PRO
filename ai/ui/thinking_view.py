import time
from ai.runtime.orchestrator import Orchestrator

class ThinkingViewer:

    def __init__(self):
        self.orch = Orchestrator()

    def run(self):
        print("\n🧠 SYNERGIA THINKING VIEWER")
        print("================================")

        while True:
            user_input = input("\nINPUT> ")

            if user_input == "exit":
                break

            print("\n[1] INPUT CAPTURED")
            time.sleep(0.3)

            print("[2] ORCHESTRATOR ACTIVATED")
            time.sleep(0.3)

            print("[3] LOADING MEMORY...")
            time.sleep(0.3)

            print("[4] DECIDING FLOW...")
            time.sleep(0.3)

            result = self.orch.handle(user_input)

            print("[5] EXECUTION COMPLETE")
            time.sleep(0.2)

            print("\n===== RESULT =====")
            print(result)
            print("==================")
