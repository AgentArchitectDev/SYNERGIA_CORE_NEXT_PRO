"""
=========================================================
SYNERGIA OS

Module Registry V1.3

ACEA Dynamic Registry

Enterprise Cognitive Operating System AI
=========================================================
"""

import json
from pathlib import Path


class ModuleRegistry:

    def __init__(self):

        self.modules = {}

        self.registry_path = (
            Path(__file__).resolve().parent.parent
            / "storage"
            / "modules"
            / "modules.json"
        )

        self.load()

    # =====================================================
    # LOAD REGISTRY
    # =====================================================

    def load(self):

        try:

            with open(
                self.registry_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.modules = json.load(file)

            print(
                f"[ModuleRegistry] {len(self.modules)} modules loaded."
            )

        except Exception as error:

            print(
                "[ModuleRegistry]",
                error
            )

            self.modules = {}

    # =====================================================
    # RELOAD
    # =====================================================

    def reload(self):

        self.load()

    # =====================================================
    # EXISTS
    # =====================================================

    def exists(self, key):

        return key in self.modules

    # =====================================================
    # GET MODULE
    # =====================================================

    def get_module(self, key):

        return self.modules.get(key)

    # =====================================================
    # GET ALL
    # =====================================================

    def get_all_modules(self):

        return self.modules

    # =====================================================
    # GET TITLE
    # =====================================================

    def get_title(self, key):

        module = self.get_module(key)

        if module:

            return module.get(
                "title",
                key
            )

        return key

    # =====================================================
    # GET ICON
    # =====================================================

    def get_icon(self, key):

        module = self.get_module(key)

        if module:

            return module.get(
                "icon",
                "📦"
            )

        return "❓"

    # =====================================================
    # GET PAGE
    # =====================================================

    def get_page(self, key):

        module = self.get_module(key)

        if module:

            return module.get(
                "page"
            )

        return None

    # =====================================================
    # GET DESCRIPTION
    # =====================================================

    def get_description(self, key):

        module = self.get_module(key)

        if module:

            return module.get(
                "description",
                ""
            )

        return ""

    # =====================================================
    # GET CATEGORY
    # =====================================================

    def get_category(self, key):

        module = self.get_module(key)

        if module:

            return module.get(
                "category",
                "general"
            )

        return "general"

    # =====================================================
    # GET TYPE
    # =====================================================

    def get_type(self, key):

        module = self.get_module(key)

        if module:

            return module.get(
                "type",
                "unknown"
            )

        return "unknown"

    # =====================================================
    # GET STATUS
    # =====================================================

    def get_status(self, key):

        module = self.get_module(key)

        if module:

            return module.get(
                "status",
                "unknown"
            )

        return "unknown"

    # =====================================================
    # GET VERSION
    # =====================================================

    def get_version(self, key):

        module = self.get_module(key)

        if module:

            return module.get(
                "version",
                "-"
            )

        return "-"

    # =====================================================
    # ONLINE MODULES
    # =====================================================

    def get_online_modules(self):

        return {

            key: value

            for key, value in self.modules.items()

            if value.get("status") == "online"

        }

    # =====================================================
    # STANDBY MODULES
    # =====================================================

    def get_standby_modules(self):

        return {

            key: value

            for key, value in self.modules.items()

            if value.get("status") == "standby"

        }

    # =====================================================
    # BY CATEGORY
    # =====================================================

    def by_category(self, category):

        return {

            key: value

            for key, value in self.modules.items()

            if value.get("category") == category

        }

    # =====================================================
    # BY TYPE
    # =====================================================

    def by_type(self, module_type):

        return {

            key: value

            for key, value in self.modules.items()

            if value.get("type") == module_type

        }

    # =====================================================
    # STATISTICS
    # =====================================================

    def statistics(self):

        return {

            "total": len(self.modules),

            "online": len(self.get_online_modules()),

            "standby": len(self.get_standby_modules())

        }
