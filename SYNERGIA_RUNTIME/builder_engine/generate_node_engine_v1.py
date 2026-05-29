import os

BASE = "SYNERGIA_NODE_ENGINE_V1"

structure = {
    "core": {
        "node.py": "",
        "graph.py": "",
        "engine.py": "",
        "executor.py": "",
        "context.py": ""
    },
    "nodes": {
        "base_node.py": "",
        "business_node.py": "",
        "dev_node.py": "",
        "cms_node.py": "",
        "social_node.py": "",
        "builder_node.py": ""
    },
    "test": {
        "run_demo.py": ""
    }
}

code = {
"core/node.py": """class Node:
    def __init__(self, name):
        self.name = name
        self.next_nodes = []

    def connect(self, node):
        self.next_nodes.append(node)

    def run(self, context):
        raise NotImplementedError
""",

"core/graph.py": """class Graph:
    def __init__(self, start_node):
        self.start_node = start_node

    def run(self, context):
        current = self.start_node

        while current:
            current.run(context)
            current = current.next_nodes[0] if current.next_nodes else None

        return context
""",

"core/context.py": """class Context:
    def __init__(self, task):
        self.task = task
        self.data = {}
        self.history = []

    def update(self, key, value):
        self.data[key] = value
        self.history.append((key, value))
""",

"core/engine.py": """from core.context import Context
from core.graph import Graph

class Engine:
    def __init__(self, graph):
        self.graph = graph

    def run(self, task):
        context = Context(task)
        return self.graph.run(context)
""",

"nodes/business_node.py": """from core.node import Node

class BusinessNode(Node):
    def run(self, context):
        print('[BUSINESS] ejecutando análisis')
        context.update('business', 'modelo SaaS definido')
        return context
""",

"nodes/dev_node.py": """from core.node import Node

class DevNode(Node):
    def run(self, context):
        print('[DEV] creando arquitectura')
        context.update('dev', 'FastAPI + Docker')
        return context
""",

"test/run_demo.py": """from core.engine import Engine
from core.graph import Graph
from nodes.business_node import BusinessNode

business = BusinessNode('business')

graph = Graph(business)
engine = Engine(graph)

result = engine.run('Crear SaaS')

print(result.data)
"""
}

def create():
    for folder in structure:
        os.makedirs(f"{BASE}/{folder}", exist_ok=True)

        for file in structure[folder]:
            path = f"{BASE}/{folder}/{file}"
            with open(path, "w") as f:
                f.write(code.get(f"{folder}/{file}", ""))

    print("SYNERGIA NODE ENGINE V1 CREATED")

if __name__ == "__main__":
    create()
