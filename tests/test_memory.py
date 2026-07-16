#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from ai.director.pipeline_memory import (
    pipeline_memory
)



def main():


    print()

    print("="*60)

    print(
        "SYNERGIA PIPELINE MEMORY TEST"
    )

    print("="*60)


    print()


    print(
        pipeline_memory.initialize()
    )


    print()


    print(
        pipeline_memory.save(

            "crear una aplicación web gastronómica",

            "business",

            [
                "Business Agent",
                "Developer Agent"
            ],

            "qwen",

            "completed"

        )
    )


    print()


    print(
        pipeline_memory.save(

            "optimizar código Python",

            "development",

            [
                "Developer Agent"
            ],

            "deepseek-coder",

            "completed"

        )
    )


    print()


    print(
        "BUSQUEDA"
    )


    print(

        pipeline_memory.search(
            "Python"
        )

    )


    print()


    print(
        pipeline_memory.stats()
    )



if __name__ == "__main__":

    main()
