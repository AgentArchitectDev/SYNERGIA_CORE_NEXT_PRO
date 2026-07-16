"""
======================================================================
SYNERGIA CONTROL CENTER
MODULE REGISTRY V5 ENTERPRISE
======================================================================

Responsable de:

• Leer modules.json
• Importar módulos dinámicamente
• Instanciar páginas
• Registrar módulos
• Recargar módulos
• Obtener módulos
• Descargar módulos

======================================================================
"""

import json
import importlib
from pathlib import Path


class ModuleRegistry:

    """
    Registro dinámico de módulos.
    """

    def __init__(self):

        self.modules = {}

        self.instances = {}

        self.loaded = False

        self.config_file = (
            Path(__file__)
            .parent.parent
            / "modules.json"
        )

    # =====================================================
    # LOAD CONFIG
    # =====================================================

    def load_config(self):

        if not self.config_file.exists():

            raise FileNotFoundError(
                self.config_file
            )

        with open(
            self.config_file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        return data

    # =====================================================
    # LOAD MODULES
    # =====================================================

    def load_modules(self):

        data = self.load_config()

        self.modules.clear()

        for module in data["modules"]:

            self.modules[
                module["id"]
            ] = module

        self.loaded = True

    # =====================================================
    # CREATE INSTANCE
    # =====================================================

    def instantiate(self, module_id):

        if module_id not in self.modules:

            raise Exception(
                f"{module_id} no registrado."
            )

        info = self.modules[module_id]

        module = importlib.import_module(
            info["module"]
        )

        cls = getattr(
            module,
            info["class"]
        )

        widget = cls()

        self.instances[module_id] = widget

        return widget

    # =====================================================
    # GET
    # =====================================================

    def get(self, module_id):

        if module_id in self.instances:

            return self.instances[module_id]

        return self.instantiate(module_id)

    # =====================================================
    # GET ALL
    # =====================================================

    def get_all(self):

        result = {}

        for module_id in self.modules:

            result[module_id] = self.get(module_id)

        return result

    # =====================================================
    # UNLOAD
    # =====================================================

    def unload(self, module_id):

        if module_id not in self.instances:

            return

        widget = self.instances[module_id]

        widget.deleteLater()

        del self.instances[module_id]

    # =====================================================
    # RELOAD
    # =====================================================

    def reload(self):

        self.instances.clear()

        self.load_modules()

    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        return {

            "loaded": self.loaded,

            "registered":

                len(self.modules),

            "instantiated":

                len(self.instances),

            "modules":

                list(self.modules.keys())

        }


module_registry = ModuleRegistry()
