# =========================================================
# SYNERGIA CORE NEXT PRO
# STATE MANAGER
# =========================================================

import json

from pathlib import Path


class StateManager:

    # =====================================================
    # STATE FILE
    # =====================================================

    STATE_FILE = Path("runtime/sessions/system_state.json")

    # =====================================================
    # LOAD STATE
    # =====================================================

    @classmethod
    def load_state(cls):

        if not cls.STATE_FILE.exists():

            default_state = {

                "system_name": "SYNERGIA_CORE_NEXT_PRO",

                "current_mode": "DEV",

                "current_maq": "MAQ2",

                "active_model": "qwen2.5-coder",

                "active_project": "SYNERGIA_CORE_NEXT_PRO",

                "runtime_status": "ONLINE",

                "kernel_status": "ACTIVE",

                "active_agents": [],

                "last_boot": None
            }

            cls.save_state(default_state)

            return default_state

        with open(cls.STATE_FILE, "r") as f:

            return json.load(f)

    # =====================================================
    # SAVE STATE
    # =====================================================

    @classmethod
    def save_state(cls, data):

        cls.STATE_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(cls.STATE_FILE, "w") as f:

            json.dump(
                data,
                f,
                indent=4
            )

    # =====================================================
    # UPDATE STATE
    # =====================================================

    @classmethod
    def update(cls, key, value):

        state = cls.load_state()

        state[key] = value

        cls.save_state(state)

    # =====================================================
    # GET VALUE
    # =====================================================

    @classmethod
    def get(cls, key):

        state = cls.load_state()

        return state.get(key)

    # =====================================================
    # SHOW STATE
    # =====================================================

    @classmethod
    def show(cls):

        state = cls.load_state()

        print("\n========================================")
        print("🧠 SYNERGIA STATE ENGINE")
        print("========================================\n")

        for key, value in state.items():

            print(f"{key} => {value}")

        print("\n========================================")
