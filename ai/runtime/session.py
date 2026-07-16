"""
============================================================
SYNERGIA COGNITIVE OS
Session Manager
Version 4.0
============================================================
"""

import uuid
from datetime import datetime


class Session:
    """
    Representa una sesión activa del sistema.

    Una sesión contiene:
    - identidad
    - contexto de ejecución
    - historial de acciones
    - estado runtime asociado
    """

    def __init__(self, user_id="anonymous"):

        self.session_id = str(uuid.uuid4())

        self.user_id = user_id

        self.created = datetime.now().isoformat()

        self.last_active = self.created

        self.active = True

        self.data = {}

        self.events = []

    # -------------------------------------------------

    def touch(self):

        self.last_active = datetime.now().isoformat()

    # -------------------------------------------------

    def set(self, key, value):

        self.data[key] = value

        self.events.append({
            "event": "set",
            "key": key,
            "value": value,
            "timestamp": datetime.now().isoformat()
        })

        self.touch()

    # -------------------------------------------------

    def get(self, key, default=None):

        self.touch()

        return self.data.get(key, default)

    # -------------------------------------------------

    def log_event(self, event_name, payload=None):

        self.events.append({
            "event": event_name,
            "data": payload,
            "timestamp": datetime.now().isoformat()
        })

        self.touch()

    # -------------------------------------------------

    def close(self):

        self.active = False

        self.log_event("session_closed")

    # -------------------------------------------------

    def summary(self):

        return {
            "session_id": self.session_id,
            "user_id": self.user_id,
            "active": self.active,
            "created": self.created,
            "last_active": self.last_active,
            "events": len(self.events)
        }


class SessionManager:
    """
    Administra múltiples sesiones del sistema.
    """

    def __init__(self):

        self.sessions = {}

    # -------------------------------------------------

    def create_session(self, user_id="anonymous"):

        session = Session(user_id)

        self.sessions[session.session_id] = session

        return session

    # -------------------------------------------------

    def get_session(self, session_id):

        return self.sessions.get(session_id)

    # -------------------------------------------------

    def close_session(self, session_id):

        session = self.sessions.get(session_id)

        if session:

            session.close()

        return session

    # -------------------------------------------------

    def active_sessions(self):

        return [
            s.summary()
            for s in self.sessions.values()
            if s.active
        ]

    # -------------------------------------------------

    def dump(self):

        return {
            "total": len(self.sessions),
            "active": len(self.active_sessions()),
            "sessions": [
                s.summary()
                for s in self.sessions.values()
            ]
        }


session_manager = SessionManager()
