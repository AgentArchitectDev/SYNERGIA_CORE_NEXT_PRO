from ai.runtime.runtime_manager import runtime_manager


class Dashboard:

    def render_cli(self):

        print("\n====================")
        print("SYNERGIA DASHBOARD")
        print("====================\n")

        status = runtime_manager.status()

        print("Runtime:")
        print(status)

        print("\nLast execution:")
        print(runtime_manager.last_result)

        print("\n====================")

    def snapshot(self):

        return {
            "runtime": runtime_manager.status(),
            "last": runtime_manager.last_result
        }


dashboard = Dashboard()
