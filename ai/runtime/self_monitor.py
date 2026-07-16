#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

SELF MONITOR

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

Sistema de auto monitoreo del Runtime.

Responsabilidades:

- observar estado runtime
- revisar ejecuciones
- generar diagnóstico
- detectar actividad


Evolución futura:

Health Manager
Predictive Maintenance
Cognitive Self Awareness
Distributed Monitoring


============================================================
"""


import time



class SelfMonitor:


    def __init__(self):

        self.initialized = False

        self.checks = 0

        self.last_report = None



    # --------------------------------------------------

    def initialize(self):


        self.initialized = True


        return {


            "status":

            "self_monitor_ready",


            "initialized":

            True

        }



    # --------------------------------------------------

    def inspect(

        self,
        runtime_state=None,
        execution_history=None

    ):


        self.checks += 1



        report = {


            "component":

            "OMEGA Self Monitor",



            "runtime":

            self._runtime_status(
                runtime_state
            ),



            "executions":

            self._execution_status(
                execution_history
            ),



            "health":

            "OK",



            "timestamp":

            time.time()

        }



        self.last_report = report



        return report



    # --------------------------------------------------

    def _runtime_status(

        self,
        runtime_state

    ):


        if runtime_state is None:


            return {


                "status":

                "unknown"

            }



        try:


            state = runtime_state.get_state()



            return {


                "status":

                state.get(
                    "status"
                ),


                "node":

                state.get(
                    "node"
                ),


                "mode":

                state.get(
                    "mode"
                ),


                "execution":

                state.get(
                    "execution_id"
                )

            }


        except Exception:


            return {


                "status":

                "error"

            }



    # --------------------------------------------------

    def _execution_status(

        self,
        execution_history

    ):


        if execution_history is None:


            return {


                "records":

                0

            }



        try:


            stats = execution_history.stats()



            return {


                "records":

                stats.get(
                    "executions"
                )

            }



        except Exception:


            return {


                "records":

                "error"

            }



    # --------------------------------------------------

    def status(self):


        return {


            "component":

            "OMEGA Self Monitor",


            "initialized":

            self.initialized,


            "checks":

            self.checks,


            "last_report":

            self.last_report

        }





self_monitor = SelfMonitor()
