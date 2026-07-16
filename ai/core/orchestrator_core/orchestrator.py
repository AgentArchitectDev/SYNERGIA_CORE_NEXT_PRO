"""
=========================================================
SYNERGIA CORE NEXT_PRO

ORCHESTRATOR CORE V5.1

Motor central de coordinación

=========================================================
"""


import time


from .pipeline import pipeline

from .telemetry import telemetry

from .execution_context import ExecutionContext

from .response_builder import ResponseBuilder



class Orchestrator:


    def __init__(self):

        self.version = "5.1"

        self.executions = 0

        self.history = []



    # -------------------------------------------------

    def run(self, input_text):


        self.executions += 1


        context = ExecutionContext(
            input_text
        )


        start = time.time()


        try:


            result = pipeline.execute(
                context
            )


            status = "success"



        except Exception as e:


            result = {

                "error":
                    str(e)

            }


            status = "error"



        latency = (
            time.time()
            -
            start
        )


        telemetry.record(

            status=status,

            latency=latency

        )


        response = ResponseBuilder.build(

            input_text,

            result

        )


        self.history.append(
            response
        )


        return response



    # -------------------------------------------------

    def status(self):


        return {


            "version":
                self.version,


            "executions":
                self.executions,


            "history":
                len(self.history)


        }





orchestrator = Orchestrator()
