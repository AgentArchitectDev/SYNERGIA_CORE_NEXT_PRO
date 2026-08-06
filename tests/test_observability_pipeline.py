# =========================================================
# SYNERGIA CORE NEXT PRO
# STAGE 6.3.15.7.6.3
# REAL PIPELINE OBSERVABILITY TEST
# =========================================================


import sys

from pathlib import Path


# =========================================================
# PROJECT ROOT PATH
# =========================================================

ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT)
)



from datetime import datetime
import time



# =========================================================
# SYNERGIA MODULES
# =========================================================

from ai.business.business_generator import (
    create_business_project
)


from ai.runtime.live_dashboard import (
    LiveDashboard
)



print(
    "[OBSERVABILITY PIPELINE TEST LOADED]"
)



# =========================================================
# INITIALIZE DASHBOARD
# =========================================================

dashboard = LiveDashboard()



print()

print(
    "=============================="
)

print(
    "[START REAL PIPELINE TEST]"
)

print(
    "=============================="
)



start = datetime.now()


print(
    "START TIME:",
    start.isoformat()
)



# =========================================================
# REAL BUSINESS GENERATION
# =========================================================

result = create_business_project(
    "Empresa argentina de inteligencia artificial para automatizacion empresarial"
)



# =========================================================
# FINISH
# =========================================================

end = datetime.now()



print()

print(
    "=============================="
)

print(
    "[END PIPELINE]"
)

print(
    "=============================="
)



print(
    "END TIME:",
    end.isoformat()
)



# =========================================================
# LIVE DASHBOARD SNAPSHOT
# =========================================================

print()

print(
    "=============================="
)

print(
    "[FINAL DASHBOARD]"
)

print(
    "=============================="
)



dashboard.display()



# =========================================================
# RESULT
# =========================================================

print()

print(
    "=============================="
)

print(
    "[RESULT]"
)

print(
    "=============================="
)



print(
    result
)



print()

print(
    "=============================="
)

print(
    "[TEST COMPLETE]"
)

print(
    "=============================="
)
