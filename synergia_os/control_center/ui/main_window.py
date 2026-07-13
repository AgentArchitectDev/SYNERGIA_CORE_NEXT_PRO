"""
=========================================================
SYNERGIA OS
Control Center V2.0 - Core Console

Main Window Navigation Edition

Enterprise Cognitive Operating System AI
=========================================================
"""


from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)


from version import *
from constants import *


from widgets.top_bar import TopBar
from widgets.sidebar import Sidebar
from widgets.status_bar import StatusBar
from widgets.workspace import Workspace



class MainWindow(QMainWindow):


    def __init__(self):

        super().__init__()

        self.setup_ui()



    def setup_ui(self):


        # =============================================
        # WINDOW
        # =============================================

        self.setWindowTitle(
            f"{APP_NAME} - {APP_MODULE} {VERSION}"
        )


        self.resize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )


        self.setMinimumSize(
            MIN_WIDTH,
            MIN_HEIGHT
        )



        self.setStyleSheet(f"""

            QMainWindow {{

                background-color:{PRIMARY_COLOR};

            }}

        """)



        # =============================================
        # CENTRAL
        # =============================================


        central = QWidget()


        self.setCentralWidget(
            central
        )


        main_layout = QVBoxLayout()


        main_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )


        main_layout.setSpacing(
            0
        )


        central.setLayout(
            main_layout
        )



        # =============================================
        # TOP BAR
        # =============================================


        self.top_bar = TopBar()


        main_layout.addWidget(
            self.top_bar
        )



        # =============================================
        # BODY
        # =============================================


        body = QWidget()


        body_layout = QHBoxLayout()


        body_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )


        body_layout.setSpacing(
            0
        )


        body.setLayout(
            body_layout
        )


        main_layout.addWidget(
            body
        )



        # =============================================
        # SIDEBAR
        # =============================================


        self.sidebar = Sidebar()


        body_layout.addWidget(
            self.sidebar
        )



        # =============================================
        # WORKSPACE DINAMICO
        # =============================================


        self.workspace = Workspace()


        body_layout.addWidget(
            self.workspace
        )



        # =============================================
        # CONEXION SIDEBAR -> WORKSPACE
        # =============================================


        self.sidebar.module_selected.connect(
            self.workspace.load_module
        )



        # =============================================
        # STATUS BAR
        # =============================================


        self.status_bar = StatusBar()


        main_layout.addWidget(
            self.status_bar
        )
