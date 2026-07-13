"""
=========================================================
SYNERGIA OS
Control Center V2.0 - Core Console

Runtime Module V1.0

Execution Layer

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




class RuntimePage(QWidget):


    def __init__(self):

        super().__init__()

        self.setup_ui()



    # =====================================================
    # UI PRINCIPAL
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



        # TITULO

        title = QLabel(
            "🔄 SYNERGIA RUNTIME"
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
            "Execution and Service Management Layer"
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



        # STATUS


        layout.addWidget(
            self.create_panel(
                "🔄 Runtime Status",
                """
Engine:

ONLINE


Execution Layer:

ACTIVE


Scheduler:

RUNNING


Pipeline Manager:

READY
"""
            )
        )



        # SERVICES


        services = QHBoxLayout()



        services.addWidget(
            self.create_panel(
                "⚙ Runtime Services",
                """
Kernel Service

Agent Service

Memory Service

Router Service

Knowledge Service
"""
            )
        )



        services.addWidget(
            self.create_panel(
                "🚀 Execution Engine",
                """
Active Tasks

Running Jobs

Pipelines

Background Workers

Queue Manager
"""
            )
        )



        layout.addLayout(
            services
        )



        # ENVIRONMENT


        layout.addWidget(
            self.create_panel(
                "💻 Environment",
                """
Machine:

MAQ2 Development


OS:

Linux


Framework:

PySide6


Language:

Python


Status:

Operational
"""
            )
        )



        # FUTURE


        layout.addWidget(
            self.create_panel(
                "🔮 Future Runtime Expansion",
                """
Distributed Runtime

Multi Agent Execution

Cloud Workers

Remote Nodes

Enterprise Deployment
"""
            )
        )


        layout.addStretch()



    # =====================================================
    # PANEL GENERADOR
    # =====================================================


    def create_panel(
        self,
        title,
        text
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



        content = QLabel(
            text
        )


        content.setStyleSheet("""

            color:white;

            font-size:14px;

            padding:10px;

        """)


        content.setWordWrap(
            True
        )



        layout.addWidget(
            title_label
        )


        layout.addWidget(
            content
        )


        return frame
