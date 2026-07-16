"""
=========================================================
SYNERGIA OS
Control Center V2.0 - Core Console

Knowledge Module V1.0

Knowledge Management Layer

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




class KnowledgePage(QWidget):


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



        title = QLabel(
            "📚 SYNERGIA KNOWLEDGE"
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
            "Knowledge Management and Intelligence Layer"
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



        layout.addWidget(
            self.create_panel(
                "📚 Knowledge Status",
                """
Knowledge Engine:

ONLINE


Knowledge Base:

READY


Document System:

CONNECTED


Semantic Layer:

STANDBY
"""
            )
        )



        row = QHBoxLayout()



        row.addWidget(
            self.create_panel(
                "📄 Documents",
                """
Documents

Projects

Manuals

Technical Files

Research Material
"""
            )
        )



        row.addWidget(
            self.create_panel(
                "🔎 Search Engine",
                """
Keyword Search

Semantic Search

Context Search

Knowledge Retrieval
"""
            )
        )



        layout.addLayout(
            row
        )



        layout.addWidget(
            self.create_panel(
                "🧠 Knowledge Processing",
                """
Document Analysis

Information Extraction

Context Generation

Knowledge Linking

AI Assistance
"""
            )
        )



        layout.addWidget(
            self.create_panel(
                "🚀 Future Knowledge Evolution",
                """
Vector Database

Embeddings

Knowledge Graph

Semantic Memory

Autonomous Research
"""
            )
        )


        layout.addStretch()



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


        header = QLabel(
            title
        )


        header.setStyleSheet("""

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
            header
        )


        layout.addWidget(
            body
        )


        return frame
