#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

AGENT SYSTEM TEST

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

Prueba:

Agent Router

        ↓

Agent Executor

        ↓

Resultado de ejecución


Objetivo:

Validar que SYNERGIA pueda:

- inicializar agentes
- recibir una tarea
- ejecutar una asignación
- devolver trazabilidad

============================================================
"""


from ai.director.agent_router import (
    agent_router
)

from ai.director.agent_executor import (
    agent_executor
)



# ----------------------------------------------------------

def main():


    print()

    print("=" * 60)

    print(
        "SYNERGIA AGENT SYSTEM TEST"
    )

    print("=" * 60)


    print()


    # --------------------------------------------------
    # Inicializar Router
    # --------------------------------------------------

    print(
        "Inicializando Agent Router..."
    )


    router_status = (
        agent_router.initialize()
    )


    print(router_status)



    # --------------------------------------------------
    # Inicializar Executor
    # --------------------------------------------------

    print()

    print(
        "Inicializando Agent Executor..."
    )


    executor_status = (
        agent_executor.initialize()
    )


    print(executor_status)



    # --------------------------------------------------
    # Simular tarea desde Workflow
    # --------------------------------------------------

    print()

    print("-" * 60)

    print(
        "Entrada Workflow"
    )

    print("-" * 60)



    workflow_step = {


        "step":

        3,


        "task":

        "Generar frontend",


        "agent":

        "Developer Agent",


        "status":

        "queued"

    }


    print(workflow_step)



    # --------------------------------------------------
    # Router decide
    # --------------------------------------------------

    print()

    print(
        "Routing tarea..."
    )


    routed_task = (

        agent_router.route(
            workflow_step
        )

    )


    print()

    print(
        routed_task
    )



    # --------------------------------------------------
    # Executor ejecuta
    # --------------------------------------------------

    print()

    print(
        "Ejecutando agente..."
    )


    execution = (

        agent_executor.execute(
            routed_task
        )

    )


    print()

    print(
        execution
    )



    # --------------------------------------------------
    # Estados finales
    # --------------------------------------------------

    print()

    print("=" * 60)

    print(
        "ESTADO FINAL"
    )

    print("=" * 60)



    print()

    print(
        agent_router.status()
    )


    print()

    print(
        agent_executor.status()
    )


    print()

    print("=" * 60)

    print(
        "AGENT SYSTEM TEST FINALIZADO"
    )

    print("=" * 60)



# ----------------------------------------------------------

if __name__ == "__main__":

    main()
