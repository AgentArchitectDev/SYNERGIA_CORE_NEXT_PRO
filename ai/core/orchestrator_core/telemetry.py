"""
=========================================================
SYNERGIA CORE NEXT_PRO

TELEMETRY V2

Sistema de observabilidad del Orchestrator Core

Compatible con:

- begin()
- error()
- status()
- record()

=========================================================
"""


import time



class Telemetry:


    def __init__(self):

        self.executions = 0

        self.errors = 0

        self.last_execution = None

        self.history = []



    # -------------------------------------------------
    # LEGACY START
    # -------------------------------------------------

    def begin(self):


        self.executions += 1

        self.last_execution = time.time()



    # -------------------------------------------------
    # ERROR TRACKING
    # -------------------------------------------------

    def error(self):


        self.errors += 1



    # -------------------------------------------------
    # NEW V2 RECORD
    # -------------------------------------------------

    def record(
        self,
        status="success",
        latency=0
    ):


        event = {


            "status":
                status,


            "latency":
                latency,


            "timestamp":
                time.time()

        }


        self.history.append(
            event
        )


        self.executions += 1


        self.last_execution = (
            event["timestamp"]
        )


        if status == "error":

            self.errors += 1



        return event



    # -------------------------------------------------
    # STATUS
    # -------------------------------------------------

    def status(self):


        return {


            "executions":
                self.executions,


            "errors":
                self.errors,


            "last_execution":
                self.last_execution,


            "history":
                len(self.history)


        }




# singleton

telemetry = Telemetry()
