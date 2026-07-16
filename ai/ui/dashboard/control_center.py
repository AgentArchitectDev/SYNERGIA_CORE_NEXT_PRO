"""
============================================================
SYNERGIA COGNITIVE OS
CONTROL CENTER (DASHBOARD CORE)
Version 1.0
============================================================
"""

import time
import threading

from ai.runtime.runtime_manager import runtime_manager
from ai.kernel.kernel import kernel
from ai.runtime.runtime_logger import runtime_logger


class ControlCenter:

    def __init__(self):

        self.running = False

        self.refresh_rate = 1.0  # segundos

        self.thread = None

    # -------------------------------------------------

    def start(self):

        self.running = True

        self.thread = threading.Thread(target=self._loop)

        self.thread.start()

        print("\n🚀 CONTROL CENTER STARTED\n")

    # -------------------------------------------------

    def stop(self):

        self.running = False

        print("\n🛑 CONTROL CENTER STOPPED\n")

    # -------------------------------------------------

    def _loop(self):

        while self.running:

            self.render()

            time.sleep(self.refresh_rate)

    # -------------------------------------------------

    def render(self):

        snapshot = runtime_manager.snapshot()

        status = kernel.status()

        logs = runtime_logger.get_logs(5)

        print("\n" + "=" * 60)
        print("SYNERGIA CONTROL CENTER - LIVE DASHBOARD")
        print("=" * 60)

        print(f"VERSION: {status['version']}")
        print(f"UPTIME : {status['uptime']:.2f}s")

        print("\n📊 STATE")
        for k, v in snapshot["state"].items():
            print(f" - {k}: {v}")

        print("\n📦 TASKS")
        for t in snapshot["tasks"][-5:]:
            print(f" - {t}")

        print("\n🧠 CONTEXT")
        for k, v in snapshot["context"].items():
            print(f" - {k}: {v}")

        print("\n🪵 LOGS (last 5)")
        for l in logs:
            print(f" - [{l['level']}] {l['module']}: {l['message']}")

        print("=" * 60)


control_center = ControlCenter()
