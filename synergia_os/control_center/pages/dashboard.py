"""
=========================================================
SYNERGIA OS
Control Center V2.0 - Core Console

Dashboard Module V1.2
Enterprise Console Edition

Enterprise Cognitive Operating System AI
=========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QScrollArea,
    QSizePolicy
)


from PySide6.QtCore import Qt




class DashboardPage(QWidget):


    def __init__(self):

        super().__init__()

        self.setup_ui()



    # =====================================================
    # MAIN UI
    # =====================================================


    def setup_ui(self):


        main_layout = QVBoxLayout()


        main_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )


        self.setLayout(
            main_layout
        )



        # =================================================
        # SCROLL PRINCIPAL
        # =================================================


        scroll = QScrollArea()


        scroll.setWidgetResizable(
            True
        )


        scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )


        scroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarAsNeeded
        )


        scroll.setStyleSheet("""

            QScrollArea {

                border:none;

                background:#101217;

            }


            QScrollBar:vertical {

                width:14px;

                background:#16181d;

            }


            QScrollBar::handle:vertical {

                background:#00C853;

                border-radius:7px;

            }

        """)



        container = QWidget()



        dashboard_layout = QVBoxLayout()


        dashboard_layout.setContentsMargins(
            35,
            35,
            35,
            35
        )


        dashboard_layout.setSpacing(
            25
        )


        container.setLayout(
            dashboard_layout
        )



        scroll.setWidget(
            container
        )


        main_layout.addWidget(
            scroll
        )



        # =================================================
        # TITULO
        # =================================================


        self.add_title(
            dashboard_layout,
            "🏠 SYNERGIA OS DASHBOARD"
        )


        self.add_subtitle(
            dashboard_layout,
            "Enterprise Cognitive Operating System AI"
        )



        # =================================================
        # SYSTEM STATUS
        # =================================================


        dashboard_layout.addWidget(
            self.section_title(
                "SYSTEM STATUS"
            )
        )


        status_row = QHBoxLayout()


        status_row.addWidget(
            self.create_panel(
                "🧠 Kernel",
                """
Status:

READY


Core:

SYNERGIA Kernel


Processes:

Active


Scheduler:

Running
"""
            )
        )


        status_row.addWidget(
            self.create_panel(
                "🔄 Runtime",
                """
Status:

ONLINE


Environment:

Execution Layer


Services:

Active


Tasks:

Available
"""
            )
        )


        status_row.addWidget(
            self.create_panel(
                "💾 Memory",
                """
Status:

ACTIVE


Storage:

Connected


Sessions:

Loaded


Context:

Ready
"""
            )
        )


        status_row.addWidget(
            self.create_panel(
                "🤖 AI Engine",
                """
Status:

CONNECTED


Pipeline:

Ready


Models:

Available


Inference:

Online
"""
            )
        )


        dashboard_layout.addLayout(
            status_row
        )



        # =================================================
        # AI ECOSYSTEM
        # =================================================


        dashboard_layout.addWidget(
            self.section_title(
                "AI ECOSYSTEM"
            )
        )


        ai_row = QHBoxLayout()



        ai_row.addWidget(
            self.create_panel(
                "🌐 AI Providers",
                """
Ollama

OpenAI

Gemini

Local Providers

External Providers
"""
            )
        )



        ai_row.addWidget(
            self.create_panel(
                "📦 Models",
                """
Local Models

Cloud Models

GGUF Models

Coding Models

Reasoning Models
"""
            )
        )



        ai_row.addWidget(
            self.create_panel(
                "🧩 Modules",
                """
CORE

Runtime

Agents

Memory

Knowledge

Evolution
"""
            )
        )


        dashboard_layout.addLayout(
            ai_row
        )



        # =================================================
        # ARCHITECTURE
        # =================================================


        dashboard_layout.addWidget(
            self.section_title(
                "SYNERGIA ARCHITECTURE"
            )
        )


        dashboard_layout.addWidget(
            self.create_panel(
                "🏗 CORE NEXT PRO",
                """
Architecture:

SYNERGIA_CORE_NEXT_PRO


Layers:

AI Layer

Kernel Layer

Runtime Layer

Storage Layer

Interface Layer


Mode:

Enterprise Cognitive OS
"""
            )
        )



        # =================================================
        # SYSTEM INFORMATION
        # =================================================


        dashboard_layout.addWidget(
            self.section_title(
                "SYSTEM INFORMATION"
            )
        )


        dashboard_layout.addWidget(
            self.create_panel(
                "⚙ System Information",
                """
Project:

SYNERGIA_CORE_NEXT_PRO


Version:

SYNERGIA OS V2.0


Edition:

Core Console


Machine:

MAQ2 Development


Status:

Operational


Environment:

Linux + PySide6


Interface:

Enterprise Console
"""
            )
        )



        # =================================================
        # FUTURE EXPANSION
        # =================================================


        dashboard_layout.addWidget(
            self.section_title(
                "FUTURE EXPANSION"
            )
        )


        dashboard_layout.addWidget(
            self.create_panel(
                "🚀 Roadmap Modules",
                """
Kernel Monitor

Runtime Manager

Cognitive Router

Agent System

Evolution Engine

Knowledge Graph

Enterprise Services

Security Layer

Distributed Execution
"""
            )
        )



        dashboard_layout.addStretch()



    # =====================================================
    # COMPONENTES
    # =====================================================


    def add_title(
        self,
        layout,
        text
    ):


        label = QLabel(
            text
        )


        label.setAlignment(
            Qt.AlignCenter
        )


        label.setStyleSheet("""

            font-size:40px;

            font-weight:bold;

            color:white;

        """)


        layout.addWidget(
            label
        )



    def add_subtitle(
        self,
        layout,
        text
    ):


        label = QLabel(
            text
        )


        label.setAlignment(
            Qt.AlignCenter
        )


        label.setStyleSheet("""

            font-size:18px;

            color:#BFBFBF;

        """)


        layout.addWidget(
            label
        )



    def section_title(
        self,
        text
    ):


        label = QLabel(
            text
        )


        label.setStyleSheet("""

            color:#00C853;

            font-size:20px;

            font-weight:bold;

            padding-top:10px;

        """)


        return label



    def create_panel(
        self,
        title,
        content
    ):


        panel = QFrame()


        panel.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred
        )


        panel.setStyleSheet("""

            QFrame {

                background-color:#20232b;

                border-radius:12px;

                border:1px solid #3A3F4B;

            }

        """)



        layout = QVBoxLayout()


        panel.setLayout(
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



        content_label = QLabel(
            content
        )


        content_label.setWordWrap(
            True
        )


        content_label.setStyleSheet("""

            color:white;

            font-size:14px;

            padding:10px;

        """)



        layout.addWidget(
            title_label
        )


        layout.addWidget(
            content_label
        )


        return panel
