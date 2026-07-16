import time
from ai.core.event_bus import event_bus
from ai.core.scheduler import scheduler


class CognitiveLoop:
    """
    SYNERGIA COGNITIVE LOOP v1.0
    ----------------------------
    - Revisión del plan antes y después de ejecutar
    - Auto-corrección básica
    - Reintento inteligente de módulos fallidos
    - Base del "mini cerebro operativo autónomo"
    """

    def __init__(self):
        self.enabled = True
        self.iteration = 0
        self.history = []

    # ---------------------------------------------------------
    # THINK PHASE (REFLEXIÓN DEL PLAN)
    # ---------------------------------------------------------
    def think(self, input_text: str, plan: list):

        self.iteration += 1

        event_bus.emit("cognitive_think", {
            "input": input_text,
            "plan": plan,
            "iteration": self.iteration
        })

        refined_plan = list(set(plan))  # limpieza básica

        # heurística simple de corrección
        if "memory" in refined_plan and "export" in refined_plan:
            refined_plan.append("memory_sync")

        return refined_plan

    # ---------------------------------------------------------
    # EXECUTE PHASE
    # ---------------------------------------------------------
    def execute(self, input_text: str, plan: list):

        event_bus.emit("cognitive_execute_start", {
            "input": input_text,
            "plan": plan
        })

        results = scheduler.execute(input_text, plan)

        return results

    # ---------------------------------------------------------
    # REFLECT PHASE (AUTO-ANÁLISIS)
    # ---------------------------------------------------------
    def reflect(self, results: list):

        failed = [
            r for r in results
            if r.get("status") != "executed"
        ]

        event_bus.emit("cognitive_reflect", {
            "failed_modules": len(failed)
        })

        return failed

    # ---------------------------------------------------------
    # REASON LOOP (CICLO COMPLETO)
    # ---------------------------------------------------------
    def run(self, input_text: str, plan: list):

        start = time.time()

        # 1. THINK
        refined_plan = self.think(input_text, plan)

        # 2. EXECUTE
        results = self.execute(input_text, refined_plan)

        # 3. REFLECT
        failed = self.reflect(results)

        # 4. AUTO-RECOVERY SIMPLE
        if failed:
            retry_plan = [f["module"] for f in failed if "module" in f]

            if retry_plan:
                event_bus.emit("cognitive_retry", retry_plan)
                retry_results = scheduler.execute(input_text, retry_plan)

                results.extend(retry_results)

        end = time.time()

        final_state = {
            "input": input_text,
            "initial_plan": plan,
            "refined_plan": refined_plan,
            "results": results,
            "failed": failed,
            "execution_time": end - start
        }

        self.history.append(final_state)

        event_bus.emit("cognitive_loop_end", final_state)

        return final_state


# singleton global
cognitive_loop = CognitiveLoop()
