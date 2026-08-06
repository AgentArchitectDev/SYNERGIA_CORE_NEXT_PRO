# =========================================================
# SYNERGIA OBSERVABILITY API
# STAGE 6.3.15.7.6.1
# AI RUNTIME OBSERVABILITY API LAYER
# =========================================================

from fastapi import APIRouter

from ai.runtime.live_dashboard import (
    LiveDashboard
)


print("[OBSERVABILITY API LOADED]")


router = APIRouter(
    prefix="/api/observability",
    tags=["Observability"]
)


dashboard = LiveDashboard()


# =========================================================
# SYSTEM STATUS
# =========================================================

@router.get("/status")
def system_status():

    return dashboard.generate_status()



# =========================================================
# MODEL METRICS
# =========================================================

@router.get("/models")
def model_metrics():

    return dashboard.load_model_metrics()



# =========================================================
# EXECUTION HISTORY
# =========================================================

@router.get("/history")
def execution_history():

    return dashboard.load_execution_history()



# =========================================================
# FULL DASHBOARD
# =========================================================

@router.get("/dashboard")
def full_dashboard():

    return dashboard.generate_status()
