"""
============================================================
SYNERGIA GLOBAL MEMORY
Persistent runtime memory store
============================================================
"""

import time


class GlobalMemory:

    def __init__(self):

        self.memory = []

    # -------------------------------------------------

    def store(self, source: str, data):

        entry = {
            "source": source,
            "data": data,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
        }

        self.memory.append(entry)

        return entry

    # -------------------------------------------------

    def search(self, keyword: str):

        results = []

        for m in self.memory:

            if keyword.lower() in str(m["data"]).lower():
                results.append(m)

        return results

    # -------------------------------------------------

    def all(self):

        return self.memory

    # -------------------------------------------------

    def clear(self):

        self.memory = []

        return {"status": "cleared"}


global_memory = GlobalMemory()
