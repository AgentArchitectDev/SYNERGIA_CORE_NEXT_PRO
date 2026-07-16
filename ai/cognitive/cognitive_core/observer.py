import time


class Observer:

    """
    Observa el estado del sistema.
    """

    def __init__(self):

        self.observations = []


    def observe(self, data):

        observation = {

            "input": data,

            "timestamp": time.time()

        }

        self.observations.append(
            observation
        )

        return observation



    def status(self):

        return {

            "observations":
                len(self.observations)

        }


observer = Observer()
