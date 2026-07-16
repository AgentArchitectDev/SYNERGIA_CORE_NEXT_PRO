import json
import time
import os

LOG_FILE = "ai/runtime_storage/logs/system_log.json"


class ExportManager:

    def save(self, input_data, result):

        log = {
            "timestamp": time.time(),
            "input": input_data,
            "result": result
        }

        self._write(log)

        print("\n[LOG SYSTEM]")
        print(json.dumps(log, indent=2))

    def _write(self, log):
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

        if not os.path.exists(LOG_FILE):
            data = []
        else:
            with open(LOG_FILE, "r") as f:
                try:
                    data = json.load(f)
                except:
                    data = []

        data.append(log)

        with open(LOG_FILE, "w") as f:
            json.dump(data, f, indent=2)
