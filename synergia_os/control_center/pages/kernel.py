"""
=========================================================
SYNERGIA OS
Control Center V2.0 - Core Console

Kernel Module V1.0

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



class KernelPage(QWidget):


    def __init__(self):

        super().__init__()

        self.setup_ui()



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
            "⚙ SYNERGIA KERNEL"
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
            "Core Operating Layer"
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
                "🧠 Kernel Status",
                """
Kernel Core:

READY


Scheduler:

ACTIVE


Process Manager:

ONLINE


Memory Manager:

READY


System State:

NORMAL
"""
            )
        )



        # RECURSOS

        resource_row = QHBoxLayout()


        resource_row.addWidget(
            self.create_panel(
                "💻 Resources",
                """
CPU:

Monitoring


RAM:

Available


Threads:

Active


Processes:

Running
"""
            )
        )


        resource_row.addWidget(
            self.create_panel(
                "🔧 Kernel Services",
                """
Runtime Service

Memory Service

Router Service

Agent Service

Knowledge Service
"""
            )
        )


        layout.addLayout(
            resource_row
        )



        # LOGS

        layout.addWidget(
            self.create_panel(
                "📜 Kernel Events",
                """
BOOT:

SYNERGIA Kernel initialized


SYSTEM:

All services loaded


STATUS:

Waiting for operations
"""
            )
        )


        layout.addStretch()



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



        body = QLabel(
            text
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
