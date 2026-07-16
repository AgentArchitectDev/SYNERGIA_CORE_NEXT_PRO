#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from ai.director.autonomy_manager import (
    autonomy_manager
)



def main():


    print()

    print("="*60)

    print(
        "SYNERGIA AUTONOMY MANAGER TEST"
    )

    print("="*60)


    print()


    print(
        autonomy_manager.initialize(
            "autonomous"
        )
    )


    print()


    print(
        autonomy_manager.evaluate(

            "crear una aplicación web",

            [
                "Business Agent",
                "Developer Agent"
            ]

        )
    )


    print()


    print(
        autonomy_manager.set_mode(
            "human"
        )
    )


    print()


    print(
        autonomy_manager.evaluate(

            "optimizar código Python",

            [
                "Developer Agent"
            ]

        )
    )


    print()


    print(
        autonomy_manager.approve()
    )


    print()


    print(
        autonomy_manager.status()
    )



if __name__ == "__main__":

    main()
