"""
===============================================================
SYNERGIA CORE NEXT_PRO
Runtime Manager V5
===============================================================

Motor principal del Runtime.

Responsabilidades:

- administrar ciclo de vida
- coordinar Scheduler
- coordinar Orchestrator
- emitir eventos
- mantener contexto
- registrar actividad
- administrar sesiones

===============================================================
"""

import time

from ai.runtime.runtime_core.runtime_state import runtime_state
from ai.runtime.runtime_core.runtime_logger import runtime_logger
from ai.runtime.runtime_core.event_bus import event_bus
from ai.runtime.runtime_core.task_queue import task_queue
from ai.runtime.runtime_core.context_manager import context_manager
from ai.runtime.runtime_core.session_manager import session_manager

from ai.core.scheduler import scheduler
from ai.core.orchestrator import orchestrator


class RuntimeManager:

    def __init__(self):

        self.version = "5.0"

        self.running = False

    # ---------------------------------------------------------

    def boot(self):

        runtime_state.start()

        self.running = True

        runtime_logger.info("Runtime started")

        event_bus.emit("runtime_boot")

        return True

    # ---------------------------------------------------------

    def shutdown(self):

        runtime_state.stop()

        self.running = False

        runtime_logger.info("Runtime stopped")

        event_bus.emit("runtime_shutdown")

    # ---------------------------------------------------------

    def execute(self, input_text):

        if not self.running:

            self.boot()

        runtime_logger.info(
            f"INPUT -> {input_text}"
        )

        runtime_state.current_task = input_text

        runtime_state.total_tasks += 1

        context_manager.set(
            "last_input",
            input_text
        )

        event_bus.emit(
            "new_request",
            input_text
        )

        start = time.time()

        try:

            response = orchestrator.process(
                input_text
            )

            latency = round(
                time.time() - start,
                4
            )

            runtime_logger.info(
                f"Execution OK ({latency}s)"
            )

            event_bus.emit(
                "execution_ok"
            )

            runtime_state.current_task = None

            return response

        except Exception as e:

            runtime_state.total_errors += 1

            runtime_logger.error(str(e))

            event_bus.emit(
                "execution_error",
                str(e)
            )

            runtime_state.current_task = None

            raise

    # ---------------------------------------------------------

    def enqueue(self, task):

        task_queue.push(task)

    # ---------------------------------------------------------

    def next_task(self):

        return task_queue.pop()

    # ---------------------------------------------------------

    def status(self):

        return {

            "version": self.version,

            "running": self.running,

            "session":

                session_manager.current(),

            "runtime":

                runtime_state.status(),

            "queue":

                task_queue.size()

        }


runtime_manager = RuntimeManager()
