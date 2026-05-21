# =========================================================
# FILE:
# run_synergia.py
# =========================================================

import sys

from PyQt6.QtWidgets import (
    QApplication
)

print(
    ">>> SYNERGIA BOOT SEQUENCE"
)

# =========================================================
# IMPORT TEST
# =========================================================

modules = [

    "ai.ui.ai_lab_panel",

    "ai.memory.memory_manager",

    "ai.providers.ollama_connector"
]

for module in modules:

    try:

        __import__(module)

        print(f"[OK] {module}")

    except Exception as e:

        print(f"[FAIL] {module} -> {e}")

# =========================================================
# MAIN IMPORT
# =========================================================

from ai.ui.ai_lab_panel import (
    AILabPanel
)

# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    print(
        ">>> SYNERGIA RUNNING"
    )

    app = QApplication(sys.argv)

    window = AILabPanel()

    window.show()

    sys.exit(app.exec())
