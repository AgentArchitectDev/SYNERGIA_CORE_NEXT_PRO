#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA MODEL EXECUTOR TEST

ACEA

============================================================
"""


from ai.director.model_executor import (
    model_executor
)



def main():


    print()

    print("=" * 60)

    print(
        "SYNERGIA MODEL EXECUTOR TEST"
    )

    print("=" * 60)



    print()


    print(
        model_executor.initialize()
    )



    task = {


        "agent":

        "Developer Agent",


        "task":

        "optimizar código Python del sistema"


    }



    print()


    print(
        "Entrada:"
    )


    print(task)



    print()


    result = model_executor.execute(
        task
    )


    print(
        result
    )



    print()


    print(
        model_executor.status()
    )


    print()

    print("=" * 60)

    print(
        "MODEL EXECUTOR TEST FINALIZADO"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()
