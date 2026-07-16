#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

MODEL EXECUTION BRIDGE

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

Responsabilidad:

Conectar:

Agent Executor

con

Model Router


Flujo:

Agent Executor

        ↓

Model Executor

        ↓

Model Router

        ↓

Modelo IA


No ejecuta todavía Ollama.

Prepara la capa de ejecución.

============================================================
"""


from __future__ import annotations

import time


from ai.director.model_router import (
    model_router
)



class ModelExecutor:


    def __init__(self):

        self.initialized = False

        self.executions = 0

        self.last_model = None

        self.last_task = None



    # --------------------------------------------------

    def initialize(self):


        self.initialized = True


        model_router.initialize(
            "autonomous"
        )


        return {


            "status":

            "model_executor_ready",


            "initialized":

            True

        }



    # --------------------------------------------------

    def execute(
        self,
        agent_result
    ):

        """
        Recibe resultado del Agent Executor.

        Ejemplo:

        {
          agent:
          Developer Agent,

          task:
          Generar frontend
        }

        """


        self.executions += 1


        task = agent_result["task"]


        selection = model_router.select(
            task
        )


        model = selection["recommendation"]["model"]


        self.last_model = model

        self.last_task = task



        return {


            "execution":

            self.executions,


            "agent":

            agent_result["agent"],


            "task":

            task,


            "model":

            model,


            "status":

            "model_selected",


            "details":

            selection,


            "timestamp":

            time.time()

        }



    # --------------------------------------------------

    def status(self):


        return {


            "component":

            "OMEGA Model Executor",


            "initialized":

            self.initialized,


            "executions":

            self.executions,


            "last_model":

            self.last_model,


            "last_task":

            self.last_task

        }



# ------------------------------------------------------

# instancia global

# ------------------------------------------------------

model_executor = ModelExecutor()
