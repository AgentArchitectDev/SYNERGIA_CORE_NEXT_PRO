from ai.core.module_registry import module_registry


class Scheduler:

    def execute(self, input_text: str, modules: list = None):

        if modules is None:
            return []

        results = []

        for module_name in modules:

            module = module_registry.get(module_name)

            if module is None:
                results.append({
                    "module": module_name,
                    "status": "not_found"
                })
                continue

            # ejecución real del módulo
            result = module.execute(input_text)

            results.append(result)

        return results


scheduler = Scheduler()
