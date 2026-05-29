from core.node import Node

class BusinessNode(Node):
    def run(self, context):
        print('[BUSINESS] ejecutando análisis')
        context.update('business', 'modelo SaaS definido')
        return context
