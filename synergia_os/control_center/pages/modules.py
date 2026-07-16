"""
=========================================================
SYNERGIA OS
Control Center V2.0

Modules Management Page V1.0

Enterprise Cognitive Operating System AI
=========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFrame,
    QScrollArea
)

from PySide6.QtCore import Qt



class ModulesPage(QWidget):


    def __init__(self):

        super().__init__()

        self.setup_ui()



    def setup_ui(self):


        main = QVBoxLayout()

        self.setLayout(main)



        scroll = QScrollArea()

        scroll.setWidgetResizable(True)



        container = QWidget()

        layout = QVBoxLayout()


        layout.setContentsMargins(
            30,30,30,30
        )


        container.setLayout(layout)


        scroll.setWidget(container)


        main.addWidget(scroll)



        title = QLabel(
            "🧩 SYNERGIA MODULES"
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        title.setStyleSheet("""
            color:white;
            font-size:40px;
            font-weight:bold;
        """)


        layout.addWidget(title)



        modules = """

CORE SYSTEM

🧠 AI Engine

📦 Models

⚙ Kernel

🔄 Runtime

🤖 Agents

🧠 Memory

🧭 Cognitive Router

📚 Knowledge

📊 Runtime Monitor


Future:

Tools

Plugins

Enterprise Services

Distributed Nodes

"""


        layout.addWidget(
            self.create_box(
                "System Modules",
                modules
            )
        )



    def create_box(
        self,
        title,
        text
    ):


        frame = QFrame()


        frame.setStyleSheet("""
            QFrame{
                background:#20232b;
                border-radius:12px;
            }
        """)


        layout = QVBoxLayout()

        frame.setLayout(layout)



        h = QLabel(title)

        h.setStyleSheet("""
            color:#00C853;
            font-size:20px;
            font-weight:bold;
        """)



        b = QLabel(text)

        b.setStyleSheet("""
            color:white;
            font-size:15px;
        """)



        layout.addWidget(h)

        layout.addWidget(b)


        return frame
