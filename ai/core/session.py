import time
from ai.core.event_bus import event_bus


class SessionManager:
    """
    SYNERGIA SESSION ENGINE
    -----------------------
    - Maneja sesiones de usuario/runtime
    """

    def __init__(self):
        self.sessions = {}
        self.active_session = None

    def start_session(self, session_id="default"):

        self.active_session = session_id

        if session_id not in self.sessions:
            self.sessions[session_id] = {
                "created_at": time.time(),
                "history": []
            }

        event_bus.emit("session_started", session_id)

        return self.sessions[session_id]

    def add_event(self, event):

        if not self.active_session:
            self.start_session()

        self.sessions[self.active_session]["history"].append({
            "event": event,
            "timestamp": time.time()
        })

    def get_session(self, session_id=None):

        session_id = session_id or self.active_session
        return self.sessions.get(session_id, None)


# singleton
session_manager = SessionManager()
