import time


class Scheduler:

    """
    SYNERGIA Scheduler V4
    """

    def __init__(self):

        self.modules = {}

        self.executions = 0

        self.errors = 0

        self.history = []

        self.last_execution = None

    # ----------------------------------

    def register(self, name, module):

        self.modules[name] = module

    # ----------------------------------

    def execute(self, input_text, plan):

        start = time.time()

        results = []

        self.executions += 1

        self.last_execution = time.time()

        for module_name in plan:

            module = self.modules.get(module_name)

            if module is None:

                self.errors += 1

                results.append({

                    "module": module_name,

                    "status": "missing"

                })

                continue

            try:

                if hasattr(module, "execute"):

                    output = module.execute(input_text)

                elif hasattr(module, "run"):

                    output = module.run(input_text)

                else:

                    raise Exception(
                        "Module not executable"
                    )

                results.append({

                    "module": module_name,

                    "status": "executed",

                    "result": output

                })

            except Exception as e:

                self.errors += 1

                results.append({

                    "module": module_name,

                    "status": "error",

                    "error": str(e)

                })

        latency = round(
            time.time() - start,
            4
        )

        execution_record = {

            "timestamp": self.last_execution,

            "latency": latency,

            "plan": plan,

            "results": results

        }

        self.history.append(
            execution_record
        )

        return results

    # ----------------------------------

    def get_last_execution(self):

        if not self.history:
            return None

        return self.history[-1]

    # ----------------------------------

    def statistics(self):

        return {

            "executions": self.executions,

            "errors": self.errors,

            "history_size": len(
                self.history
            )

        }

    # ----------------------------------

    def status(self):

        return {

            "modules": list(
                self.modules.keys()
            ),

            "count": len(
                self.modules
            ),

            "executions": self.executions,

            "errors": self.errors

        }


scheduler = Scheduler()
