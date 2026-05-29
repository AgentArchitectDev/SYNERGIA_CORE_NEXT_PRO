import os


# ============================================
# BASE PATH
# ============================================

BASE_PATH = os.getcwd()


# ============================================
# STACK DETECTOR
# ============================================

def detect_stack(task):

    task = task.lower()

    stack = {

        "backend": "FastAPI",
        "frontend": "React",
        "database": "MongoDB",
        "container": "Docker"
    }

    if "crm" in task:

        stack["type"] = "CRM SYSTEM"

    elif "saas" in task:

        stack["type"] = "SAAS PLATFORM"

    elif "ecommerce" in task:

        stack["type"] = "ECOMMERCE"

    else:

        stack["type"] = "GENERAL SYSTEM"

    return stack


# ============================================
# AGENT SELECTOR
# ============================================

def select_agents(task):

    agents = []

    task = task.lower()

    if "crm" in task or "saas" in task:

        agents.append("business")

    if "backend" in task or "api" in task or "crm" in task:

        agents.append("dev")

    if "dashboard" in task or "frontend" in task:

        agents.append("cms")

    agents.append("social")

    return agents


# ============================================
# CREATE DIRECTORY
# ============================================

def create_directory(path):

    if not os.path.exists(path):

        os.makedirs(path)

        print(f"📂 Created: {path}")


# ============================================
# CREATE FILE
# ============================================

def create_file(path, content=""):

    with open(path, "w", encoding="utf-8") as file:

        file.write(content)

    print(f"📄 Created: {path}")


# ============================================
# GENERATE BACKEND
# ============================================

def generate_backend():

    return '''
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():

    return {"status": "SYNERGIA BACKEND ACTIVE"}
'''


# ============================================
# GENERATE FRONTEND
# ============================================

def generate_frontend():

    return '''
function App() {

    return (

        <h1>SYNERGIA FRONTEND ACTIVE</h1>

    );
}

export default App;
'''


# ============================================
# GENERATE README
# ============================================

def generate_readme(task, stack, agents):

    return f'''
# SYNERGIA AUTONOMOUS PROJECT

## TASK

{task}

## STACK

{stack}

## AGENTS

{agents}

Generated automatically by SYNERGIA
'''


# ============================================
# BUILD PROJECT
# ============================================

def build_project(task):

    print("\n==============================")
    print(" SYNERGIA AUTONOMOUS BUILDER")
    print("==============================\n")

    stack = detect_stack(task)

    agents = select_agents(task)

    print(f"🧠 TASK:\n{task}\n")

    print(f"⚙️ STACK:\n{stack}\n")

    print(f"🤖 AGENTS:\n{agents}\n")

    project_name = task.lower().replace(" ", "_")

    project_path = os.path.join(
        BASE_PATH,
        "projects",
        project_name
    )

    # ----------------------------------------

    folders = [

        "backend",
        "frontend",
        "database",
        "docker",
        "docs"
    ]

    create_directory(project_path)

    for folder in folders:

        create_directory(
            os.path.join(project_path, folder)
        )

    # ----------------------------------------

    create_file(

        os.path.join(
            project_path,
            "backend",
            "main.py"
        ),

        generate_backend()
    )

    # ----------------------------------------

    create_file(

        os.path.join(
            project_path,
            "frontend",
            "App.jsx"
        ),

        generate_frontend()
    )

    # ----------------------------------------

    create_file(

        os.path.join(
            project_path,
            "README.md"
        ),

        generate_readme(
            task,
            stack,
            agents
        )
    )

    print("\n==============================")
    print(" AUTONOMOUS BUILD COMPLETE")
    print("==============================\n")

    print(f"🚀 PATH:\n{project_path}")


# ============================================
# RUN
# ============================================

if __name__ == "__main__":

    build_project(
        "Crear CRM IA para inmobiliarias"
    )
