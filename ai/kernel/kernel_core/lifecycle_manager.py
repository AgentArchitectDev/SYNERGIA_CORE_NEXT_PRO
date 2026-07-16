class LifecycleManager:


    def __init__(self):

        self.started = []


    def start(self, service):

        if hasattr(service, "start"):

            service.start()

        self.started.append(
            service.__class__.__name__
        )


    def stop(self, service):

        if hasattr(service, "stop"):

            service.stop()



    def status(self):

        return {

            "started":
                self.started

        }


lifecycle_manager = LifecycleManager()
