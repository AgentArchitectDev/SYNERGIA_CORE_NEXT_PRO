"""
=========================================================
SYNERGIA OS
Control Center V2.0 - Core Console

Agents Module V1.0

Cognitive Agent Management Layer

Enterprise Cognitive Operating System AI
=========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QScrollArea
)


from PySide6.QtCore import Qt




class AgentsPage(QWidget):


    def __init__(self):

        super().__init__()

        self.setup_ui()



    # =====================================================
    # MAIN UI
    # =====================================================


    def setup_ui(self):


        main_layout = QVBoxLayout()


        self.setLayout(
            main_layout
        )


        scroll = QScrollArea()


        scroll.setWidgetResizable(
            True
        )


        scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )



        container = QWidget()


        layout = QVBoxLayout()


        layout.setContentsMargins(
            30,
            30,
            30,
            30
        )


        layout.setSpacing(
            20
        )


        container.setLayout(
            layout
        )


        scroll.setWidget(
            container
        )


        main_layout.addWidget(
            scroll
        )



        # =================================================
        # TITLE
        # =================================================


        title = QLabel(
            "🤖 SYNERGIA AGENTS"
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        title.setStyleSheet("""

            color:white;

            font-size:40px;

            font-weight:bold;

        """)


        layout.addWidget(
            title
        )



        subtitle = QLabel(
            "Cognitive Agent Management System"
        )


        subtitle.setAlignment(
            Qt.AlignCenter
        )


        subtitle.setStyleSheet("""

            color:#BFBFBF;

            font-size:18px;

        """)


        layout.addWidget(
            subtitle
        )



        # =================================================
        # AGENT STATUS
        # =================================================


        layout.addWidget(
            self.create_panel(
                "🤖 Agent System Status",
                """
Agent Manager:

ONLINE


Runtime Connection:

ACTIVE


Memory Connection:

READY


AI Engine:

CONNECTED


Status:

Operational
"""
            )
        )



        # =================================================
        # AGENTS LIST
        # =================================================


        agents_row = QHBoxLayout()



        agents_row.addWidget(
            self.create_panel(
                "🧠 Cognitive Agents",
                """
CORE Agent

Role:

System Intelligence


ARCH Agent

Role:

Architecture Assistant


CODE Agent

Role:

Development Assistant


RESEARCH Agent

Role:

Knowledge Discovery
"""
            )
        )



        agents_row.addWidget(
            self.create_panel(
                "📦 Agent Configuration",
                """
Identity

Role

Model

Memory

Tools

Permissions

Runtime
"""
            )
        )



        layout.addLayout(
            agents_row
        )



        # =================================================
        # MODEL CONNECTION
        # =================================================


        layout.addWidget(
            self.create_panel(
                "🌐 AI Model Assignment",
                """
Available Models:


Local:

Ollama


Cloud:

OpenAI

Gemini


Formats:

GGUF

Llama

Qwen

DeepSeek
"""
            )
        )



        # =================================================
        # MEMORY
        # =================================================


        layout.addWidget(
            self.create_panel(
                "🧠 Agent Memory",
                """
Short Term Memory

Conversation Context

Persistent Memory

Knowledge Access

Experience History
"""
            )
        )



        # =================================================
        # FUTURE
        # =================================================


        layout.addWidget(
            self.create_panel(
                "🚀 Future Agent Evolution",
                """
Autonomous Agents

Multi Agent Collaboration

Agent Learning

Task Planning

Self Improvement

Enterprise Agents
"""
            )
        )


        layout.addStretch()



    # =====================================================
    # PANEL CREATOR
    # =====================================================


    def create_panel(
        self,
        title,
        content
    ):


        frame = QFrame()


        frame.setStyleSheet("""

            QFrame {

                background:#20232b;

                border-radius:12px;

                border:1px solid #3A3F4B;

            }

        """)



        layout = QVBoxLayout()


        frame.setLayout(
            layout
        )



        title_label = QLabel(
            title
        )


        title_label.setStyleSheet("""

            color:#00C853;

            font-size:18px;

            font-weight:bold;

            padding:10px;

        """)



        body = QLabel(
            content
        )


        body.setWordWrap(
            True
        )


        body.setStyleSheet("""

            color:white;

            font-size:14px;

            padding:10px;

        """)



        layout.addWidget(
            title_label
        )


        layout.addWidget(
            body
        )


        return frame
