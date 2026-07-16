#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

WORKFLOW DISPATCHER TEST

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

ENGINE
  |
  v
DISPATCHER
  |
  v
AGENTS QUEUE

============================================================
"""


from ai.director.workflow_engine import (
    workflow_engine
)

from ai.director.workflow_dispatcher import (
    workflow_dispatcher
)



def main():

    print()

    print("="*60)

    print(
        "SYNERGIA OMEGA WORKFLOW DISPATCHER TEST"
    )

    print("="*60)



    print()

    print(
        "Inicializando componentes..."
    )


    print(
        workflow_engine.initialize()
    )


    print(
        workflow_dispatcher.initialize()
    )



    print()

    print(
        "CREANDO WORKFLOW"
    )


    workflow = workflow_engine.build(

        "crear una aplicación web gastronómica"

    )


    print()

    print(workflow)



    print()

    print(
        "DISPATCH WORKFLOW"
    )


    result = workflow_dispatcher.dispatch(

        workflow

    )


    print()

    print(result)



    print()

    print(
        "ESTADO FINAL"
    )


    print(

        workflow_dispatcher.status()

    )



    print()

    print("="*60)

    print(
        "WORKFLOW DISPATCHER TEST FINALIZADO"
    )

    print("="*60)



if __name__ == "__main__":

    main()
