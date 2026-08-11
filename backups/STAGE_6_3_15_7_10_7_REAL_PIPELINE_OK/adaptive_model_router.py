"""
SYNERGIA CORE NEXT PRO

ADAPTIVE MODEL ROUTER ACEA

STAGE:
6.3.15.7.10.6

Responsabilidad:
- Seleccion inteligente de modelos IA
- Compatibilidad TaskEngine
- Resolucion AUTO
- Soporte modelo manual
- Fallback seguro
- Tracking de decisiones
- Preparado para Runtime Memory
- Preparado para Learning Loop

Pipeline:

TaskEngine
    |
    v
AdaptiveModelRouter
    |
    v
Model Selection
    |
    v
Ollama Provider
    |
    v
Runtime Memory
"""

from __future__ import annotations

import time
import logging

from dataclasses import dataclass, field

from typing import (
    Dict,
    List,
    Optional,
    Any
)


logger = logging.getLogger(
    "SYNERGIA.ADAPTIVE_ROUTER"
)


@dataclass
class ModelProfile:

    name: str

    provider: str = "ollama"

    capabilities: List[str] = field(
        default_factory=list
    )

    priority: int = 1

    speed_score: int = 5

    intelligence_score: int = 5

    memory_required: int = 4

    enabled: bool = True



class AdaptiveModelRouter:


    def __init__(
        self,
        runtime_memory=None,
        provider="ollama"
    ):

        self.runtime_memory = runtime_memory

        self.provider = provider


        self.models: Dict[str, ModelProfile] = {


            "llama3.2:1b": ModelProfile(

                name="llama3.2:1b",

                capabilities=[
                    "simple",
                    "basic",
                    "fast",
                    "chat"
                ],

                speed_score=10,

                intelligence_score=4,

                memory_required=1
            ),


            "llama3.2:3b": ModelProfile(

                name="llama3.2:3b",

                capabilities=[
                    "general",
                    "business",
                    "chat",
                    "basic_code"
                ],

                speed_score=8,

                intelligence_score=6,

                memory_required=3
            ),


            "qwen2.5-coder:7b": ModelProfile(

                name="qwen2.5-coder:7b",

                capabilities=[
                    "coding",
                    "python",
                    "debug",
                    "architecture"
                ],

                speed_score=6,

                intelligence_score=8,

                memory_required=6
            ),


            "deepseek-coder-v2:16b": ModelProfile(

                name="deepseek-coder-v2:16b",

                capabilities=[
                    "advanced_code",
                    "analysis",
                    "architecture",
                    "reasoning"
                ],

                speed_score=3,

                intelligence_score=10,

                memory_required=12
            )

        }


        self.selection_history = []


        print(
            "[ADAPTIVE MODEL ROUTER LOADED]"
        )


    def select_model(
        self,
        task: Any,
        requested_model: Optional[str] = None
    ):

        task_type = self.detect_task_type(
            task
        )


        if requested_model:

            if requested_model in self.models:

                return self.register_selection(
                    task,
                    requested_model,
                    "MANUAL"
                )


        memory_model = self.get_memory_recommendation(
            task_type
        )


        if memory_model:

            return self.register_selection(
                task,
                memory_model,
                "RUNTIME_MEMORY"
            )


        selected = self.calculate_best_model(
            task_type
        )


        return self.register_selection(
            task,
            selected,
            "ADAPTIVE"
        )


    def detect_task_type(
        self,
        task
    ):

        text = str(task).lower()


        if any(
            word in text
            for word in [
                "python",
                "codigo",
                "code",
                "api",
                "debug"
            ]
        ):

            return "coding"


        if any(
            word in text
            for word in [
                "empresa",
                "web",
                "marketing",
                "business"
            ]
        ):

            return "business"


        if any(
            word in text
            for word in [
                "analizar",
                "arquitectura",
                "diseño"
            ]
        ):

            return "analysis"


        return "general"
    def calculate_best_model(
        self,
        task_type
    ):

        ranking = []


        for name, profile in self.models.items():


            if not profile.enabled:

                continue


            score = 0


            if task_type in profile.capabilities:

                score += 20


            score += profile.intelligence_score

            score += profile.priority

            score -= profile.memory_required


            ranking.append(
                (
                    score,
                    name
                )
            )


        if not ranking:

            return "llama3.2:1b"


        ranking.sort(
            reverse=True
        )


        return ranking[0][1]



    def get_memory_recommendation(
        self,
        task_type
    ):

        if not self.runtime_memory:

            return None


        try:

            data = self.runtime_memory.get(
                "preferred_models"
            )


            if not data:

                return None


            return data.get(
                task_type
            )


        except Exception:

            return None



    def register_selection(
        self,
        task,
        model,
        reason
    ):

        event = {

            "timestamp": time.time(),

            "task": str(task),

            "model": model,

            "reason": reason
        }


        self.selection_history.append(
            event
        )


        logger.info(
            f"Adaptive Router -> {model} [{reason}]"
        )


        return model



    def available_models(
        self
    ):

        return list(
            self.models.keys()
        )



    def status(
        self
    ):

        return {

            "provider": self.provider,

            "models": self.available_models(),

            "selections": len(
                self.selection_history
            )

        }



    def enable_model(
        self,
        name
    ):

        if name in self.models:

            self.models[name].enabled = True



    def disable_model(
        self,
        name
    ):

        if name in self.models:

            self.models[name].enabled = False




def get_adaptive_router(
    runtime_memory=None
):

    return AdaptiveModelRouter(
        runtime_memory=runtime_memory
    )
