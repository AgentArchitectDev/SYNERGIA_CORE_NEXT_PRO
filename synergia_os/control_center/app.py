"""
=========================================================

SYNERGIA OS

Control Center

V2.0 - Core Console

Enterprise Cognitive Operating System AI

=========================================================
"""

import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow


def main():

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
