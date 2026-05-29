# =========================================================
# SYNERGIA OS v3
# LIVE AGENT COMMUNICATION BUS
# =========================================================

from datetime import datetime


# =========================================================
# LIVE AGENT BUS
# =========================================================

class LiveAgentBus:

    def __init__(self):

        self.events = []

        self.channels = {}

        print("🧠 LIVE AGENT BUS ONLINE")

    # =====================================================
    # REGISTER AGENT
    # =====================================================

    def register(self, agent_name):

        if agent_name not in self.channels:

            self.channels[agent_name] = []

            print(f"✅ AGENT REGISTERED -> {agent_name}")

    # =====================================================
    # SEND EVENT
    # =====================================================

    def send_event(
        self,
        sender,
        target,
        event_type,
        content
    ):

        event = {

            "timestamp": str(datetime.now()),
            "sender": sender,
            "target": target,
            "type": event_type,
            "content": content
        }

        self.events.append(event)

        if target in self.channels:

            self.channels[target].append(event)

        print(
            f"📡 EVENT -> "
            f"{sender} -> {target} "
            f"({event_type})"
        )

    # =====================================================
    # GET EVENTS
    # =====================================================

    def get_events(self, agent_name):

        return self.channels.get(agent_name, [])

    # =====================================================
    # GET ALL EVENTS
    # =====================================================

    def get_all_events(self):

        return self.events
