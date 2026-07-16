"""
===========================================================
SYNERGIA CORE NEXT_PRO
Base Agent v4.0
===========================================================

Clase base para todos los agentes del sistema.

Todos los agentes deben heredar de BaseAgent.

Compatible con:

- Runtime Manager
- Scheduler
- Orchestrator
- Agent Evolution Layer
- Dashboard
- Cognitive Loop

===========================================================
"""

from abc import ABC, abstractmethod
import time


class BaseAgent(ABC):

    def __init__(self, name: str = "base"):

        self.name = name

        self.created_at = time.time()

        self.executions = 0

        self.success = 0

        self.failures = 0

        self.last_execution = None

        self.enabled = True

    # --------------------------------------------------

    @abstractmethod
    def run(self, input_text: str):
        """
        Método obligatorio.
        Debe implementarlo cada agente.
        """
        pass

    # --------------------------------------------------

    def execute(self, input_text: str):

        if not self.enabled:

            return {
                "status": "disabled",
                "agent": self.name
            }

        self.executions += 1

        self.last_execution = time.time()

        start = time.time()

        try:

            result = self.run(input_text)

            self.success += 1

            latency = round(time.time() - start, 4)

            return {
                "agent": self.name,
                "status": "executed",
                "latency": latency,
                "result": result
            }

        except Exception as e:

            self.failures += 1

            latency = round(time.time() - start, 4)

            return {
                "agent": self.name,
                "status": "error",
                "latency": latency,
                "error": str(e)
            }

    # --------------------------------------------------

    def enable(self):

        self.enabled = True

    # --------------------------------------------------

    def disable(self):

        self.enabled = False

    # --------------------------------------------------

    def reset(self):

        self.executions = 0
        self.success = 0
        self.failures = 0

    # --------------------------------------------------

    def statistics(self):

        return {

            "executions": self.executions,

            "success": self.success,

            "failures": self.failures

        }

    # --------------------------------------------------

    def uptime(self):

        return round(
            time.time() - self.created_at,
            2
        )

    # --------------------------------------------------

    def status(self):

        return {

            "name": self.name,

            "enabled": self.enabled,

            "executions": self.executions,

            "success": self.success,

            "failures": self.failures,

            "uptime": self.uptime()

        }
