from ai.runtime.runtime_manager import runtime_manager
from ai.agents.agent_evolution_layer import agent_evolution_layer
from ai.core.self_improving_loop import self_improving_loop


class DashboardEvolution:

    def render_cli(self):

        print("\n==============================")
        print("SYNERGIA EVOLUTION DASHBOARD")
        print("==============================\n")

        runtime = runtime_manager.status()

        print("RUNTIME STATUS:")
        print(runtime["started"], runtime["uptime"])

        print("\nLAST RESULT:")
        print(runtime["last"])

        print("\nAGENT EVOLUTION:")
        print(agent_evolution_layer.status())

        print("\nSELF IMPROVING LOOP:")
        print(self_improving_loop.status())

        print("\n==============================")

    def snapshot(self):

        return {
            "runtime": runtime_manager.status(),
            "agents": agent_evolution_layer.status(),
            "loop": self_improving_loop.status()
        }


dashboard_evolution = DashboardEvolution()
