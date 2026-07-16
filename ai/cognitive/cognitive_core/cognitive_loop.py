from .observer import observer

from .evaluator import evaluator

from .decision_engine import decision_engine

from .learning_cycle import learning_cycle



class CognitiveLoop:


    def __init__(self):

        self.running = False



    def start(self):

        self.running = True


        return {

            "status":
                "cognitive loop started"

        }



    def process(self, data):


        observation = observer.observe(
            data
        )


        evaluation = evaluator.evaluate(
            observation
        )


        decision = decision_engine.decide(
            evaluation
        )


        learning_cycle.learn(
            decision
        )


        return {

            "observation":
                observation,

            "evaluation":
                evaluation,

            "decision":
                decision

        }



    def status(self):

        return {

            "running":
                self.running,

            "observer":
                observer.status(),

            "learning":
                learning_cycle.status()

        }
