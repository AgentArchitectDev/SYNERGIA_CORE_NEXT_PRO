from core.node import Node

class DevNode(Node):
    def run(self, context):
        print('[DEV] creando arquitectura')
        context.update('dev', 'FastAPI + Docker')
        return context
