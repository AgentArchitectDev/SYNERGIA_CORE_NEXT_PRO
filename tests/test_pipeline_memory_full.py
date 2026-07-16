#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

PIPELINE MEMORY FULL TEST

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

Valida:

PIPELINE EXECUTION

        |

        v

PIPELINE MEMORY

        |

        v

SEARCH / RECOVERY


============================================================
"""


from ai.director.pipeline_memory import (
    pipeline_memory
)



def main():


    print()

    print("=" * 60)

    print(
        "SYNERGIA OMEGA PIPELINE MEMORY FULL TEST"
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
        "GUARDANDO EJECUCIONES"
    )



    record1 = pipeline_memory.save(

        request=
        "crear una aplicación web gastronómica",

        category=
        "business",

        agents=[
            "Business Agent",
            "Developer Agent"
        ],

        model=
        "qwen",

        result=
        "completed"

    )


    print()

    print(record1)



    record2 = pipeline_memory.save(

        request=
        "optimizar código Python del sistema",

        category=
        "development",

        agents=[
            "Developer Agent"
        ],

        model=
        "deepseek-coder",

        result=
        "completed"

    )


    print()

    print(record2)



    record3 = pipeline_memory.save(

        request=
        "ejecutar modelo local Ollama",

        category=
        "ai",

        agents=[
            "Runtime Agent"
        ],

        model=
        "mistral",

        result=
        "completed"

    )


    print()

    print(record3)



    print()

    print(
        "BUSQUEDA PYTHON"
    )


    print(

        pipeline_memory.search(
            "Python"
        )

    )



    print()

    print(
        "BUSQUEDA WEB"
    )


    print(

        pipeline_memory.search(
            "web"
        )

    )



    print()

    print(
        "ESTADO MEMORY"
    )


    print(

        pipeline_memory.stats()

    )



    print()

    print("=" * 60)

    print(
        "PIPELINE MEMORY FULL TEST FINALIZADO"
    )

    print("=" * 60)



if __name__ == "__main__":

    main()
