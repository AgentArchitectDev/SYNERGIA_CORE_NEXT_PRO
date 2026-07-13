"""
=========================================================
SYNERGIA OS
Control Center V2.0 - Core Console

Workspace Module Loader V2.7

Integrated Modules:

Dashboard
AI Engine
Kernel
Runtime
Agents
Memory

Enterprise Cognitive Operating System AI
=========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)


from PySide6.QtCore import Qt



# =====================================================
# REAL MODULE IMPORTS
# =====================================================


from pages.dashboard import DashboardPage

from pages.ai_engine import AIEnginePage

from pages.kernel import KernelPage

from pages.runtime import RuntimePage

from pages.agents import AgentsPage

from pages.memory import MemoryPage





class Workspace(QWidget):


    def __init__(self):

        super().__init__()



        self.workspace_layout = QVBoxLayout()



        self.workspace_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )



        self.workspace_layout.setAlignment(
            Qt.AlignCenter
        )



        self.setLayout(
            self.workspace_layout
        )



        self.current_page = None



        self.show_home()



    # =====================================================
    # CLEAR CURRENT MODULE
    # =====================================================


    def clear_workspace(self):


        while self.workspace_layout.count():


            item = self.workspace_layout.takeAt(0)



            widget = item.widget()



            if widget:


                widget.deleteLater()





    # =====================================================
    # MODULE ROUTER ENGINE
    # =====================================================


    def load_module(
        self,
        module
    ):


        self.clear_workspace()



        # ===============================================
        # DASHBOARD
        # ===============================================


        if module == "dashboard":


            self.current_page = DashboardPage()



        # ===============================================
        # AI ENGINE
        # ===============================================


        elif module == "ai_engine":


            self.current_page = AIEnginePage()



        # ===============================================
        # KERNEL
        # ===============================================


        elif module == "kernel":


            self.current_page = KernelPage()



        # ===============================================
        # RUNTIME
        # ===============================================


        elif module == "runtime":


            self.current_page = RuntimePage()



        # ===============================================
        # AGENTS
        # ===============================================


        elif module == "agents":


            self.current_page = AgentsPage()



        # ===============================================
        # MEMORY
        # ===============================================


        elif module == "memory":


            self.current_page = MemoryPage()



        # ===============================================
        # FUTURE MODULES
        # ===============================================


        else:


            self.current_page = self.create_placeholder(
                module
            )



        self.workspace_layout.addWidget(
            self.current_page
        )



    # =====================================================
    # DEFAULT HOME
    # =====================================================


    def show_home(self):


        self.clear_workspace()



        title = QLabel(
            "SYNERGIA OS"
        )


        title.setAlignment(
            Qt.AlignCenter
        )



        title.setStyleSheet("""

            font-size:48px;

            font-weight:bold;

            color:white;

        """)



        subtitle = QLabel(
            "Control Center V2.0 - Core Console"
        )


        subtitle.setAlignment(
            Qt.AlignCenter
        )



        subtitle.setStyleSheet("""

            font-size:20px;

            color:#BFBFBF;

        """)



        self.workspace_layout.addWidget(
            title
        )


        self.workspace_layout.addWidget(
            subtitle
        )



    # =====================================================
    # FUTURE MODULE PLACEHOLDER
    # =====================================================


    def create_placeholder(
        self,
        module
    ):


        page = QWidget()



        layout = QVBoxLayout()



        layout.setAlignment(
            Qt.AlignCenter
        )



        page.setLayout(
            layout
        )



        title = QLabel(
            module.upper()
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        title.setStyleSheet("""

            font-size:40px;

            font-weight:bold;

            color:white;

        """)



        status = QLabel(
            "SYNERGIA Module - Loading..."
        )


        status.setAlignment(
            Qt.AlignCenter
        )


        status.setStyleSheet("""

            font-size:18px;

            color:#BFBFBF;

        """)



        layout.addWidget(
            title
        )


        layout.addWidget(
            status
        )



        return page
