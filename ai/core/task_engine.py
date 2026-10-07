# =========================================================
#
# SYNERGIA TASK ENGINE
#
# RUNTIME MEMORY INTEGRATION
#
# STAGE 6.3.1
# AI RUNTIME EXECUTION HISTORY
#
# STAGE 6.3.15.7.4.2.3
# TASK ENGINE + PROGRESS MONITOR
#
# STAGE 6.3.15.7.5.2
# LIVE DASHBOARD INTEGRATION
#
# STAGE 6.3.15.7.6.3
# REAL PIPELINE OBSERVABILITY
#
# STAGE 6.3.15.7.7.2
# TASK ENGINE → RUNTIME MEMORY
# AUTOMATIC EXPERIENCE STORAGE
#
# STAGE 6.3.15.7.9.1
# REAL MODEL TRACKING
#
# AdaptiveModelRouter
#        ↓
# Generator
#        ↓
# TaskEngine
#        ↓
# RuntimeMemory
#        ↓
# Learning Loop
#
# =========================================================


import time



from ai.runtime.execution_history import (
    execution_history
)



from ai.runtime.progress_monitor import (
    ProgressMonitor
)



from ai.runtime.live_dashboard import (
    LiveDashboard
)



# =========================================================
# RUNTIME MEMORY
# =========================================================


from ai.memory.runtime_memory import (
    runtime_memory
)


# =========================================================
# EXECUTION SECURITY
# SECURITY-17.5
# =========================================================

from ai.security.execution_security_gate import (
    ExecutionSecurityGate
)

from ai.decision_validation.execution_envelope import (
    ExecutionEnvelope
)

from ai.decision_validation.execution_grant import (
    ExecutionGrant
)

from ai.security.last_mile_gate import (
    LastMileGate
)

from ai.security.emergency_stop import (
    emergency_stop
)

from ai.security.autonomy_off import (
    autonomy_off
)

from ai.security.master_lock import (
    master_security_lock
)

from ai.security.sovereign_escape import (
    sovereign_escape
)



print(
    "[TASK ENGINE LOADED]"
)



print(
    "[TASK ENGINE RUNTIME MEMORY ENABLED]"
)



print(
    "[TASK ENGINE REAL MODEL TRACKING ENABLED]"
)



# =========================================================
# TASK ENGINE
# =========================================================


