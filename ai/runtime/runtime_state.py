#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

RUNTIME STATE MANAGER

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

Estado operacional del Runtime.

Controla:

- Nodo activo
- Perfil MAQ1 / MAQ2
- Modo ejecución
- Estado del sistema
- Ejecución actual
- Última actividad


Evolución futura:

Runtime Memory
Distributed State
Cluster State
Cognitive Runtime


============================================================
"""


import time



class RuntimeState:


    def __init__(self):


        self.initialized = False


        self.node = None


        self.profile = None


        self.mode = None


        self.status = "offline"


        self.execution_id = 0


        self.current_task = None


        self.last_update = None




    # --------------------------------------------------

    def initialize(
        self,
        node="MAQ2",
        profile="development",
        mode="autonomous"
    ):


        self.node = node

        self.profile = profile

        self.mode = mode

        self.status = "online"

        self.initialized = True

        self.last_update = time.time()



        return {


            "status":

            "runtime_state_ready",


            "node":

            self.node,


            "profile":

            self.profile,


            "mode":

            self.mode


        }




    # --------------------------------------------------

    def start_execution(
        self,
        task
    ):


        self.execution_id += 1


        self.current_task = task


        self.status = "executing"


        self.last_update = time.time()



        return {


            "execution":

            self.execution_id,


            "task":

            task,


            "status":

            self.status,


            "timestamp":

            self.last_update

        }




    # --------------------------------------------------

    def complete_execution(self):


        self.status = "ready"


        self.current_task = None


        self.last_update = time.time()



        return {


            "status":

            "execution_completed",


            "timestamp":

            self.last_update

        }




    # --------------------------------------------------

    def update_mode(
        self,
        mode
    ):


        self.mode = mode


        self.last_update = time.time()



        return {


            "status":

            "mode_updated",


            "mode":

            self.mode

        }




    # --------------------------------------------------

    def get_state(self):


        return {


            "component":

            "OMEGA Runtime State",


            "initialized":

            self.initialized,


            "node":

            self.node,


            "profile":

            self.profile,


            "mode":

            self.mode,


            "status":

            self.status,


            "execution_id":

            self.execution_id,


            "current_task":

            self.current_task,


            "last_update":

            self.last_update

        }





runtime_state = RuntimeState()
