"""
=========================================================
SYNERGIA OS

Workspace V3.5

ACEA HYBRID RESTORE EDITION

Real Pages + Module Registry + Future Loader

Enterprise Cognitive Operating System AI
=========================================================
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFrame
)


from PySide6.QtCore import Qt


from core.module_registry import ModuleRegistry



# =====================================================
# REAL PAGES
# =====================================================


from pages.dashboard import DashboardPage
from pages.ai_engine import AIEnginePage
from pages.kernel import KernelPage
from pages.runtime import RuntimePage
from pages.cognitive_router import CognitiveRouterPage
from pages.agents import AgentsPage
from pages.models import ModelsPage
from pages.memory import MemoryPage
from pages.knowledge import KnowledgePage
from pages.modules import ModulesPage
from pages.runtime_monitor import RuntimeMonitorPage




class Workspace(QWidget):


    def __init__(self):

        super().__init__()


        self.registry = ModuleRegistry()


        self.layout_main = QVBoxLayout()


        self.layout_main.setContentsMargins(
            20,
            20,
            20,
            20
        )


        self.layout_main.setSpacing(
            10
        )


        self.setLayout(
            self.layout_main
        )


        self.current_page = None


        self.show_home()



    # =====================================================
    # CLEAR
    # =====================================================


    def clear_workspace(self):


        while self.layout_main.count():


            item = self.layout_main.takeAt(0)


            widget = item.widget()


            if widget:


                widget.deleteLater()



    # =====================================================
    # LOAD MODULE
    # =====================================================


    def load_module(
        self,
        module_key
    ):


        self.clear_workspace()



        # ---------------------------------------------
        # Buscar información Registry
        # ---------------------------------------------


        module_info = self.registry.get_module(
            module_key
        )



        # ---------------------------------------------
        # Buscar página real
        # ---------------------------------------------


        page_class = self.get_real_page(
            module_key
        )



        if page_class:


            self.current_page = page_class()



        elif module_info:


            self.current_page = self.future_module_page(
                module_info
            )



        else:


            self.current_page = self.unknown_module(
                module_key
            )



        self.layout_main.addWidget(
            self.current_page
        )



    # =====================================================
    # REAL PAGE MAP
    # =====================================================


    def get_real_page(
        self,
        key
    ):


        pages = {


            "dashboard":
            DashboardPage,


            "ai_engine":
            AIEnginePage,


            "kernel":
            KernelPage,


            "runtime":
            RuntimePage,


            "router":
            CognitiveRouterPage,


            "agents":
            AgentsPage,


            "models":
            ModelsPage,


            "memory":
            MemoryPage,


            "knowledge":
            KnowledgePage,


            "modules":
            ModulesPage,


            "runtime_monitor":
            RuntimeMonitorPage


        }



        return pages.get(
            key
        )



    # =====================================================
    # FUTURE MODULE VIEW
    # =====================================================


    def future_module_page(
        self,
        info
    ):


        page = QWidget()


        layout = QVBoxLayout()


        layout.setAlignment(
            Qt.AlignCenter
        )


        page.setLayout(
            layout
        )



        card = QFrame()



        card.setStyleSheet("""

        QFrame{

            background:#20232b;

            border-radius:18px;

            padding:35px;

        }

        """)



        card_layout = QVBoxLayout()


        card.setLayout(
            card_layout
        )



        icon = QLabel(

            info.get(
                "icon",
                "🧠"
            )

        )


        icon.setAlignment(
            Qt.AlignCenter
        )


        icon.setStyleSheet("""

        font-size:55px;

        """)



        title = QLabel(

            info.get(
                "title",
                "Module"
            )

        )


        title.setAlignment(
            Qt.AlignCenter
        )


        title.setStyleSheet("""

        color:#00C853;

        font-size:30px;

        font-weight:bold;

        """)



        description = QLabel(

f"""
Reading Module...


Description:

{info.get("description","Future module")}



Type:

{info.get("type","unknown")}



Version:

{info.get("version","future")}



Status:

{info.get("status","standby")}

"""

        )


        description.setAlignment(
            Qt.AlignCenter
        )


        description.setStyleSheet("""

        color:white;

        font-size:18px;

        """)



        card_layout.addWidget(
            icon
        )


        card_layout.addWidget(
            title
        )


        card_layout.addWidget(
            description
        )


        layout.addWidget(
            card
        )


        return page



    # =====================================================
    # UNKNOWN
    # =====================================================


    def unknown_module(
        self,
        key
    ):


        label = QLabel(

f"""
SYNERGIA OS


Unknown Module


{key}


NOT REGISTERED

"""

        )


        label.setAlignment(
            Qt.AlignCenter
        )


        label.setStyleSheet("""

        color:white;

        font-size:25px;

        """)


        return label



    # =====================================================
    # HOME
    # =====================================================


    def show_home(
        self
    ):


        self.clear_workspace()



        home = QLabel(

"""
🧠 SYNERGIA OS


Enterprise Cognitive Operating System


SYSTEM READY


Module Registry ONLINE

"""

        )


        home.setAlignment(
            Qt.AlignCenter
        )


        home.setStyleSheet("""

        color:white;

        font-size:32px;

        """)


        self.layout_main.addWidget(
            home
        )
