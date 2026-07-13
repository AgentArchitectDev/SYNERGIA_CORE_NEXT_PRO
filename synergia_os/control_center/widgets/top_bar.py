from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
)

from PySide6.QtCore import Qt


class TopBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(55)

        self.setStyleSheet("""
            QWidget{
                background:#252932;
                border-bottom:1px solid #404552;
            }

            QLabel{
                color:white;
                font-size:13px;
                font-weight:bold;
            }
        """)

        layout = QHBoxLayout()

        layout.setContentsMargins(15,0,15,0)

        self.setLayout(layout)

        title = QLabel("SYNERGIA OS")

        layout.addWidget(title)

        layout.addStretch()

        layout.addWidget(QLabel("🟢 ONLINE"))

        layout.addSpacing(20)

        layout.addWidget(QLabel("USER: Gerardo"))

        layout.addSpacing(20)

        layout.addWidget(QLabel("PROJECT: CORE NEXT PRO"))
