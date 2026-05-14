import sys
import os

print(">>> SYNERGIA BOOT SEQUENCE")

# =========================
# FIX PATH AUTOMATICO
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# =========================
# CHECK DEPENDENCIES
# =========================
def check_import(name):
    try:
        __import__(name)
        print(f"[OK] {name}")
    except Exception as e:
        print(f"[FAIL] {name} -> {e}")
        return False
    return True

checks = [
    "ai.ui.ai_lab_panel",
    "ai.memory.memory_manager",
    "ai.providers.ollama_connector"
]

for c in checks:
    check_import(c)

# =========================
# START UI
# =========================
from PyQt6.QtWidgets import QApplication
from ai.ui.ai_lab_panel import AILabPanel

app = QApplication(sys.argv)
window = AILabPanel()
window.show()

print(">>> SYNERGIA RUNNING")

sys.exit(app.exec())
