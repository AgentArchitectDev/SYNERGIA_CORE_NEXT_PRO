"""
=========================================================
SYNERGIA OS
Control Center V2.0 - Core Console

AI Engine Module

Enterprise Cognitive Operating System AI
=========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFrame
)


from PySide6.QtCore import Qt



class AIEnginePage(QWidget):


    def __init__(self):

        super().__init__()

        self.setup_ui()



    def setup_ui(self):


        layout = QVBoxLayout()


        layout.setAlignment(
            Qt.AlignCenter
        )


        self.setLayout(
            layout
        )


        title = QLabel(
            "🧠 AI ENGINE"
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        title.setStyleSheet("""

            font-size:36px;

            font-weight:bold;

            color:white;

        """)



        description = QLabel(
            "SYNERGIA Artificial Intelligence Core"
        )


        description.setAlignment(
            Qt.AlignCenter
        )


        description.setStyleSheet("""

            font-size:18px;

            color:#BFBFBF;

        """)



        panel = QFrame()


        panel.setStyleSheet("""

            QFrame {

                background:#20232b;

                border-radius:10px;

                padding:20px;

            }

        """)


        panel_layout = QVBoxLayout()


        panel.setLayout(
            panel_layout
        )


        items = [

            "Model Manager",

            "AI Providers",

            "Ollama Interface",

            "OpenAI Interface",

            "Gemini Interface",

            "Local Models"

        ]


        for item in items:

            label = QLabel(
                "● " + item
            )

            label.setStyleSheet("""

                color:white;

                font-size:16px;

                padding:8px;

            """)


            panel_layout.addWidget(
                label
            )



        layout.addWidget(
            title
        )


        layout.addWidget(
            description
        )


        layout.addSpacing(
            30
        )


        layout.addWidget(
            panel
        )
