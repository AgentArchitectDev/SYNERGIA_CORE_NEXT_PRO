#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from ai.director.cognitive_decision import (
    cognitive_decision
)



def main():


    print()

    print("="*60)

    print(
        "SYNERGIA COGNITIVE DECISION TEST"
    )

    print("="*60)



    print()

    print(
        cognitive_decision.initialize()
    )



    #
    # CASO 1
    #

    print()

    print(
        "ESCENARIO 1"
    )

    print(
        "Crear una página web simple"
    )


    print()

    print(

        cognitive_decision.evaluate(

            "crear una página web simple"

        )

    )



    #
    # CASO 2
    #

    print()

    print(
        "ESCENARIO 2"
    )

    print(
        "Modificar kernel Linux"
    )


    print()

    print(

        cognitive_decision.evaluate(

            "modificar kernel Linux del sistema"

        )

    )



    #
    # STATUS
    #

    print()

    print(

        cognitive_decision.status()

    )



    print()

    print(
        "="*60
    )

    print(
        "COGNITIVE DECISION TEST FINALIZADO"
    )

    print(
        "="*60
    )



if __name__ == "__main__":

    main()
