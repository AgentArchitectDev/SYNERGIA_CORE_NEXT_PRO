"""
dashboard_controller.py
-----------------------------------------
SYNERGIA Dashboard Controller

Coordina:

- Brain Panel
- Output Panel
- System Monitor

No dibuja nada.

Solo decide qué debe mostrar cada panel.
"""

import time


class DashboardController:

    def __init__(
        self,
        brain_panel,
        output_panel,
        system_monitor,
        orchestrator,
    ):

        self.brain = brain_panel
        self.output = output_panel
        self.monitor = system_monitor
        self.orchestrator = orchestrator

        self.memory = []

    # ------------------------------------------------

    def execute(self, user_input):

        start = time.time()

        self.memory.append(user_input)

        self.brain.clear()

        self.brain.add("🧠 INPUT RECEIVED")

        context = {
            "intent": self.detect_intent(user_input),
            "engine": "",
            "steps": []
        }

        if context["intent"] == "TASK":

            context["engine"] = "TASK ENGINE"

            context["steps"] = [

                "📦 MEMORY",

                "🔍 TASK DETECTED",

                "⚙ TASK ENGINE",

                "📤 EXPORT",

                "✅ FINISHED"

            ]

        else:

            context["engine"] = "CORE ENGINE"

            context["steps"] = [

                "📦 MEMORY",

                "💬 CHAT REQUEST",

                "🧠 CORE ENGINE",

                "📤 RESPONSE",

                "✅ FINISHED"

            ]

        for step in context["steps"]:
            self.brain.add(step)

        result = self.orchestrator.handle(user_input)

        self.output.show_result(result)

        elapsed = f"{time.time()-start:.3f} s"

        self.monitor.update(

            memory_size=len(self.memory),

            last_command=user_input,

            last_task=user_input,

            last_module=context["engine"],

            execution_time=elapsed,

            ai_provider="LOCAL",

            ai_model="SYNERGIA CORE"

        )

        return result

    # ------------------------------------------------

    def detect_intent(self, text):

        text = text.lower()

        keywords = [

            "hacer",

            "crear",

            "generar",

            "ejecutar",

            "buscar",

            "guardar"

        ]

        for word in keywords:

            if word in text:

                return "TASK"

        return "CHAT"
