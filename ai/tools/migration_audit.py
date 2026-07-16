"""
SYNERGIA V3 - Migration Audit Tool

Verifica:
- Migración completa de core_system → core
- Imports rotos
- módulos sin run()
- dependencias legacy
"""

import os
import importlib
import inspect


LEGACY_PATH = "ai/core_system/core"
NEW_CORE_PATH = "ai/core"


class MigrationAudit:

    def __init__(self):

        self.errors = []
        self.warnings = []
        self.ok = []

    # -------------------------------------

    def check_legacy_exists(self):

        if os.path.exists(LEGACY_PATH):
            self.warnings.append(
                "CORE LEGACY AÚN EXISTE (core_system/core)"
            )
        else:
            self.ok.append("CORE LEGACY ELIMINADO O INACTIVO")

    # -------------------------------------

    def check_imports_core(self):

        modules_to_check = [
            "ai.core.task_engine",
            "ai.core.memory_context",
            "ai.core.export_manager"
        ]

        for module_name in modules_to_check:

            try:
                importlib.import_module(module_name)
                self.ok.append(f"IMPORT OK: {module_name}")

            except Exception as e:
                self.errors.append(f"IMPORT ERROR: {module_name} → {e}")

    # -------------------------------------

    def check_agents_interface(self):

        agents = [
            "ai.agents.memory_agent",
            "ai.agents.export_agent",
            "ai.agents.research_agent"
        ]

        for agent_path in agents:

            try:
                module = importlib.import_module(agent_path)

                # buscar clases
                classes = inspect.getmembers(module, inspect.isclass)

                found_run = False

                for _, cls in classes:

                    if hasattr(cls, "run"):
                        found_run = True

                if found_run:
                    self.ok.append(f"AGENT OK: {agent_path}")
                else:
                    self.errors.append(f"AGENT SIN run(): {agent_path}")

            except Exception as e:
                self.errors.append(f"AGENT ERROR: {agent_path} → {e}")

    # -------------------------------------

    def check_kernel_integrity(self):

        try:
            from ai.kernel.kernel import kernel

            if hasattr(kernel, "execute"):
                self.ok.append("KERNEL EXECUTE OK")
            else:
                self.errors.append("KERNEL SIN EXECUTE")

        except Exception as e:
            self.errors.append(f"KERNEL ERROR → {e}")

    # -------------------------------------

    def run(self):

        print("\n==============================")
        print("SYNERGIA MIGRATION AUDIT")
        print("==============================\n")

        self.check_legacy_exists()
        self.check_imports_core()
        self.check_agents_interface()
        self.check_kernel_integrity()

        self.report()

    # -------------------------------------

    def report(self):

        print("✔ OK:\n")
        for o in self.ok:
            print("  -", o)

        print("\n⚠ WARNINGS:\n")
        for w in self.warnings:
            print("  -", w)

        print("\n❌ ERRORS:\n")
        for e in self.errors:
            print("  -", e)

        print("\n==============================")

        if not self.errors:
            print("🚀 MIGRACIÓN LISTA PARA FASE 5")
        else:
            print("⛔ MIGRACIÓN INCOMPLETA - NO PASAR A FASE 5")

        print("==============================\n")


if __name__ == "__main__":
    audit = MigrationAudit()
    audit.run()
