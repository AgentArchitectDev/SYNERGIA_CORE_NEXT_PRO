"""
=========================================================
SYNERGIA OS

Top Bar Widget V1.2

ACEA OS CONTROL EDITION

Home + Language + Exit

Enterprise Cognitive Operating System AI
=========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QPushButton
)

from PySide6.QtCore import Signal


from core.language_manager import LanguageManager




class TopBar(QWidget):


    home_clicked = Signal()

    exit_clicked = Signal()



    def __init__(self):

        super().__init__()


        self.language_manager = LanguageManager()


        self.setup_ui()



    def setup_ui(self):


        layout = QHBoxLayout()


        layout.setContentsMargins(
            15,
            8,
            15,
            8
        )


        layout.setSpacing(
            10
        )


        self.setLayout(
            layout
        )



        # =============================================
        # TITLE
        # =============================================


        title = QLabel(
            "🧠 SYNERGIA OS | Control Center V2.0"
        )


        title.setStyleSheet("""
            QLabel{

                color:white;

                font-size:20px;

                font-weight:bold;

            }
        """)


        layout.addWidget(
            title
        )



        layout.addStretch()



        # =============================================
        # HOME BUTTON
        # =============================================


        self.home_button = QPushButton(
            "🏠"
        )


        self.home_button.setToolTip(
            "Volver al escritorio SYNERGIA OS"
        )


        self.home_button.clicked.connect(
            self.home_clicked.emit
        )


        layout.addWidget(
            self.home_button
        )



        # =============================================
        # LANGUAGE
        # =============================================


        language_icon = QLabel(
            "🌐"
        )


        layout.addWidget(
            language_icon
        )



        self.language_box = QComboBox()



        for code,name in self.language_manager.available_languages().items():


            self.language_box.addItem(
                name,
                code
            )



        layout.addWidget(
            self.language_box
        )



        # =============================================
        # EXIT
        # =============================================


        self.exit_button = QPushButton(
            "⏻"
        )


        self.exit_button.setToolTip(
            "Cerrar SYNERGIA OS"
        )


        self.exit_button.clicked.connect(
            self.exit_clicked.emit
        )


        layout.addWidget(
            self.exit_button
        )



        self.apply_style()



    def apply_style(self):


        self.setStyleSheet("""

        QWidget{

            background:#16181d;

        }


        QPushButton{

            background:#20232b;

            color:white;

            border:none;

            border-radius:6px;

            padding:6px 12px;

            font-size:16px;

        }


        QPushButton:hover{

            background:#00C853;

        }


        QComboBox{

            background:#20232b;

            color:white;

            border-radius:6px;

            padding:5px;

        }


        """)

