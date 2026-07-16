class EventBus:

    def __init__(self):

        self.events = []

    def emit(self, name, data=None):

        self.events.append({

            "event": name,

            "data": data

        })

    def history(self):

        return self.events


event_bus = EventBus()
