"""
SYNERGIA ORCHESTRATOR
Fase 2.7
Event Driven Runtime
"""

from ai.core_system.core.task_engine import TaskEngine
from ai.core_system.core.memory_context_builder import MemoryContextBuilder
from ai.core_system.core.cms_bridge import CMSBridge
from ai.core_system.core.export_manager import ExportManager

from ai.runtime.event_bus import EventBus
from ai.runtime.telemetry import Telemetry
from ai.runtime import events


class Orchestrator:

    def __init__(self):

        self.task_engine = TaskEngine()

        self.memory = MemoryContextBuilder()

        self.exporter = ExportManager()

        self.cms = CMSBridge()

        self.event_bus = EventBus()

        self.telemetry = Telemetry()

    # ------------------------------------------------

    def handle(self, user_input: str):

        self.event_bus.emit(events.INPUT_RECEIVED, user_input)
        self.telemetry.log(events.INPUT_RECEIVED, user_input)

        context = self.memory.build(user_input)

        self.event_bus.emit(events.MEMORY_LOAD, context)
        self.telemetry.log(events.MEMORY_LOAD)

        if "tarea" in user_input.lower():

            self.event_bus.emit(events.INTENT_DETECTED, "TASK")
            self.telemetry.log(events.INTENT_DETECTED, "TASK")

            self.event_bus.emit(events.TASK_STARTED)

            raw_result = self.task_engine.execute(
                user_input,
                context
            )

            self.event_bus.emit(events.TASK_COMPLETED)

        else:

            self.event_bus.emit(events.INTENT_DETECTED, "CHAT")
            self.telemetry.log(events.INTENT_DETECTED, "CHAT")

            self.event_bus.emit(events.CORE_PROCESSING)

            raw_result = {

                "type": "core",

                "response": f"Procesado: {user_input}",

                "context": context

            }

        self.memory.save(user_input)

        self.event_bus.emit(events.MEMORY_UPDATED)

        self.exporter.save(
            user_input,
            raw_result
        )

        self.event_bus.emit(events.RESPONSE_GENERATED)

        self.telemetry.log(events.RESPONSE_GENERATED)

        return self._format_output(raw_result)

    # ------------------------------------------------

    def _format_output(self, result):

        if isinstance(result, dict):

            if result.get("status") == "ok":

                return (
                    "⚙️ TAREA EJECUTADA\n"
                    f"→ {result.get('task')}"
                )

            if result.get("status") == "executed":

                return (
                    "⚙️ TAREA EJECUTADA\n"
                    f"→ {result.get('task')}"
                )

            if result.get("type") == "core":

                return (
                    f"💬 {result.get('response')}"
                )

        return str(result)
