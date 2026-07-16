#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
SYNERGIA OMEGA

WORKFLOW DISPATCHER

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

Responsabilidad

Recibir un Workflow generado por Workflow Engine
y distribuir cada paso al Agent Router.

NO ejecuta IA.

NO llama modelos.

NO ejecuta Runtime.

Su única función es distribuir el flujo de trabajo.

============================================================
"""

from __future__ import annotations

import time

from typing import Dict
from typing import List


class WorkflowDispatcher:

    """
    Dispatcher del Workflow Cognitivo.
    """

    def __init__(self):

        self.initialized = False

        self.executions = 0

        self.last_workflow = []

        self.last_dispatch = []

    # --------------------------------------------------

    def initialize(self):

        self.initialized = True

        return {

            "status": "workflow_dispatcher_ready",

            "initialized": True

        }

    # --------------------------------------------------

    def dispatch(
        self,
        workflow: Dict
    ):

        self.executions += 1

        self.last_workflow = workflow

        dispatch = []

        for step in workflow["steps"]:

            dispatch.append(

                self.execute_step(step)

            )

        self.last_dispatch = dispatch

        return {

            "status": "workflow_dispatched",

            "steps": dispatch,

            "count": len(dispatch),

            "timestamp": time.time()

        }

    # --------------------------------------------------

    def execute_step(
        self,
        step: Dict
    ):

        name = step["name"].lower()

        # --------------------------------------------

        if "arquitectura" in name:

            agent = "Business Agent"

        elif "frontend" in name:

            agent = "Developer Agent"

        elif "backend" in name:

            agent = "Developer Agent"

        elif "python" in name:

            agent = "Developer Agent"

        elif "modelo" in name:

            agent = "Ollama Agent"

        elif "runtime" in name:

            agent = "Runtime Agent"

        elif "documentación" in name:

            agent = "Documentation Agent"

        elif "analizar" in name:

            agent = "Analysis Agent"

        elif "resolver" in name:

            agent = "General Agent"

        else:

            agent = "General Agent"

        return {

            "step": step["id"],

            "task": step["name"],

            "agent": agent,

            "status": "queued"

        }

    # --------------------------------------------------

    def status(self):

        return {

            "component": "OMEGA Workflow Dispatcher",

            "initialized": self.initialized,

            "executions": self.executions,

            "last_steps": len(self.last_dispatch)

        }


workflow_dispatcher = WorkflowDispatcher()
