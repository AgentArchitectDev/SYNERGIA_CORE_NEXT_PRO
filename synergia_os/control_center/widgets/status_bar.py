"""
=========================================================
SYNERGIA OS

Status Bar V1.1

System Monitor

Enterprise Cognitive Operating System AI
=========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel
)




class StatusBar(QWidget):


    def __init__(self):

        super().__init__()


        self.setup_ui()



    def setup_ui(self):


        layout = QHBoxLayout()


        self.setLayout(
            layout
        )



        self.status = QLabel(
            "🟢 SYNERGIA CORE ONLINE"
        )


        self.runtime = QLabel(
            "Runtime ACTIVE"
        )


        self.memory = QLabel(
            "Memory READY"
        )


        self.models = QLabel(
            "Models CONNECTED"
        )



        for item in [

            self.status,

            self.runtime,

            self.memory,

            self.models

        ]:


            item.setStyleSheet("""

            color:white;

            font-size:13px;

            padding:8px;

            """)


            layout.addWidget(
                item
            )



        layout.addStretch()
