import os

BASE = "visual_os_v2"

structure = {
    "core": ["visual_engine.py", "node_mapper.py", "bridge.py"],
    "canvas": ["graph_view.py", "node_ui.py"],
    "components": ["sidebar.py", "toolbar.py"],
    "modes": ["autonomous.py", "hybrid.py", "manual.py"],
    "assets": ["styles.css"]
}

code = {
    "app.py": """import streamlit as st

st.set_page_config(page_title='SYNERGIA VISUAL OS v2')

st.title('🧠 SYNERGIA VISUAL OS v2')

mode = st.selectbox('Select Mode', ['AUTONOMOUS', 'HYBRID', 'MANUAL'])

task = st.text_input('Enter your request')

if st.button('Execute'):
    st.success('Execution completed')
    st.json({
        'status': 'RUNNING',
        'mode': mode,
        'task': task
    })
""",

    "core/visual_engine.py": """class VisualEngine:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def execute(self, context):
        for node in self.nodes:
            node.run(context)
        return context
""",

    "core/node_mapper.py": """class NodeMapper:
    def map_task(self, task):
        if 'business' in task:
            return ['business']
        if 'dev' in task:
            return ['dev']
        return ['business', 'dev']
""",

    "core/bridge.py": """class SynergiaBridge:
    def run(self, task):
        return {
            'status': 'OK',
            'task': task,
            'engine': 'Node Engine v1'
        }
"""
}

def create():
    # 🔥 CREAR BASE
    os.makedirs(BASE, exist_ok=True)

    # 🔥 CREAR SUBCARPETAS PRIMERO
    for folder in structure:
        os.makedirs(os.path.join(BASE, folder), exist_ok=True)

    # 🔥 CREAR ARCHIVOS CON SEGURIDAD
    for file, content in code.items():
        full_path = os.path.join(BASE, file)

        folder = os.path.dirname(full_path)
        os.makedirs(folder, exist_ok=True)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    print("✅ VISUAL OS v2 CREATED SUCCESSFULLY")


if __name__ == "__main__":
    create()
