"""
============================================================
SYNERGIA COGNITIVE LOOP ENGINE
Self-improving execution cycle
============================================================
"""

import time
from ai.core.router import router
from ai.core.scheduler import scheduler
from ai.runtime.runtime_state import runtime_state
from ai.runtime.event_bus import event_bus


class CognitiveLoop:

    def __init__(self):

        self.max_iterations = 3
        self.last_trace = []

    # -------------------------------------------------
    # MAIN LOOP ENTRYPOINT
    # -------------------------------------------------

    def run(self, input_text: str, context=None):

        event_bus.emit("cognitive_loop_start", input_text)

        iteration = 0
        current_input = input_text
        final_result = None

        trace = []

        # -------------------------------------------------
        # LOOP CORE
        # -------------------------------------------------

        while iteration < self.max_iterations:

            iteration += 1

            # 1. PLAN
            plan = router.route(current_input)

            event_bus.emit("loop_plan", {
                "iteration": iteration,
                "plan": plan
            })

            # 2. EXECUTE
            result = scheduler.execute(current_input, plan, context)

            # 3. EVALUATE (simple heuristic)
            evaluation = self._evaluate(result)

            trace.append({
                "iteration": iteration,
                "input": current_input,
                "plan": plan,
                "result": result,
                "evaluation": evaluation
            })

            # 4. DECISION

            if evaluation["status"] == "success":
                final_result = result
                break

            # 5. REPLAN (refinement step)
            current_input = self._refine_input(current_input, evaluation)

        # -------------------------------------------------
        # FINALIZATION
        # -------------------------------------------------

        self.last_trace = trace

        runtime_state.set("last_cognitive_trace", trace)

        event_bus.emit("cognitive_loop_end", {
            "iterations": iteration,
            "success": final_result is not None
        })

        return {
            "input": input_text,
            "iterations": iteration,
            "trace": trace,
            "final_result": final_result
        }

    # -------------------------------------------------
    # SIMPLE EVALUATION ENGINE
    # -------------------------------------------------

    def _evaluate(self, result):

        # check if any module failed
        failed = False

        if isinstance(result, list):

            for r in result:
                if r.get("status") in ["error", "missing"]:
                    failed = True

        else:
            failed = True

        if failed:
            return {
                "status": "retry",
                "reason": "execution_errors_detected"
            }

        return {
            "status": "success"
        }

    # -------------------------------------------------
    # INPUT REFINEMENT LOGIC
    # -------------------------------------------------

    def _refine_input(self, input_text, evaluation):

        return input_text + " (refinado por fallo previo)"


# SINGLETON
cognitive_loop = CognitiveLoop()
