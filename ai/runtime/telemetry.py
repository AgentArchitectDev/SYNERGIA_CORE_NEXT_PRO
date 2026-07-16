"""
SYNERGIA TELEMETRY SYSTEM
Monitoreo interno del runtime
"""

import time


class Telemetry:

    def __init__(self):

        self.events = []
        self.start_time = time.time()

    # -----------------------------
    # LOG EVENT
    # -----------------------------

    def log(self, event_name, data=None):

        self.events.append({

            "timestamp": time.time(),

            "event": event_name,

            "data": data

        })

    # -----------------------------
    # STATS
    # -----------------------------

    def get_stats(self):

        return {

            "uptime": time.time() - self.start_time,

            "events": len(self.events),

            "last_event": self.events[-1] if self.events else None

        }

    # -----------------------------
    # RESET
    # -----------------------------

    def reset(self):

        self.events = []

        self.start_time = time.time()
