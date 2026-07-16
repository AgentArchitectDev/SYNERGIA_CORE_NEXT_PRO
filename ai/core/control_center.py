"""
SYNERGIA V3 - Control Center
"""

from ai.core.event_bus import event_bus
from ai.core.model_manager import model_manager
from ai.kernel.kernel import kernel


class ControlCenter:

    def snapshot(self):

        return {
            "kernel": kernel.status(),
            "models": model_manager.list_parsed(),
            "events": event_bus.get_events()[-10:]
        }


control_center = ControlCenter()
