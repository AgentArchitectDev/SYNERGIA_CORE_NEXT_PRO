"""
SYNERGIA V3 - Telemetry Core
Registro de eventos del sistema
"""

import time
from datetime import datetime


class Telemetry:

    def __init__(self):

        self.events = []

    # -----------------------------

    def start(self, module):

        return {
            "module": module,
            "start": time.time()
        }

    # -----------------------------

    def end(self, event, result):

        record = {
            "module": event["module"],
            "start": event["start"],
            "end": time.time(),
            "duration": round(time.time() - event["start"], 6),
            "timestamp": datetime.now().isoformat(),
            "status": result.get("status", "unknown") if isinstance(result, dict) else "unknown"
        }

        self.events.append(record)

        return record

    # -----------------------------

    def get_all(self):

        return self.events

    # -----------------------------

    def summary(self):

        return {
            "total_events": len(self.events),
            "last_event": self.events[-1] if self.events else None
        }


telemetry = Telemetry()
