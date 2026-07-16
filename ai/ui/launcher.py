"""
SYNERGIA V3 - UI LAUNCHER (CONSOLE CONTROL PANEL)
"""

from ai.kernel.kernel import kernel
import time


class SynergiaLauncher:

    def __init__(self):
        self.kernel = kernel

    # -----------------------------

    def splash(self):

        print("\n" + "=" * 60)
        print("        SYNERGIA COGNITIVE OS - V3 LAUNCHER")
        print("=" * 60)
        print("Booting system...\n")

    # -----------------------------

    def boot_system(self):

        self.kernel.boot()

    # -----------------------------

    def show_status(self):

        status = self.kernel.status()

        print("\n🧠 SYSTEM STATUS")
        print("-" * 40)

        print("Kernel:", status["kernel"])
        print("Models:", len(status.get("models", [])))
        print("Health:", status.get("health"))

    # -----------------------------

    def run(self):

        self.splash()

        self.boot_system()

        self.show_status()

        self.loop()

    # -----------------------------

    def loop(self):

        while True:

            print("\n")
            print("COMMANDS:")
            print("1 - status")
            print("2 - execute task")
            print("3 - models")
            print("0 - exit")

            cmd = input("\n> ")

            if cmd == "1":
                self.show_status()

            elif cmd == "2":
                task = input("Task > ")
                result = self.kernel.execute(task)
                print("\nRESULT:\n", result)

            elif cmd == "3":
                print(self.kernel.status()["models"])

            elif cmd == "0":
                print("Shutting down SYNERGIA...")
                break

            else:
                print("Invalid command")


# entrypoint
launcher = SynergiaLauncher()
