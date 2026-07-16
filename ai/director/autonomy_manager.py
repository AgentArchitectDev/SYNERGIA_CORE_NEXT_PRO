#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

AUTONOMY MANAGER

CORE IA SYSTEMS

ACEA VERSION 1.2

============================================================

Control:

AUTO MODE
HUMAN MODE

Integración:

Cognitive Decision Layer

============================================================
"""


import time


from ai.director.cognitive_decision import (
    cognitive_decision
)



class AutonomyManager:


    def __init__(self):

        self.initialized = False

        self.mode = "autonomous"

        self.executions = 0

        self.pending = None

        self.last_decision = None



    # --------------------------------------------------

    def initialize(
        self,
        mode="autonomous"
    ):


        self.mode = mode

        self.initialized = True


        return {


            "status":

            "autonomy_manager_ready",


            "mode":

            self.mode

        }



    # --------------------------------------------------

    def set_mode(
        self,
        mode
    ):


        self.mode = mode


        return {


            "status":

            "mode_changed",


            "mode":

            self.mode

        }



    # --------------------------------------------------

    def evaluate(
        self,
        request,
        mode=None
    ):


        if mode:

            self.mode = mode



        self.executions += 1



        cognitive = cognitive_decision.evaluate(

            request

        )



        approval_required = False



        decision = "execute"



        if cognitive["decision"] == "HUMAN_APPROVAL":


            approval_required = True

            decision = "waiting_approval"



        elif self.mode == "human":


            approval_required = True

            decision = "waiting_approval"



        result = {


            "request":

            request,


            "mode":

            self.mode,


            "cognitive":

            cognitive,


            "decision":

            decision,


            "approval_required":

            approval_required

        }



        if approval_required:


            self.pending = result



        else:

            self.pending = None



        self.last_decision = result



        return result




    # --------------------------------------------------

    def approve(self):


        if not self.pending:


            return {


                "status":

                "nothing_pending"

            }



        request = self.pending["request"]



        self.pending = None



        return {


            "status":

            "approved",


            "request":

            request,


            "execution":

            "authorized"

        }



    # --------------------------------------------------

    def status(self):


        return {


            "component":

            "OMEGA Autonomy Manager V1.2",


            "initialized":

            self.initialized,


            "mode":

            self.mode,


            "executions":

            self.executions,


            "pending":

            self.pending,


            "last_decision":

            self.last_decision

        }





autonomy_manager = AutonomyManager()
