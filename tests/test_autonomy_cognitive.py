#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from ai.director.autonomy_manager import (
    autonomy_manager
)



def main():


    print()

    print("="*60)

    print(
        "SYNERGIA AUTONOMY + COGNITIVE TEST"
    )

    print("="*60)



    print(
        autonomy_manager.initialize(
            "autonomous"
        )
    )



    print()

    print(
        "CASO 1 AUTO DECISION"
    )


    print(

        autonomy_manager.evaluate(

            "crear una página web simple"

        )

    )



    print()

    print(
        "CASO 2 RIESGO ALTO"
    )


    print(

        autonomy_manager.evaluate(

            "modificar kernel Linux"

        )

    )



    print()

    print(
        "APROBACION HUMANA"
    )


    print(

        autonomy_manager.approve()

    )



    print()

    print(

        autonomy_manager.status()

    )



    print()

    print("="*60)

    print(
        "TEST FINALIZADO"
    )

    print("="*60)



if __name__ == "__main__":

    main()
