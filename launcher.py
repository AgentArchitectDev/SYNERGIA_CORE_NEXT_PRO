#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================
SYNERGIA OMEGA
BOOT LAUNCHER

CORE IA SYSTEMS

Archivo:
launcher.py

Punto único de entrada del sistema.

A partir de este archivo se inicia
todo el Boot System de SYNERGIA.

ACEA VERSION 1.0
============================================================
"""

from pathlib import Path
import sys


# ----------------------------------------------------------
# Agregar automáticamente el proyecto al PYTHONPATH
# ----------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# ----------------------------------------------------------
# Boot Manager
# ----------------------------------------------------------

from boot.boot_manager import BootManager


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------

def main():

    manager = BootManager()

    manager.boot()


# ----------------------------------------------------------

if __name__ == "__main__":
    main()
