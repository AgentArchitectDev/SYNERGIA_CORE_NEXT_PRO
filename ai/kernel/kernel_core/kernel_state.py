import time


class KernelState:

    def __init__(self):

        self.boot_time = time.time()

        self.running = False

        self.services = 0

        self.errors = 0


    def boot(self):

        self.running = True


    def shutdown(self):

        self.running = False


    def status(self):

        return {

            "running": self.running,

            "uptime":
                round(
                    time.time() - self.boot_time,
                    2
                ),

            "services":
                self.services,

            "errors":
                self.errors
        }


kernel_state = KernelState()
