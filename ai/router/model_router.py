"""
============================================================
SYNERGIA MODEL ROUTER
Seleccion inteligente de modelos por tarea
============================================================
"""

class ModelRouter:

    def __init__(self):

        # mapa de tareas → modelos optimizados
        self.model_map = {
            "research": "llama3.2:3b",
            "memory": "phi3:mini",
            "export": "mistral:latest",
            "code": "deepseek-coder-v2:16b",
            "ollama": "llama3.1:latest",
            "default": "llama3.1:latest"
        }

    # -------------------------------------------------

    def select(self, task: str) -> str:

        return self.model_map.get(task, self.model_map["default"])


model_router = ModelRouter()
