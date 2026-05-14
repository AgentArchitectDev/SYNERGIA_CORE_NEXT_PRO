import sys
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QTextEdit, QComboBox, QLabel
)
from PyQt6.QtCore import QThread, pyqtSignal

from ai.models.models_manager import ModelsManager
from ai.providers.ollama_connector import OllamaConnector
from ai.memory.memory_manager import memory


# =========================================================
# WORKER THREAD (STREAMING)
# =========================================================
class StreamWorker(QThread):
    token_signal = pyqtSignal(str)

    def __init__(self, model, messages):
        super().__init__()
        self.model = model
        self.messages = messages
        self.connector = OllamaConnector()

    def run(self):
        def callback(token):
            self.token_signal.emit(token)

        self.connector.chat_stream(
            self.model,
            self.messages,
            callback
        )


# =========================================================
# MAIN PANEL
# =========================================================
class AILabPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SYNERGIA AI LAB")
        self.resize(900, 600)

        self.models_manager = ModelsManager()

        self.init_ui()
        self.load_models()

    # =====================================================
    # UI
    # =====================================================
    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Modelo:")
        layout.addWidget(self.label)

        self.model_selector = QComboBox()
        layout.addWidget(self.model_selector)

        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Escribí tu prompt...")
        layout.addWidget(self.input_box)

        self.run_button = QPushButton("Ejecutar IA")
        self.run_button.clicked.connect(self.run_prompt)
        layout.addWidget(self.run_button)

        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        layout.addWidget(self.output_box)

        self.setLayout(layout)

    # =====================================================
    # LOAD MODELS
    # =====================================================
    def load_models(self):
        models = self.models_manager.get_model_names()
        self.model_selector.addItems(models)

    # =====================================================
    # RUN PROMPT
    # =====================================================
    def run_prompt(self):
        prompt = self.input_box.toPlainText()
        model = self.model_selector.currentText()

        self.output_box.clear()

        messages = [
            {"role": "user", "content": prompt}
        ]

        # guardar en memoria
        memory.save_prompt(prompt)

        self.worker = StreamWorker(model, messages)
        self.worker.token_signal.connect(self.update_output)
        self.worker.start()

    # =====================================================
    # STREAM UPDATE
    # =====================================================
    def update_output(self, token):
        self.output_box.insertPlainText(token)
