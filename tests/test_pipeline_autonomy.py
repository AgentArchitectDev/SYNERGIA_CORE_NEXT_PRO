#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from ai.director.omega_pipeline import (
    omega_pipeline
)



def main():


    print()

    print("="*60)

    print(
        "SYNERGIA OMEGA PIPELINE AUTONOMY TEST"
    )

    print("="*60)



    #
    # ESCENARIO 1
    # AUTO MODE
    #

    print()

    print(
        "ESCENARIO 1: AUTO MODE"
    )


    print(
        omega_pipeline.initialize(
            "autonomous"
        )
    )


    result = omega_pipeline.execute(

        "crear una aplicación web"

    )


    print()

    print(result)



    #
    # ESCENARIO 2
    # HUMAN MODE
    #

    print()

    print(
        "ESCENARIO 2: HUMAN MODE"
    )


    print(
        omega_pipeline.initialize(
            "human"
        )
    )


    result = omega_pipeline.execute(

        "optimizar código Python"

    )


    print()

    print(result)



    print()

    print(
        "APROBANDO..."
    )


    print(
        omega_pipeline.approve()
    )



    print()

    print(
        omega_pipeline.status()
    )



if __name__ == "__main__":

    main()
