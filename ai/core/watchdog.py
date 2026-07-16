"""
SYNERGIA V3 - Watchdog (FINAL)
Auto-recovery del sistema
"""

import time


class Watchdog:

    def __init__(self, lifecycle, health):

        self.lifecycle = lifecycle
        self.health = health
        self.last_check = time.time()

    # -----------------------------

    def check(self):

        report = []

        for module, state in self.lifecycle.states.items():

            health = self.health.get(module)

            # CASO 1: módulo caído
            if state != "running":

                self.lifecycle.restart(module)

                report.append({
                    "module": module,
                    "issue": "not_running",
                    "action": "restart_triggered"
                })

            # CASO 2: health fallando
            elif health.get("status") == "failed":

                self.lifecycle.restart(module)

                report.append({
                    "module": module,
                    "issue": "failed_health",
                    "action": "restart_triggered"
                })

            # CASO OK
            else:

                report.append({
                    "module": module,
                    "status": "ok"
                })

        self.last_check = time.time()

        return report


watchdog = Watchdog(None, None)
