#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
============================================================

SYNERGIA OMEGA PIPELINE TEST

ACEA

============================================================
"""


from ai.director.omega_pipeline import (
    omega_pipeline
)



def main():


    print()

    print("=" * 60)

    print(
        "SYNERGIA OMEGA FULL PIPELINE TEST"
    )

    print("=" * 60)


    print()


    print(
        omega_pipeline.initialize()
    )


    print()


    result = omega_pipeline.execute(

        "crear una aplicación web para un cliente"

    )


    print()


    print(
        "RESULTADO PIPELINE"
    )

    print()


    print(result)


    print()


    print(
        omega_pipeline.status()
    )


    print()

    print("=" * 60)

    print(
        "OMEGA PIPELINE TEST FINALIZADO"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()
