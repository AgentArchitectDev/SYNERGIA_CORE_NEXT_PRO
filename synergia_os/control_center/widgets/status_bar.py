"""
=========================================================
SYNERGIA OS
Control Center V2.0 - Core Console

Status Bar Widget

Enterprise Cognitive Operating System AI
=========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel
)


from PySide6.QtCore import Qt



class StatusBar(QWidget):


    def __init__(self):

        super().__init__()

        self.initialize_ui()



    def initialize_ui(self):


        self.setFixedHeight(30)


        self.setStyleSheet("""

            QWidget {

                background-color:#111318;

                border-top:1px solid #404552;

            }


            QLabel {

                color:#BFBFBF;

                font-size:12px;

                padding-left:10px;

            }

        """)



        layout = QHBoxLayout()


        layout.setContentsMargins(
            5,
            0,
            5,
            0
        )


        self.setLayout(
            layout
        )


        # Estado izquierdo

        self.system_status = QLabel(
            "🟢 SYSTEM READY"
        )


        layout.addWidget(
            self.system_status
        )


        layout.addStretch()



        # Kernel

        self.kernel_status = QLabel(
            "Kernel: READY"
        )


        layout.addWidget(
            self.kernel_status
        )



        # Runtime

        self.runtime_status = QLabel(
            "Runtime: ONLINE"
        )


        layout.addWidget(
            self.runtime_status
        )



        # Version

        self.version_status = QLabel(
            "SYNERGIA OS V2.0"
        )


        layout.addWidget(
            self.version_status
        )
