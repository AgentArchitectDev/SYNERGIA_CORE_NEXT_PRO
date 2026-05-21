from kernel.runtime.runtime_manager import RuntimeManager

class Bootstrap:

    @staticmethod
    def start():

        print("\n🚀 BOOTSTRAP STARTED\n")

        RuntimeManager.boot()

        print("✅ SYNERGIA BOOT COMPLETE\n")

# =========================================================
# SYNERGIA CORE NEXT PRO
# BOOTSTRAP SYSTEM
# =========================================================

from kernel.runtime.runtime_manager import RuntimeManager
from kernel.services.config_service import ConfigService


class Bootstrap:

    def __init__(self):

        self.config = ConfigService.system_config()

    def start(self):

        print("\n[BOOT] Loading system config...")
        print(self.config)

        print("\n[BOOT] Starting Runtime Manager...")

        runtime = RuntimeManager()

        runtime.initialize()

        print("\n[BOOT] Kernel initialized successfully.")
