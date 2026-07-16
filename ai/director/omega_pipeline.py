#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

OMEGA PIPELINE

CORE IA SYSTEMS

ACEA VERSION 1.2

============================================================

Pipeline Cognitivo Principal

Director
Cognitive Decision
Autonomy
Workflow
Agents
Models
Memory

============================================================
"""


import time


from ai.director.omega_director import (
    omega_director
)


from ai.director.autonomy_manager import (
    autonomy_manager
)


from ai.director.workflow_engine import (
    workflow_engine
)


from ai.director.workflow_dispatcher import (
    workflow_dispatcher
)


from ai.director.pipeline_memory import (
    pipeline_memory
)



class OmegaPipeline:


    def __init__(self):

        self.initialized = False

        self.mode = "autonomous"

        self.executions = 0

        self.last_request = None



    # --------------------------------------------------

    def initialize(
        self,
        mode="autonomous"
    ):


        self.mode = mode


        omega_director.initialize()

        autonomy_manager.initialize(
            mode
        )

        workflow_engine.initialize()

        workflow_dispatcher.initialize()

        pipeline_memory.initialize()



        self.initialized = True



        return {


            "status":

            "omega_pipeline_ready",


            "mode":

            self.mode,


            "initialized":

            True

        }



    # --------------------------------------------------

    def execute(
        self,
        request
    ):


        self.executions += 1

        self.last_request = request



        #
        # Capa Cognitiva + Autonomía
        #

        autonomy = autonomy_manager.evaluate(

            request,

            self.mode

        )



        #
        # Si requiere aprobación humana
        #

        if autonomy["approval_required"]:


            return {


                "pipeline":

                "OMEGA",


                "mode":

                self.mode,


                "status":

                "waiting_approval",


                "cognitive":

                autonomy["cognitive"],


                "autonomy":

                {

                    "decision":

                    autonomy["decision"],


                    "approval_required":

                    True

                },


                "timestamp":

                time.time()

            }



        #
        # Director OMEGA
        #

        director_result = omega_director.execute(

            request

        )



        #
        # Crear Workflow
        #

        workflow = workflow_engine.build(

            request

        )



        dispatch = workflow_dispatcher.dispatch(

            workflow

        )



        #
        # Guardar memoria
        #

        pipeline_memory.save(

            request=request,

            category="omega",

            agents=[

                step["agent"]

                for step in dispatch["steps"]

            ],

            model="runtime",

            result="completed"

        )



        return {


            "pipeline":

            "OMEGA",


            "mode":

            self.mode,



            "director":

            director_result,



            "cognitive":

            autonomy["cognitive"],



            "autonomy":

            {

                "decision":

                autonomy["decision"],


                "approval_required":

                False

            },



            "workflow":

            dispatch,



            "memory":

            {

                "stored":

                True

            },



            "status":

            "completed",



            "timestamp":

            time.time()

        }



    # --------------------------------------------------

    def status(self):


        return {


            "component":

            "OMEGA Pipeline V1.2",


            "initialized":

            self.initialized,


            "mode":

            self.mode,


            "executions":

            self.executions,


            "last_request":

            self.last_request

        }





omega_pipeline = OmegaPipeline()
