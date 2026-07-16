"""
============================================================
SYNERGIA RUNTIME EVENT BUS
OS-level event system
============================================================
"""


class EventBus:

    def __init__(self):

        self.events = []

    # -------------------------------------------------

    def emit(self, event_name, data=None):

        event = {
            "event": event_name,
            "data": data
        }

        self.events.append(event)

        return event

    # -------------------------------------------------

    def get_events(self):

        return self.events

    # -------------------------------------------------

    def clear(self):

        self.events = []


event_bus = EventBus()
