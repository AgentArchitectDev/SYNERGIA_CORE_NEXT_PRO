"""
=========================================================
SYNERGIA OS
Control Center V2.0 - Core Console

Models Module V1.0

AI Model Management Layer

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





class ModelsPage(QWidget):


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
            "📦 SYNERGIA MODELS"
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
            "AI Model Management and Provider Layer"
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
        # MODEL STATUS
        # =================================================


        layout.addWidget(
            self.create_panel(
                "📦 Model System Status",
                """
Model Manager:

ONLINE


Model Registry:

ACTIVE


Loading Engine:

READY


Inference Layer:

CONNECTED
"""
            )
        )



        # =================================================
        # LOCAL / CLOUD
        # =================================================


        row = QHBoxLayout()



        row.addWidget(
            self.create_panel(
                "💻 Local Models",
                """
Ollama Models


Llama


Qwen


DeepSeek


Mistral


Gemma


Phi


GGUF Models
"""
            )
        )



        row.addWidget(
            self.create_panel(
                "☁ Cloud Models",
                """
OpenAI


Gemini


Enterprise APIs


External Providers


Cloud Inference
"""
            )
        )



        layout.addLayout(
            row
        )



        # =================================================
        # PROVIDERS
        # =================================================


        layout.addWidget(
            self.create_panel(
                "🌐 AI Providers",
                """
Ollama Provider

Status:

CONNECTED


OpenAI Provider

Status:

READY


Gemini Provider

Status:

READY
"""
            )
        )



        # =================================================
        # MODEL MANAGEMENT
        # =================================================


        layout.addWidget(
            self.create_panel(
                "⚙ Model Operations",
                """
Load Model

Unload Model

Select Default Model

Test Inference

Monitor Usage

Manage Versions
"""
            )
        )



        # =================================================
        # FUTURE
        # =================================================


        layout.addWidget(
            self.create_panel(
                "🚀 Model Evolution",
                """
Fine Tuning

Model Training

Quantization

GGUF Optimization

Multi Model Routing
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
