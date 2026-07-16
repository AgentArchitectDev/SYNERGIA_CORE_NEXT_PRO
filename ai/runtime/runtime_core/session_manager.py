import uuid


class SessionManager:

    def __init__(self):

        self.session_id = str(uuid.uuid4())

    def new_session(self):

        self.session_id = str(uuid.uuid4())

        return self.session_id

    def current(self):

        return self.session_id


session_manager = SessionManager()
