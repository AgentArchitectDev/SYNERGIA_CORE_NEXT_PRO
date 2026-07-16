"""
============================================================
SYNERGIA RUNTIME LOGGER
Simple system logger
============================================================
"""

import time
import json
import os


class RuntimeLogger:

    def __init__(self):

        self.log_file = "runtime_storage/logs/system_log.json"

        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

    # -------------------------------------------------

    def log(self, tag, message):

        entry = {
            "tag": tag,
            "message": message,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
        }

        try:

            logs = []

            if os.path.exists(self.log_file):
                with open(self.log_file, "r") as f:
                    logs = json.load(f)

            logs.append(entry)

            with open(self.log_file, "w") as f:
                json.dump(logs, f, indent=2)

        except Exception:
            pass

        return entry


runtime_logger = RuntimeLogger()
