from ai.modules.memory_module import memory_module
from ai.modules.research_module import research_module
from ai.modules.export_module import export_module


class ModuleRegistry:

    def __init__(self):

        self.modules = {
            "memory": memory_module,
            "research": research_module,
            "export": export_module
        }

    def get(self, name: str):

        return self.modules.get(name)

    def list(self):

        return list(self.modules.keys())


module_registry = ModuleRegistry()
