from core.engine import Engine
from core.graph import Graph
from nodes.business_node import BusinessNode

business = BusinessNode('business')

graph = Graph(business)
engine = Engine(graph)

result = engine.run('Crear SaaS')

print(result.data)
