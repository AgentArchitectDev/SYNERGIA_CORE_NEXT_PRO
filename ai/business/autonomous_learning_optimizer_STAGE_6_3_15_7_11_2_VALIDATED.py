"""
SYNERGIA CORE NEXT PRO

AUTONOMOUS LEARNING OPTIMIZER

STAGE 6.3.15.7.11.2

AUTONOMOUS OPTIMIZER -> ROUTER INTEGRATION

Responsabilidades:

- Leer Self Learning Feedback
- Evaluar estrategia de modelos
- Generar decisiones de optimización
- Exponer decisión al Adaptive Model Router
- Mantener compatibilidad con Runtime Memory
- Mantener compatibilidad con TaskEngine
- No modificar automáticamente modelos todavía

Pipeline:

Runtime Memory
      |
      v
Self Learning Loop
      |
      v
Self Learning Feedback
      |
      v
Autonomous Learning Optimizer
      |
      v
Adaptive Model Router
"""

from datetime import datetime

from ai.business.self_learning_feedback import (
    self_learning_feedback
)


print(
    "[AUTONOMOUS LEARNING OPTIMIZER LOADED]"
)


class AutonomousLearningOptimizer:

    def __init__(self, adaptive_router=None):

        self.adaptive_router = adaptive_router

        self.last_optimization = None

        print(
            "[AUTONOMOUS LEARNING OPTIMIZER READY]"
        )

    # ========================================================
    # ROUTER CONNECTION
    # ========================================================

    def connect_router(self, adaptive_router):

        self.adaptive_router = adaptive_router

        return True

    # ========================================================
    # OPTIMIZATION ANALYSIS
    # ========================================================

    def optimize(self):

        feedback = (
            self_learning_feedback.generate()
        )

        success_rate = feedback.get(
            "success_rate",
            0
        )

        router_feedback = feedback.get(
            "router_feedback",
            {}
        )

        if success_rate >= 90:

            strategy = (
                "KEEP_CURRENT_MODEL_STRATEGY"
            )

            reason = (
                "HIGH_SUCCESS_RATE"
            )

        elif success_rate >= 70:

            strategy = (
                "CONTINUE_LEARNING"
            )

            reason = (
                "ACCEPTABLE_PERFORMANCE"
            )

        else:

            strategy = (
                "REVIEW_MODEL_SELECTION"
            )

            reason = (
                "LOW_PERFORMANCE"
            )

        optimization = {

            "timestamp":
                datetime.now().isoformat(),

            "source":
                "AUTONOMOUS_LEARNING_OPTIMIZER",

            "success_rate":
                success_rate,

            "decision": {

                "strategy":
                    strategy,

                "confidence":
                    router_feedback.get(
                        "confidence",
                        0
                    ),

                "reason":
                    reason

            },

            "router_integration": {

                "connected":
                    self.adaptive_router is not None,

                "status":
                    "READY"

            }

        }

        self.last_optimization = optimization

        return optimization

    # ========================================================
    # ROUTER DECISION BRIDGE
    # ========================================================

    def get_router_decision(self):

        if self.last_optimization is None:

            self.optimize()

        decision = (
            self.last_optimization
            .get("decision", {})
        )

        return {

            "strategy":
                decision.get(
                    "strategy"
                ),

            "confidence":
                decision.get(
                    "confidence",
                    0
                ),

            "reason":
                decision.get(
                    "reason"
                ),

            "source":
                "AUTONOMOUS_LEARNING_OPTIMIZER"

        }

    # ========================================================
    # ROUTER STATUS
    # ========================================================

    def router_status(self):

        if self.adaptive_router is None:

            return {

                "connected":
                    False,

                "status":
                    "NOT_CONNECTED"

            }

        try:

            return {

                "connected":
                    True,

                "status":
                    self.adaptive_router.status()

            }

        except Exception as exc:

            return {

                "connected":
                    False,

                "status":
                    "ERROR",

                "error":
                    str(exc)

            }

    # ========================================================
    # STATUS
    # ========================================================

    def status(self):

        return {

            "module":
                "AUTONOMOUS_LEARNING_OPTIMIZER",

            "loaded":
                True,

            "router_connected":
                self.adaptive_router is not None,

            "last_optimization":
                self.last_optimization

        }


# ============================================================
# GLOBAL INSTANCE
# ============================================================

autonomous_learning_optimizer = (
    AutonomousLearningOptimizer()
)
