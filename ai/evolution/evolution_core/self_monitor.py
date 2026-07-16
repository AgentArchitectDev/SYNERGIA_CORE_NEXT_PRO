import time


class SelfMonitor:


    def __init__(self):

        self.checks = []


    def inspect(self, state):

        result = {

            "timestamp": time.time(),

            "state": state,

            "health": "stable"

        }

        self.checks.append(result)

        return result



    def status(self):

        return {

            "checks":
                len(self.checks)

        }



self_monitor = SelfMonitor()
