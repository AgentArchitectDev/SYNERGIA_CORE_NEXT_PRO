"""
======================================================
SYNERGIA COGNITIVE ROUTER V5
======================================================

Motor de decisión cognitiva.

Pipeline:

Input
 |
Intent Analyzer
 |
Context Analyzer
 |
Priority Engine
 |
Execution Planner
 |
Plan
======================================================
"""


from .intent_analyzer import intent_analyzer
from .context_analyzer import context_analyzer
from .priority_engine import priority_engine
from .execution_planner import execution_planner



class CognitiveRouter:


    def __init__(self):

        self.executions = 0

        self.last_plan = []



    def route(self, text):


        self.executions += 1


        context = context_analyzer.analyze(
            text
        )


        intents = intent_analyzer.analyze(
            text
        )


        ordered = priority_engine.sort(
            intents
        )


        plan = execution_planner.build(
            ordered
        )


        if not plan:

            plan = [
                "research"
            ]


        self.last_plan = plan


        return plan




    def status(self):


        return {


            "router":
                "Cognitive Router V5",


            "executions":
                self.executions,


            "last_plan":
                self.last_plan


        }
