#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

BOOT PROFILE

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

Este módulo administra los perfiles de arranque
de cada nodo del ecosistema SYNERGIA.

Actualmente:

    MAQ1
    MAQ2
    AUTO

En futuras versiones:

    CLOUD
    SERVER
    CLIENT
    VPS
    EDGE
    REMOTE

============================================================
"""

from copy import deepcopy


class BootProfile:

    """
    Administrador de perfiles de arranque.
    """

    # ------------------------------------------------------

    def __init__(self):

        self.current = None

        self.profiles = {

            "MAQ1": {

                "name": "MAQ1",

                "description": "Nodo Principal IA",

                "workspace": True,

                "editor": True,

                "runtime": True,

                "runtime_manager": True,

                "agent_manager": True,

                "core_bridge": True,

                "ollama": True,

                "memory": True,

                "dashboard": True,

                "monitor": True,

                "development": True,

                "production": True,

                "models": "FULL"

            },

            "MAQ2": {

                "name": "MAQ2",

                "description": "Nodo Desarrollo",

                "workspace": True,

                "editor": True,

                "runtime": True,

                "runtime_manager": True,

                "agent_manager": True,

                "core_bridge": True,

                "ollama": True,

                "memory": True,

                "dashboard": True,

                "monitor": True,

                "development": True,

                "production": False,

                "models": "DEV"

            },

            "AUTO": {

                "name": "AUTO",

                "description": "Detección Automática",

                "workspace": True,

                "editor": True,

                "runtime": True,

                "runtime_manager": True,

                "agent_manager": True,

                "core_bridge": True,

                "ollama": True,

                "memory": True,

                "dashboard": True,

                "monitor": True,

                "development": True,

                "production": True,

                "models": "AUTO"

            }

        }

    # ------------------------------------------------------

    def load(self, profile_name):

        if profile_name not in self.profiles:

            raise ValueError(
                f"Perfil inexistente: {profile_name}"
            )

        self.current = deepcopy(
            self.profiles[profile_name]
        )

        print()

        print("Perfil cargado")

        print("-------------------------")

        print("Nombre :", self.current["name"])

        print("Modo   :", self.current["description"])

        print()

        return self.current

    # ------------------------------------------------------

    def current_profile(self):

        return self.current

    # ------------------------------------------------------

    def get(self, key, default=None):

        if self.current is None:

            return default

        return self.current.get(key, default)

    # ------------------------------------------------------

    def available_profiles(self):

        return list(
            self.profiles.keys()
        )

    # ------------------------------------------------------

    def status(self):

        return {

            "component": "OMEGA Boot Profile",

            "current": self.current,

            "profiles": self.available_profiles(),

            "loaded": self.current is not None

        }


boot_profile = BootProfile()
