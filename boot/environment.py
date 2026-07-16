#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA
BOOT SYSTEM

environment.py

Detecta automáticamente el entorno donde se
está ejecutando SYNERGIA.

ACEA V1.0

============================================================
"""

import os
import platform
import socket
import sys
from pathlib import Path


class Environment:

    def __init__(self):

        self.info = {}

    # ---------------------------------------------------------

    def detect(self):

        self.info = {

            "hostname": socket.gethostname(),

            "platform": platform.system(),

            "platform_release": platform.release(),

            "platform_version": platform.version(),

            "architecture": platform.machine(),

            "python": platform.python_version(),

            "cwd": str(Path.cwd()),

            "project": str(Path(__file__).resolve().parents[1]),

            "venv": os.environ.get("VIRTUAL_ENV", "No VirtualEnv"),

            "user": os.environ.get("USER", "unknown"),

        }

        return self.info

    # ---------------------------------------------------------

    def get(self):

        return self.info

    # ---------------------------------------------------------

    def print_summary(self):

        print()

        print("=" * 60)

        print("        SYNERGIA OMEGA BOOT SYSTEM")

        print("=" * 60)

        print()

        print(f"Host.............. {self.info['hostname']}")

        print(f"Sistema.......... {self.info['platform']}")

        print(f"Versión.......... {self.info['platform_release']}")

        print(f"Arquitectura..... {self.info['architecture']}")

        print(f"Python........... {self.info['python']}")

        print(f"Usuario.......... {self.info['user']}")

        print(f"Proyecto......... {self.info['project']}")

        print(f"VirtualEnv....... {self.info['venv']}")

        print()

        print("=" * 60)

        print()

    # ---------------------------------------------------------

    def status(self):

        return self.info
