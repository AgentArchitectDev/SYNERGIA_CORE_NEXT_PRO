#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA MODEL RUNTIME TEST

ACEA

============================================================
"""


from ai.runtime.model_runtime import (
    model_runtime
)



def main():


    print()

    print("=" * 60)

    print(
        "SYNERGIA MODEL RUNTIME TEST"
    )

    print("=" * 60)


    print()


    print(
        model_runtime.initialize()
    )


    print()


    result = model_runtime.execute(

        "deepseek-coder",

        "Optimizar código Python del sistema"

    )


    print(result)


    print()


    print(
        model_runtime.status()
    )


    print()

    print("=" * 60)

    print(
        "MODEL RUNTIME TEST FINALIZADO"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()
