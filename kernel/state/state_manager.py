import json
from pathlib import Path


class StateManager:

    STATE_FILE = Path("runtime/sessions/system_state.json")

    @classmethod
    def load_state(cls):

        if not cls.STATE_FILE.exists():

            default_state = {
                "current_mode": "DEV",
                "current_maq": "MAQ2",
                "active_model": "qwen2.5-coder",
                "active_project": "SYNERGIA_CORE_NEXT_PRO"
            }

            cls.save_state(default_state)

            return default_state

        with open(cls.STATE_FILE, "r") as f:
            return json.load(f)

    @classmethod
    def save_state(cls, data):

        cls.STATE_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(cls.STATE_FILE, "w") as f:
            json.dump(data, f, indent=4)
