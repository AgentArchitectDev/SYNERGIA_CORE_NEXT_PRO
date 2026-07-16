#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

FULL SYSTEM TEST

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

End To End Validation

DIRECTOR
COGNITIVE DECISION
AUTONOMY
PIPELINE
WORKFLOW
AGENTS
MODELS
RUNTIME
MEMORY

============================================================
"""


from ai.director.omega_pipeline import omega_pipeline
from ai.director.autonomy_manager import autonomy_manager
from ai.director.pipeline_memory import pipeline_memory



def execute_test(
    request,
    mode
):


    print()

    print("-" * 60)

    print(
        "REQUEST:"
    )

    print(
        request
    )


    print()

    print(
        "MODE:"
    )

    print(
        mode
    )


    print()


    omega_pipeline.initialize(
        mode
    )


    result = omega_pipeline.execute(
        request
    )


    print()

    print(
        "PIPELINE RESULT"
    )


    print(
        result
    )


    if result.get(
        "status"
    ) == "completed":


        pipeline_memory.save(

            request=request,

            category="omega",

            agents=[

                "OMEGA Director",

                "Agents"

            ],

            model="runtime",

            result="completed"

        )


    return result




def main():


    print()

    print("=" * 60)

    print(
        "SYNERGIA OMEGA FULL SYSTEM TEST"
    )

    print("=" * 60)



    print()

    print(
        "Inicializando memoria..."
    )


    print(
        pipeline_memory.initialize()
    )



    print()

    print(
        "==============================="
    )

    print(
        "ESCENARIO 1 - AUTONOMOUS MODE"
    )

    print(
        "==============================="
    )


    execute_test(

        "crear una aplicación web para un cliente",

        "autonomous"

    )



    print()

    print(
        "==============================="
    )

    print(
        "ESCENARIO 2 - HUMAN MODE"
    )

    print(
        "==============================="
    )


    result = execute_test(

        "modificar kernel Linux del sistema",

        "human"

    )



    if result.get(
        "status"
    ) == "waiting_approval":


        print()

        print(
            "SOLICITANDO APROBACION HUMANA"
        )


        print(

            autonomy_manager.approve()

        )



    print()

    print(
        "MEMORIA FINAL"
    )


    print(

        pipeline_memory.stats()

    )



    print()

    print("=" * 60)

    print(
        "OMEGA FULL SYSTEM TEST FINALIZADO"
    )

    print("=" * 60)




if __name__ == "__main__":

    main()
