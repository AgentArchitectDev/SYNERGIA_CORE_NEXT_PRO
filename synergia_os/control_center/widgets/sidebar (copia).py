"""
=========================================================
SYNERGIA OS
Control Center V2.0 - Core Console

Sidebar Widget

Enterprise Cognitive Operating System AI
=========================================================
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)

from PySide6.QtCore import Qt


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

        self.initialize_ui()


    def initialize_ui(self):

        self.setFixedWidth(260)

        self.setStyleSheet("""
            QWidget {
                background-color:#16181d;
            }

            QLabel {
                color:white;
                font-size:20px;
                font-weight:bold;
                padding:15px;
            }

            QPushButton {
                background-color:#20232b;
                color:white;
                border:none;
                text-align:left;
                padding:12px;
                font-size:14px;
            }

            QPushButton:hover {
                background-color:#303541;
            }

            QPushButton:pressed {
                background-color:#00C853;
            }
        """)


        layout = QVBoxLayout()

        layout.setContentsMargins(
            5,
            5,
            5,
            5
        )

        layout.setSpacing(3)


        self.setLayout(layout)


        # ---------------------------------------------
        # Logo / Titulo
        # ---------------------------------------------

        title = QLabel(
            "🧠 SYNERGIA"
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(title)


        # ---------------------------------------------
        # Menu principal
        # ---------------------------------------------

        modules = [

            "🏠 Dashboard",

            "🧠 AI Engine",

            "⚙ Kernel",

            "🔄 Runtime",

            "🧭 Cognitive Router",

            "🤖 Agents",

            "📦 Models",

            "🧠 Memory",

            "📚 Knowledge",

            "📈 Evolution",

            "📁 Projects",

            "📄 Documentation",

            "💾 Storage",

            "📤 Outputs",

            "📊 Monitor",

            "⚙ Settings"

        ]


        for module in modules:

            button = QPushButton(
                module
            )

            button.setCursor(
                Qt.PointingHandCursor
            )

            layout.addWidget(
                button
            )


        layout.addStretch()
