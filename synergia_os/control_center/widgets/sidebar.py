"""
=========================================================
SYNERGIA OS
Control Center V2.0 - Core Console

Sidebar Navigation Widget

Enterprise Cognitive Operating System AI
=========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)


from PySide6.QtCore import (
    Qt,
    Signal
)



class Sidebar(QWidget):


    # Señal de navegación
    # Envía el nombre del módulo seleccionado

    module_selected = Signal(str)



    def __init__(self):

        super().__init__()

        self.buttons = {}

        self.active_button = None

        self.initialize_ui()



    def initialize_ui(self):


        self.setFixedWidth(
            260
        )


        self.setStyleSheet("""

            QWidget {

                background-color:#16181d;

            }


            QLabel {

                color:white;

                font-size:20px;

                font-weight:bold;

                padding:15px;

            }


            QPushButton {

                background-color:#20232b;

                color:white;

                border:none;

                text-align:left;

                padding:12px;

                font-size:14px;

                border-radius:5px;

            }


            QPushButton:hover {

                background-color:#303541;

            }


        """)



        layout = QVBoxLayout()


        layout.setContentsMargins(
            5,
            5,
            5,
            5
        )


        layout.setSpacing(
            4
        )


        self.setLayout(
            layout
        )



        # ---------------------------------------------
        # Titulo
        # ---------------------------------------------


        title = QLabel(
            "🧠 SYNERGIA OS"
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        layout.addWidget(
            title
        )



        # ---------------------------------------------
        # Modulos
        # ---------------------------------------------


        modules = [

            ("Dashboard","dashboard"),

            ("AI Engine","ai_engine"),

            ("Kernel","kernel"),

            ("Runtime","runtime"),

            ("Cognitive Router","router"),

            ("Agents","agents"),

            ("Models","models"),

            ("Memory","memory"),

            ("Knowledge","knowledge"),

            ("Evolution","evolution"),

            ("Projects","projects"),

            ("Documentation","documentation"),

            ("Storage","storage"),

            ("Outputs","outputs"),

            ("Monitor","monitor"),

            ("Tools","tools"),

            ("Settings","settings")

        ]



        for text, key in modules:


            button = QPushButton(
                text
            )


            button.setCursor(
                Qt.PointingHandCursor
            )


            button.clicked.connect(
                lambda checked=False,
                k=key:
                self.select_module(k)
            )


            self.buttons[key] = button


            layout.addWidget(
                button
            )



        layout.addStretch()



        # Selección inicial

        self.select_module(
            "dashboard"
        )



    def select_module(
        self,
        module
    ):


        # ---------------------------------------------
        # Restaurar botón anterior
        # ---------------------------------------------


        if self.active_button:


            self.active_button.setStyleSheet("""

                QPushButton {

                    background-color:#20232b;

                    color:white;

                }

            """)



        # ---------------------------------------------
        # Activar nuevo botón
        # ---------------------------------------------


        button = self.buttons.get(
            module
        )


        if button:


            button.setStyleSheet("""

                QPushButton {

                    background-color:#00C853;

                    color:white;

                    font-weight:bold;

                }

            """)


            self.active_button = button



        # Enviar señal

        self.module_selected.emit(
            module
        )
