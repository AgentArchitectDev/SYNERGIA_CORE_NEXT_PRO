#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA TEST FRAMEWORK

PIPELINE TEST

ACEA VERSION 1.0

============================================================
"""

from ai.director.workflow_engine import workflow_engine
from ai.director.workflow_dispatcher import workflow_dispatcher
from ai.director.agent_router import agent_router


def main():

    print()

    print("=" * 60)
    print("SYNERGIA PIPELINE TEST")
    print("=" * 60)

    workflow_engine.initialize()

    workflow_dispatcher.initialize()

    agent_router.initialize()

    workflow = workflow_engine.build(
        "crear una aplicación web"
    )

    dispatch = workflow_dispatcher.dispatch(workflow)

    print()

    print("Solicitud:")

    print(workflow["request"])

    print()

    print("-" * 60)

    for step in dispatch["steps"]:

        result = agent_router.route(step)

        print()

        print(f"STEP {result['step']}")

        print(result["task"])

        print("↓")

        print(result["agent"])

    print()

    print("=" * 60)

    print("PIPELINE FINALIZADO")

    print("=" * 60)


if __name__ == "__main__":

    main()
