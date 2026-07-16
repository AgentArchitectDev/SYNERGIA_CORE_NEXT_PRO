#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

BOOT MENU

ACEA VERSION 1.0

CORE IA SYSTEMS

============================================================
"""

class BootMenu:

    """
    Menú principal del Boot.

    En versiones futuras será reemplazado
    por un menú gráfico Qt.

    La API permanecerá igual.
    """

    def __init__(self):

        self.machine = None
        self.mode = None

    # ---------------------------------------------------------

    def separator(self):

        print("-" * 60)

    # ---------------------------------------------------------

    def select_machine(self):

        while True:

            self.separator()

            print("SELECCIONAR PERFIL")

            self.separator()

            print()

            print("A) MAQ1  (Producción IA)")
            print()

            print("B) MAQ2  (Desarrollo)")
            print()

            print("C) AUTO")
            print()

            print("Q) Salir")
            print()

            option = input("Seleccione opción : ").strip().upper()

            if option == "A":

                self.machine = "MAQ1"

                break

            elif option == "B":

                self.machine = "MAQ2"

                break

            elif option == "C":

                self.machine = "AUTO"

                break

            elif option == "Q":

                raise SystemExit()

            else:

                print()

                print("Opción incorrecta.")

        return self.machine

    # ---------------------------------------------------------

    def select_mode(self):

        while True:

            print()

            self.separator()

            print("MODO DE ARRANQUE")

            self.separator()

            print()

            print("1) Crear / Continuar Desarrollo")

            print()

            print("2) Ejecutar Sistema")

            print()

            print("3) Diagnóstico")

            print()

            print("4) Benchmark")

            print()

            print("5) Runtime")

            print()

            print("6) IA Completa")

            print()

            option = input("Modo : ").strip()

            modes = {

                "1": "development",

                "2": "production",

                "3": "diagnostic",

                "4": "benchmark",

                "5": "runtime",

                "6": "ai",

            }

            if option in modes:

                self.mode = modes[option]

                break

            print()

            print("Modo inválido.")

        return self.mode

    # ---------------------------------------------------------

    def status(self):

        return {

            "component": "OMEGA Boot Menu",

            "machine": self.machine,

            "mode": self.mode,

        }


boot_menu = BootMenu()
