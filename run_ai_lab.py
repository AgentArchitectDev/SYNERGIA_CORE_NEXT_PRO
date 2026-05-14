import sys
from PyQt6.QtWidgets import QApplication

print(">>> SYNERGIA STARTING")

from ai.ui.ai_lab_panel import AILabPanel

print(">>> IMPORT OK")

if __name__ == "__main__":
    print(">>> ENTER MAIN")
    app = QApplication(sys.argv)

    window = AILabPanel()
    window.show()

    print(">>> WINDOW CREATED")

    sys.exit(app.exec())
