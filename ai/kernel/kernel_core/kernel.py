"""
====================================================
SYNERGIA KERNEL CORE V1
====================================================
"""


from .kernel_state import kernel_state

from .service_registry import service_registry

from .lifecycle_manager import lifecycle_manager



class Kernel:


    def __init__(self):

        self.version = "1.0"

        self.name = "SYNERGIA Kernel"



    def boot(self):

        kernel_state.boot()

        return {

            "kernel":
                self.name,

            "status":
                "booted"

        }



    def register_service(
            self,
            name,
            service
    ):

        service_registry.register(
            name,
            service
        )

        kernel_state.services = len(
            service_registry.services
        )



    def start_service(self, name):

        service = service_registry.get(
            name
        )

        if service:

            lifecycle_manager.start(
                service
            )

            return True

        return False



    def shutdown(self):

        kernel_state.shutdown()



    def status(self):

        return {

            "version":
                self.version,

            "state":
                kernel_state.status(),

            "services":
                service_registry.status(),

            "lifecycle":
                lifecycle_manager.status()

        }
