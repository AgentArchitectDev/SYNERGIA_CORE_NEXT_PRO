import os


BASE_PATH = os.getcwd()


STRUCTURE = {

    "cognitive_kernel": [
        "kernel.py",
        "runtime_manager.py",
        "state_engine.py",
        "task_engine.py",
        "event_bus.py"
    ],

    "ai_layer": [

        "ai_engine.py",

        "orchestrator/__init__.py",
        "orchestrator/orchestrator_v8.py",
        "orchestrator/shared_memory.py",
        "orchestrator/debate_engine.py",
        "orchestrator/collab_engine.py",
        "orchestrator/context_manager.py",
        "orchestrator/execution_engine.py",
        "orchestrator/workflow_builder.py",

        "agents/__init__.py",
        "agents/agent_core.py",
        "agents/business_agent.py",
        "agents/dev_agent.py",
        "agents/cms_agent.py",
        "agents/social_agent.py",
        "agents/research_agent.py",
        "agents/automation_agent.py",

        "memory/short_term/.gitkeep",
        "memory/long_term/.gitkeep",
        "memory/experiences/.gitkeep",
    ],

    "builder_engine": [
        "backend_builder.py",
        "frontend_builder.py",
        "api_builder.py",
        "project_generator.py",
        "docker_builder.py"
    ],

    "output_engine": [
        "export_manager.py",
        "deploy_engine.py",
        "package_engine.py"
    ],

    "control_center": [
        "dashboard.py",
        "runtime_console.py",
        "agent_monitor.py",
        "live_monitor.py"
    ],

    "projects": [],

    "memory": [],

    "logs": [],

    "deploy": []
}


# ============================================
# CREATE DIRECTORY
# ============================================

def create_directory(path):

    if not os.path.exists(path):

        os.makedirs(path)

        print(f"📂 Created directory: {path}")


# ============================================
# CREATE FILE
# ============================================

def create_file(path):

    if not os.path.exists(path):

        with open(path, "w", encoding="utf-8") as file:

            file.write("")

        print(f"📄 Created file: {path}")


# ============================================
# BUILD SYSTEM
# ============================================

def build_system():

    print("\n==============================")
    print(" SYNERGIA BUILD SYSTEM v1")
    print("==============================\n")

    for folder, files in STRUCTURE.items():

        folder_path = os.path.join(BASE_PATH, folder)

        create_directory(folder_path)

        for file in files:

            file_path = os.path.join(folder_path, file)

            parent_dir = os.path.dirname(file_path)

            create_directory(parent_dir)

            create_file(file_path)

    print("\n==============================")
    print(" SYSTEM GENERATED SUCCESSFULLY")
    print("==============================\n")


# ============================================
# RUN
# ============================================

if __name__ == "__main__":

    build_system()
