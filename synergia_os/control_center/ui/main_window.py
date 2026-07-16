"""
=========================================================
SYNERGIA OS

Main Window V3.4

ACEA FINAL SHELL CONNECTED

Integrated:

TopBar
Sidebar
Workspace
StatusBar

Enterprise Cognitive Operating System AI
=========================================================
"""


from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)


from version import *
from constants import *


from widgets.top_bar import TopBar
from widgets.sidebar import Sidebar
from widgets.workspace import Workspace
from widgets.status_bar import StatusBar




class MainWindow(QMainWindow):


    def __init__(self):

        super().__init__()

        self.setup_ui()



    # =================================================
    # UI
    # =================================================


    def setup_ui(self):


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



        self.setStyleSheet("""

        QMainWindow{

            background:#1B1D23;

        }

        """)



        # ---------------------------------------------
        # CENTRAL
        # ---------------------------------------------


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



        # ---------------------------------------------
        # TOP BAR
        # ---------------------------------------------


        self.top_bar = TopBar()


        main_layout.addWidget(
            self.top_bar
        )



        # ---------------------------------------------
        # BODY
        # ---------------------------------------------


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



        # ---------------------------------------------
        # SIDEBAR
        # ---------------------------------------------


        self.sidebar = Sidebar()


        body_layout.addWidget(
            self.sidebar
        )



        # ---------------------------------------------
        # WORKSPACE
        # ---------------------------------------------


        self.workspace = Workspace()


        body_layout.addWidget(
            self.workspace
        )



        # ---------------------------------------------
        # CONNECTIONS
        # ---------------------------------------------


        self.sidebar.module_selected.connect(

            self.workspace.load_module

        )



        self.top_bar.home_clicked.connect(

            self.workspace.show_home

        )



        self.top_bar.exit_clicked.connect(

            self.close_system

        )



        # ---------------------------------------------
        # STATUS BAR
        # ---------------------------------------------


        self.status_bar = StatusBar()


        main_layout.addWidget(
            self.status_bar
        )



        # ---------------------------------------------
        # INITIAL HOME
        # ---------------------------------------------


        self.workspace.show_home()



    # =================================================
    # EXIT
    # =================================================


    def close_system(self):


        result = QMessageBox.question(

            self,

            "SYNERGIA OS",

            "¿Desea cerrar SYNERGIA OS?",


            QMessageBox.Yes |

            QMessageBox.No

        )


        if result == QMessageBox.Yes:


            self.close()



    # =================================================
    # WINDOW CLOSE
    # =================================================


    def closeEvent(
        self,
        event
    ):


        self.close_system()


        event.accept()

