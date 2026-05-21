# =========================================================
# SYNERGIA CORE NEXT PRO
# MODEL SERVICE
# =========================================================

from kernel.state.state_manager import StateManager


class ModelService:

    # =====================================================
    # SET MODEL
    # =====================================================

    @classmethod
    def set_model(cls, model_name):

        StateManager.update(
            "active_model",
            model_name
        )

        print(f"\n[MODEL SERVICE] Active model => {model_name}")

    # =====================================================
    # GET MODEL
    # =====================================================

    @classmethod
    def get_model(cls):

        return StateManager.get(
            "active_model"
        )

    # =====================================================
    # SHOW MODEL
    # =====================================================

    @classmethod
    def show(cls):

        model = cls.get_model()

        print("\n========================================")
        print("🤖 ACTIVE AI MODEL")
        print("========================================")
        print(f"\nMODEL => {model}")
        print("\n========================================")
