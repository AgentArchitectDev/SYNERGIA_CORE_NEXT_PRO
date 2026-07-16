import time

from ai.runtime.runtime_manager import runtime_manager
from ai.ui.dashboard_evolution import dashboard_evolution
from ai.core.self_improving_loop import self_improving_loop
from ai.cognitive.cognitive_continuous_loop import cognitive_continuous_loop


# -----------------------------
# BANNER
# -----------------------------

def banner():
    print("\n" + "=" * 65)
    print("🚀 SYNERGIA CORE NEXT_PRO")
    print("🧠 COGNITIVE OPERATING SYSTEM - PRODUCTION MODE")
    print("=" * 65 + "\n")


# -----------------------------
# BOOT SEQUENCE
# -----------------------------

def boot_system():

    print("⚙️ Booting Runtime Manager...")
    runtime_manager.start()

    print("🧠 Initializing Self Improving Layer...")
    self_improving_loop.optimize()

    print("🔁 Starting Cognitive Core...")
    cognitive_continuous_loop.step()

    print("\n✅ SYSTEM READY\n")


# -----------------------------
# DEMO EXECUTION
# -----------------------------

def run_demo():

    print("📡 Running execution demo...\n")

    inputs = [
        "memoria usuario sistema",
        "analizar inteligencia artificial",
        "exportar datos sistema",
        "consultar modelo ollama"
    ]

    for i, text in enumerate(inputs, 1):

        print(f"\n--- EXEC {i} ---")
        print("INPUT:", text)

        result = runtime_manager.execute(text)

        print("OUTPUT:")
        print(result)

        time.sleep(0.5)


# -----------------------------
# DASHBOARD SNAPSHOT
# -----------------------------

def show_dashboard():

    print("\n📊 DASHBOARD SNAPSHOT\n")
    dashboard_evolution.render_cli()


# -----------------------------
# COGNITIVE LOOP MODE
# -----------------------------

def loop_mode(iterations=3):

    print("\n🔁 COGNITIVE LOOP MODE\n")

    for i in range(iterations):

        print(f"\n=== LOOP ITERATION {i + 1} ===")

        cognitive_continuous_loop.step()

        self_improving_loop.optimize()

        dashboard_evolution.render_cli()

        time.sleep(1)


# -----------------------------
# MAIN ENTRYPOINT
# -----------------------------

if __name__ == "__main__":

    banner()

    boot_system()

    run_demo()

    show_dashboard()

    loop_mode(3)

    print("\n🏁 SYNERGIA SHUTDOWN COMPLETE\n")
