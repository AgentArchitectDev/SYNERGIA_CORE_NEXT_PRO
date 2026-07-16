"""
SYNERGIA V3 - Event Bus (REAL)
"""

class EventBus:

    def __init__(self):
        self.events = []

    def emit(self, name, data=None):

        event = {
            "event": name,
            "data": data
        }

        self.events.append(event)

        return event

    def get_events(self):

        return self.events


event_bus = EventBus()
