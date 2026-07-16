#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

MODEL ROUTER TEST

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

Valida:

REQUEST

   |

MODEL ROUTER

   |

CATEGORY

   |

MODEL SELECTION


============================================================
"""


from ai.director.model_router import (
    model_router
)



def main():

    print()

    print("="*60)

    print(
        "SYNERGIA OMEGA MODEL ROUTER TEST"
    )

    print("="*60)



    print()

    print(
        "Inicializando Model Router..."
    )


    print(
        model_router.initialize(
            "autonomous"
        )
    )



    print()

    print(
        "ESCENARIO 1"
    )

    print(
        "Desarrollo Python"
    )


    result1 = model_router.select(

        "optimizar código Python del sistema"

    )


    print()

    print(result1)



    print()

    print(
        "ESCENARIO 2"
    )

    print(
        "Business"
    )


    result2 = model_router.select(

        "crear una aplicación web para un cliente"

    )


    print()

    print(result2)



    print()

    print(
        "CAMBIO A HUMAN MODE"
    )


    print(

        model_router.set_mode(
            "human"
        )

    )



    print()

    print(
        model_router.select(

            "modificar arquitectura del sistema"

        )

    )



    print()

    print(
        "ESTADO FINAL"
    )


    print(

        model_router.status()

    )



    print()

    print("="*60)

    print(
        "MODEL ROUTER TEST FINALIZADO"
    )

    print("="*60)



if __name__ == "__main__":

    main()
