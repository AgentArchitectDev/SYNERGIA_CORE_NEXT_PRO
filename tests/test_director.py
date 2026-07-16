#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

DIRECTOR TEST

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

Valida:

REQUEST
   |
   v
OMEGA DIRECTOR
   |
   v
DECISION
   |
   v
PLAN DE AGENTES

============================================================
"""


from ai.director.omega_director import (
    omega_director
)



def main():

    print()

    print("="*60)

    print(
        "SYNERGIA OMEGA DIRECTOR TEST"
    )

    print("="*60)



    print()

    print(
        "Inicializando OMEGA Director..."
    )



    print(
        omega_director.initialize()
    )



    print()

    print(
        "ESCENARIO 1"
    )

    print(
        "Crear una aplicación web para cliente"
    )



    result1 = omega_director.execute(

        "crear una aplicación web para un cliente"

    )


    print()

    print(result1)



    print()

    print(
        "ESCENARIO 2"
    )

    print(
        "Optimizar código Python"
    )



    result2 = omega_director.execute(

        "optimizar código Python del sistema"

    )


    print()

    print(result2)



    print()

    print(
        "ESTADO DIRECTOR"
    )



    print(

        omega_director.status()

    )



    print()

    print("="*60)

    print(
        "DIRECTOR TEST FINALIZADO"
    )

    print("="*60)



if __name__ == "__main__":

    main()
