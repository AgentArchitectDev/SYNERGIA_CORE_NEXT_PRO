import json
from datetime import datetime

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QComboBox, QLabel
)
from PyQt6.QtCore import QThread, pyqtSignal

from ai.models.models_manager import ModelsManager
from ai.providers.ollama_connector import OllamaConnector
from ai.memory.memory_manager import MemoryManager


# =========================================================
# STREAM WORKER
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
# MAIN SYNERGIA BRAIN PANEL
# =========================================================
class AILabPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SYNERGIA BRAIN SYSTEM v1")
        self.resize(1100, 700)

        self.models_manager = ModelsManager()
        self.memory = MemoryManager()

        self.init_ui()
        self.load_models()

    # =====================================================
    # UI
    # =====================================================
    def init_ui(self):

        layout = QHBoxLayout()

        # =========================
        # LEFT PANEL (CHAT UI)
        # =========================
        left = QVBoxLayout()

        self.model_selector = QComboBox()
        left.addWidget(QLabel("Modelo"))
        left.addWidget(self.model_selector)

        self.lang_selector = QComboBox()
        self.lang_selector.addItems(["Español", "English"])
        left.addWidget(QLabel("Idioma"))
        left.addWidget(self.lang_selector)

        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Escribí tu prompt...")
        left.addWidget(self.input_box)

        self.run_button = QPushButton("Ejecutar IA")
        self.run_button.clicked.connect(self.run_prompt)
        left.addWidget(self.run_button)

        self.export_button = QPushButton("Exportar historial")
        self.export_button.clicked.connect(self.export_history)
        left.addWidget(self.export_button)

        self.history_button = QPushButton("Ver historial")
        self.history_button.clicked.connect(self.show_history)
        left.addWidget(self.history_button)

        self.compare_button = QPushButton("Comparar modelos")
        self.compare_button.clicked.connect(self.compare_models)
        left.addWidget(self.compare_button)

        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        left.addWidget(self.output_box)

        # =========================
        # RIGHT PANEL (BRAIN)
        # =========================
        right = QVBoxLayout()

        right.addWidget(QLabel("🧠 SYNERGIA BRAIN"))

        self.brain_view = QTextEdit()
        self.brain_view.setReadOnly(True)
        right.addWidget(self.brain_view)

        # =========================
        # COMBINE PANELS
        # =========================
        layout.addLayout(left, 3)
        layout.addLayout(right, 2)

        self.setLayout(layout)

    # =====================================================
    # LOAD MODELS
    # =====================================================
    def load_models(self):
        models = self.models_manager.get_model_names()
        self.model_selector.addItems(models)

    # =====================================================
    # BRAIN ROUTING (AUTO MODEL + AGENT)
    # =====================================================
    def brain_router(self, prompt):

        p = prompt.lower()

        if "code" in p or "api" in p or "python" in p:
            return "deepseek-coder-v2:16b", "DEV_AGENT"

        if "marketing" in p or "instagram" in p or "seo" in p:
            return "mistral:latest", "MARKETING_AGENT"

        if len(prompt) < 80:
            return "phi3:mini", "LIGHT_AGENT"

        return self.model_selector.currentText(), "GENERAL_AGENT"

    # =====================================================
    # RUN PROMPT
    # =====================================================
    def run_prompt(self):

        prompt = self.input_box.toPlainText()
        language = self.lang_selector.currentText()

        model, agent = self.brain_router(prompt)

        self.output_box.clear()

        # language control
        if language == "English":
            prompt = f"Answer in English:\n\n{prompt}"

        messages = [
            {"role": "user", "content": prompt}
        ]

        # MEMORY SAVE (prompt only for now)
        self.memory.save_prompt(prompt)

        # BRAIN VIEW UPDATE
        self.brain_view.setPlainText(f"""
MODEL SELECTED: {model}
AGENT: {agent}
LANG: {language}
STATUS: RUNNING
TIME: {datetime.now().strftime('%H:%M:%S')}
        """)

        # STREAM
        self.worker = StreamWorker(model, messages)
        self.worker.token_signal.connect(self.update_output)
        self.worker.start()

    # =====================================================
    # STREAM OUTPUT
    # =====================================================
    def update_output(self, token):
        self.output_box.insertPlainText(token)

    # =====================================================
    # EXPORT
    # =====================================================
    def export_history(self):

        data = self.memory.get_context(limit=100)

        file_json = f"ai/memory/export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        file_txt = file_json.replace(".json", ".txt")

        with open(file_json, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        with open(file_txt, "w", encoding="utf-8") as f:
            for item in data:
                f.write(f"PROMPT: {item['prompt']}\n")
                f.write(f"RESPONSE: {item.get('response','')}\n\n")

        self.output_box.setPlainText(f"EXPORTED:\n{file_json}\n{file_txt}")

    # =====================================================
    # HISTORY
    # =====================================================
    def show_history(self):

        history = self.memory.get_context(limit=50)

        self.output_box.clear()

        for item in history:
            self.output_box.append("🧠 PROMPT:")
            self.output_box.append(item["prompt"])
            self.output_box.append("\n🤖 RESPONSE:")
            self.output_box.append(str(item.get("response", "")))
            self.output_box.append("\n-------------------\n")

    # =====================================================
    # MULTI MODEL COMPARE
    # =====================================================
    def compare_models(self):

        prompt = self.input_box.toPlainText()

        models = [
            self.model_selector.currentText(),
            "mistral:latest",
            "phi3:mini"
        ]

        self.output_box.clear()

        for model in models:

            self.output_box.append(f"\n===== {model} =====\n")

            messages = [
                {"role": "user", "content": prompt}
            ]

            connector = OllamaConnector()

            def callback(token):
                self.output_box.insertPlainText(token)

            connector.chat_stream(model, messages, callback)