class TaskEngine:



    def __init__(self, adaptive_router=None):


        # =========================================
        # BUSINESS TASK QUEUE
        # =========================================


        self.tasks = []



        # =========================================
        # RUNTIME COMPONENTS
        # =========================================


        self.monitor = None



        self.dashboard = LiveDashboard()

        # =========================================
        # ADAPTIVE MODEL ROUTER
        # =========================================

        self.adaptive_router = adaptive_router

        # =========================================
        # ADAPTIVE MODEL TRACKING
        # =========================================

        self.last_selected_model = None

        self.last_model_source = None

        # =========================================
        # EXECUTION SECURITY GATE
        # SECURITY-17.5
        #
        # Central execution interception point.
        # FAIL-CLOSED.
        # =========================================

        self.execution_security_gate = (
            ExecutionSecurityGate(
                emergency_stop=emergency_stop,
                autonomy_off=autonomy_off,
                master_security_lock=master_security_lock,
                sovereign_escape=sovereign_escape,
            )
        )

        self.last_mile_gate = LastMileGate(
            security_gate=self.execution_security_gate
        )

    # =====================================================
    # ADAPTIVE MODEL RESOLUTION
    #
    # STAGE 6.3.15.7.10.6
    #
    # TaskEngine -> AdaptiveModelRouter
    # =====================================================

    def resolve_model(
        self,
        task,
        requested_model=None
    ):

        if requested_model is None:
            requested_model = "AUTO"


        # =========================================
        # MANUAL MODEL
        # =========================================

        if requested_model != "AUTO":

            if self.adaptive_router:

                selected_model = (
                    self.adaptive_router.select_model(
                        task,
                        requested_model
                    )
                )

                self.last_selected_model = selected_model
                self.last_model_source = "MANUAL"
                return (
                    selected_model,
                    "MANUAL"
                )

            return (
                requested_model,
                "TASK_REQUEST"
            )


        # =========================================
        # AUTO MODEL
        # =========================================

        if self.adaptive_router:

            selected_model = (
                self.adaptive_router.select_model(
                    task
                )
            )

            if selected_model:

                self.last_selected_model = selected_model
                self.last_model_source = "ADAPTIVE_ROUTER"

                return (
                    selected_model,
                    "ADAPTIVE_ROUTER"
                )


        # =========================================
        # SAFE FALLBACK
        # =========================================

        return (
            "llama3.2:1b",
            "FALLBACK"
        )

    # =====================================================
    # ADD TASK
    # =====================================================


    def add_task(

        self,

        name,

        function,

        model=None

    ):



        if not callable(function):


            raise TypeError(

                f"Task '{name}' is not callable"

            )



        self.tasks.append(

            {

                "name":

                    name,


                "function":

                    function,


                "model":

                    model

            }

        )



        print(

            f"[TASK ADDED] {name}"

        )



    # =====================================================
    # RUN TASK QUEUE
    # =====================================================


    def run(
        self,
        execution_envelope=None,
        execution_grant=None,
    ):


        results = []



        total = len(

            self.tasks

        )



        print()



        print(

            f"[TASK ENGINE] Running {total} task(s)"

        )



        # =========================================
        # CREATE MONITOR
        # =========================================


        self.monitor = ProgressMonitor(

            total_tasks=total

        )



        self.dashboard.attach_monitor(

            self.monitor

        )



        # =========================================
        # EXECUTION LOOP
        # =========================================


        for index, task in enumerate(

            self.tasks,

            start=1

        ):



            name = task["name"]



            requested_model = task.get(

                "model",

                "AUTO"

            )



            print()



            print(

                f"[TASK {index}/{total}] {name}"

            )



            start_time = time.time()



            try:



                self.monitor.start_task(

                    name,

                    requested_model

                )



                # =====================================
                # SECURITY-17.5
                # EXECUTION SECURITY GATE
                #
                # TODA EJECUCION DE GENERATOR DEBE
                # PASAR POR ESTE GATE.
                #
                # FAIL-CLOSED:
                # si no existe autorizacion explicita,
                # la funcion NO se ejecuta.
                # =====================================

                security_decision = (
                    self.execution_security_gate.check_execution(
                        execution_name=name
                    )
                )

                print()
                print(
                    "[SECURITY-17.5] SECURITY DECISION:"
                )
                print(
                    security_decision
                )

                if not security_decision.get(
                    "authorized",
                    False
                ):

                    print()
                    print(
                        f"[SECURITY-17.5] BLOCKED: {name}"
                    )

                    duration = round(
                        time.time() - start_time,
                        2
                    )

                    result = {
                        "status": "BLOCKED",
                        "authorized": False,
                        "security": security_decision,
                        "execution": name,
                    }

                    # =================================
                    # REGISTER SECURITY BLOCK
                    # =================================

                    try:

                        execution_history.register(
                            task=name,
                            node="MAQ2",
                            result="SECURITY_BLOCKED",
                            model=requested_model,
                        )

                    except Exception:

                        pass

                    # =================================
                    # SECURITY-17.5.5
                    # RUNTIME MEMORY SECURITY EVENT
                    #
                    # IMPORTANTE:
                    # SECURITY_BLOCKED NO ES FAILED.
                    #
                    # El Gate impidio la ejecucion
                    # antes de llamar a la funcion.
                    # =================================

                    try:

                        runtime_memory.add_experience(

                            task=name,

                            model=requested_model,

                            status="SECURITY_BLOCKED",

                            duration_seconds=duration,

                            metadata={

                                "security":
                                    True,

                                "security_status":
                                    "BLOCKED",

                                "security_reason":
                                    security_decision.get(
                                        "reason"
                                    ),

                                "authorized":
                                    security_decision.get(
                                        "authorized",
                                        False
                                    ),

                                "execution":
                                    name,

                                "requested_model":
                                    requested_model,

                                "stage":
                                    "6.3.15.7.9.1",

                                "security_blocked_memory":
                                    True,
                            }
                        )

                    except Exception as memory_error:

                        print()

                        print(
                            "[SECURITY-17.5.5] "
                            "RUNTIME MEMORY ERROR:"
                        )

                        print(
                            memory_error
                        )

                    continue

                # =====================================
                # EXECUTE GENERATOR
                # SECURITY-17.5 AUTHORIZED
                # =====================================

                print()
                print(
                    f"[SECURITY-17.5] SECURITY CONTROLS ALLOWED: {name}"
                )

                # =====================================
                # SECURITY-17.5 / LAST MILE ENFORCEMENT
                #
                # Formal execution requires:
                # ExecutionEnvelope + ExecutionGrant
                # + LastMileGate == EXECUTABLE.
                #
                # No authorization is fabricated here.
                # Missing formal authorization FAILS CLOSED.
                # =====================================

                if not isinstance(
                    execution_envelope,
                    ExecutionEnvelope
                ):

                    last_mile_decision = {
                        "status": "BLOCKED",
                        "execution": name,
                        "authorized": False,
                        "fail_closed": True,
                        "reason": "EXECUTION_ENVELOPE_MISSING_OR_INVALID",
                        "runtime_execution": False,
                    }

                elif not isinstance(
                    execution_grant,
                    ExecutionGrant
                ):

                    last_mile_decision = {
                        "status": "BLOCKED",
                        "execution": name,
                        "authorized": False,
                        "fail_closed": True,
                        "reason": "EXECUTION_GRANT_MISSING_OR_INVALID",
                        "runtime_execution": False,
                    }

                else:

                    last_mile_decision = self.last_mile_gate.check(
                        envelope=execution_envelope,
                        execution_name=name,
                        requested_scope=name,
                        grant=execution_grant,
                    )

                print()
                print(
                    "[SECURITY-17.5] LAST MILE DECISION:"
                )
                print(
                    last_mile_decision
                )

                if last_mile_decision.get("status") != "EXECUTABLE":

                    print()
                    print(
                        f"[SECURITY-17.5] LAST MILE BLOCKED: {name}"
                    )

                    results.append({
                        "status": "BLOCKED",
                        "authorized": False,
                        "security": security_decision,
                        "last_mile": last_mile_decision,
                        "execution": name,
                    })

                    continue

                # =====================================
                # ADAPTIVE MODEL RESOLUTION
                #
                # STAGE 6.3.15.7.10.16
                #
                # SECURITY AUTHORIZED
                #        ↓
                # MODEL RESOLUTION
                #        ↓
                # GENERATOR EXECUTION
                # =====================================

                resolved_model, resolved_source = (
                    self.resolve_model(
                        name,
                        requested_model
                    )
                )

                if isinstance(
                    resolved_model,
                    dict
                ):

                    execution_model = resolved_model.get(
                        "model",
                        "llama3.2:1b"
                    )

                else:

                    execution_model = resolved_model

                print(
                    f"[TASK ENGINE MODEL] {execution_model}"
                )

                print(
                    f"[TASK ENGINE SOURCE] {resolved_source}"
                )

                # =====================================
                # PROPAGATE EXECUTION MODEL
                #
                # STAGE 6.3.15.7.10.17
                #
                # TaskEngine is the authoritative
                # model resolution point.
                # =====================================

                result = (

                    task["function"](
                        execution_model
                    )

                )



                duration = round(

                    time.time() - start_time,

                    2

                )



                # =====================================
                # REAL MODEL TRACKING
                #
                # STAGE 6.3.15.7.9.1
                #
                # Capture the model returned
                # by generators
                # =====================================


                real_model = requested_model



                model_source = "TASK_DEFAULT"



                if isinstance(result, dict):


                    real_model = result.get(

                        "model",

                        requested_model

                    )



                    if "model" in result:


                        model_source = (

                            "GENERATOR_OUTPUT"

                        )



                self.monitor.complete_task(

                    name

                )



                # =====================================
                # EXECUTION HISTORY
                # =====================================


                execution_history.register(

                    task=name,

                    node="MAQ2",

                    result="completed",
                    model=real_model,

                )



                # =====================================
                # RUNTIME EXPERIENCE MEMORY
                #
                # REAL MODEL STORAGE
                # =====================================


                runtime_memory.add_experience(

                    task=name,

                    model=real_model,

                    status="SUCCESS",

                    duration_seconds=duration,

                    metadata={

                        "result_type":

                            type(result).__name__,


                        "requested_model":

                            requested_model,


                        "real_model":

                            real_model,


                        "model_source":

                            model_source,


                        "stage":

                            "6.3.15.7.9.1"

                    }

                )
                results.append(

                    {

                        "name":

                            name,


                        "status":

                            "success",


                        "result":

                            result,


                        "model":

                            real_model,


                        "duration_seconds":

                            duration,


                        "security":

                            security_decision,


                        "last_mile":

                            last_mile_decision

                    }

                )



                print(

                    f"[TASK OK] {name}"

                )



                print(

                    f"[REAL MODEL] {real_model}"

                )



            except Exception as e:



                duration = round(

                    time.time() - start_time,

                    2

                )



                # =====================================
                # FAILED EXECUTION HISTORY
                # =====================================


                execution_history.register(

                    task=name,

                    node="MAQ2",

                    result="failed",
                    model=requested_model,

                )



                # =====================================
                # FAILED EXPERIENCE MEMORY
                # =====================================


                runtime_memory.add_experience(

                    task=name,

                    model=requested_model,

                    status="FAILED",

                    duration_seconds=duration,

                    metadata={

                        "error":

                            str(e),


                        "requested_model":

                            requested_model,


                        "stage":

                            "6.3.15.7.9.1"

                    }

                )



                results.append(

                    {

                        "name":

                            name,


                        "status":

                            "error",


                        "error":

                            str(e),


                        "model":

                            requested_model,


                        "duration_seconds":

                            duration

                    }

                )



                print(

                    f"[TASK ERROR] {name}"

                )



                print(

                    str(e)

                )



        # =========================================
        # EXECUTION SUMMARY
        # =========================================


        successful = sum(

            1

            for item in results

            if item["status"] == "success"

        )



        failed = total - successful



        summary = {


            "total":

                total,


            "successful":

                successful,


            "failed":

                failed,


            "results":

                results,


            "monitor":

                self.monitor.status()

                if self.monitor

                else {},



            "memory":

                runtime_memory.status()

        }



        print()



        print(

            "[TASK ENGINE FINISHED]"

        )



        print(

            f"SUCCESS: {successful}"

        )



        print(

            f"FAILED: {failed}"

        )



        print()



        print(

            "[RUNTIME MEMORY STATUS]"

        )



        print(

            runtime_memory.status()

        )



        return summary



    # =====================================================
    # MODERN EXECUTION API
    # =====================================================


    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        return {
            "tasks": len(self.tasks),
            "adaptive_router": self.adaptive_router is not None,
            "last_selected_model": self.last_selected_model,
            "last_model_source": self.last_model_source
        }


    # =====================================================
    # ROUTER STATUS
    # =====================================================

    def get_router_status(self):

        if self.adaptive_router is None:

            return {
                "enabled": False
            }

        return {
            "enabled": True,
            "status": self.adaptive_router.status()
        }


    def execute(

        self,

        user_input,

        context=None

    ):



        text = user_input.lower()



        if "calcular" in text:



            return {


                "type":

                    "calculator",


                "message":

                    "Calculation request detected"

            }



        return {


            "type":

                "general",


            "input":

                user_input,


            "context":

                context

        }
