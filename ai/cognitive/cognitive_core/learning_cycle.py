import time


class LearningCycle:


    def __init__(self):

        self.cycles = 0

        self.history = []



    def learn(self, result):

        self.cycles += 1


        self.history.append({

            "result":
                result,

            "time":
                time.time()

        })


    def status(self):

        return {

            "cycles":
                self.cycles

        }



learning_cycle = LearningCycle()
