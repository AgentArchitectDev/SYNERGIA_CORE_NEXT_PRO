#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

RUNTIME CONTROLLER

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

Controlador central del Runtime.

Responsabilidades:

- iniciar nodo
- controlar estado global
- registrar ejecuciones
- verificar salud
- supervisar runtime


Integración:

Runtime State
Execution History
Self Monitor
Health Manager


Evolución futura:

Distributed Runtime
Node Bus
Remote Execution
Fault Recovery


============================================================
"""


import time



from ai.runtime.runtime_state import runtime_state

from ai.runtime.execution_history import execution_history

from ai.runtime.self_monitor import self_monitor

from ai.runtime.health_manager import health_manager




class OmegaRuntimeController:


    def __init__(self):

        self.initialized = False

        self.node = None

        self.profile = None

        self.mode = None

        self.executions = 0

        self.last_result = None



    # --------------------------------------------------

    def initialize(
        self,
        node,
        profile,
        mode
    ):


        self.node = node

        self.profile = profile

        self.mode = mode



        runtime_state.initialize(
            node,
            profile,
            mode
        )


        execution_history.initialize()


        self_monitor.initialize()


        health_manager.initialize()



        self.initialized = True



        return {


            "status":

            "omega_runtime_controller_ready",


            "node":

            node,


            "profile":

            profile,


            "mode":

            mode

        }



    # --------------------------------------------------

    def execute(
        self,
        task,
        agent="General Agent",
        model="mistral"
    ):


        if not self.initialized:


            return {


                "status":

                "error",


                "message":

                "runtime not initialized"

            }



        self.executions += 1



        start = runtime_state.start_execution(
            task
        )



        record = execution_history.register(

            task,

            self.node,

            agent,

            model

        )



        monitor = self_monitor.inspect(

            runtime_state,

            execution_history

        )



        health = health_manager.evaluate(

            monitor

        )



        runtime_state.complete_execution()



        result = {


            "execution":

            self.executions,


            "task":

            task,


            "agent":

            agent,


            "model":

            model,


            "history":

            record,


            "health":

            health,


            "status":

            "completed",


            "timestamp":

            time.time()

        }



        self.last_result = result



        return result



    # --------------------------------------------------

    def health(self):


        monitor = self_monitor.inspect(

            runtime_state,

            execution_history

        )


        return health_manager.evaluate(

            monitor

        )



    # --------------------------------------------------

    def status(self):


        return {


            "component":

            "OMEGA Runtime Controller",


            "initialized":

            self.initialized,


            "node":

            self.node,


            "profile":

            self.profile,


            "mode":

            self.mode,


            "executions":

            self.executions,


            "last_result":

            self.last_result

        }



    # --------------------------------------------------

    def shutdown(self):


        self.initialized = False


        return {


            "status":

            "runtime_shutdown",


            "node":

            self.node,


            "timestamp":

            time.time()

        }





omega_runtime = OmegaRuntimeController()
