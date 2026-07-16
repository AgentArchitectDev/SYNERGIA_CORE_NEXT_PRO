#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

MODEL ROUTER V2

CORE IA SYSTEMS

ACEA VERSION 2.0

============================================================

Director de selección de modelos.

Modos:

AUTONOMOUS:
OMEGA decide automáticamente.

HUMAN:
OMEGA recomienda y espera validación.

============================================================
"""


import time



class ModelRouter:


    def __init__(self):

        self.initialized = False

        self.mode = "autonomous"

        self.routes = {}

        self.executions = 0

        self.last_selection = None



    # --------------------------------------------------

    def initialize(self, mode="autonomous"):


        self.initialized = True

        self.mode = mode


        self.routes = {


            "development":
            {
                "model":
                "deepseek-coder",

                "reason":
                "programacion y arquitectura software"
            },


            "business":
            {
                "model":
                "qwen",

                "reason":
                "soluciones empresariales"
            },


            "creative":
            {
                "model":
                "llama",

                "reason":
                "creatividad y contenido"
            },


            "reasoning":
            {
                "model":
                "mistral",

                "reason":
                "analisis y razonamiento"
            },


            "local_ai":
            {
                "model":
                "ollama",

                "reason":
                "ejecucion local"
            }

        }


        return {

            "status":
            "model_router_ready",

            "mode":
            self.mode,

            "models":
            len(self.routes)

        }



    # --------------------------------------------------

    def set_mode(self, mode):


        if mode not in [
            "autonomous",
            "human"
        ]:

            return {

                "status":
                "error",

                "message":
                "modo invalido"

            }


        self.mode = mode


        return {

            "status":
            "mode_changed",

            "mode":
            self.mode

        }



    # --------------------------------------------------

    def select(self, task):


        self.executions += 1


        text = task.lower()



        if any(
            x in text
            for x in [
                "codigo",
                "python",
                "programar",
                "software",
                "app"
            ]
        ):

            category = "development"



        elif any(
            x in text
            for x in [
                "cliente",
                "empresa",
                "negocio",
                "web"
            ]
        ):

            category = "business"



        elif any(
            x in text
            for x in [
                "imagen",
                "diseño",
                "crear"
            ]
        ):

            category = "creative"



        elif any(
            x in text
            for x in [
                "ollama",
                "modelo",
                "local"
            ]
        ):

            category = "local_ai"



        else:

            category = "reasoning"



        recommendation = self.routes.get(
            category
        )



        result = {


            "task":
            task,


            "mode":
            self.mode,


            "category":
            category,


            "recommendation":
            recommendation,


            "approval_required":
            self.mode == "human",


            "timestamp":
            time.time()

        }



        self.last_selection = result


        return result



    # --------------------------------------------------

    def status(self):


        return {


            "component":
            "OMEGA Model Router V2",


            "initialized":
            self.initialized,


            "mode":
            self.mode,


            "executions":
            self.executions,


            "last_selection":
            self.last_selection

        }



model_router = ModelRouter()
