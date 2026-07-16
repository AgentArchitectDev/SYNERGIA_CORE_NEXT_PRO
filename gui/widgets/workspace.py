"""
======================================================================
SYNERGIA CONTROL CENTER
WORKSPACE V5 ENTERPRISE
======================================================================

Workspace completamente dinámico.

No conoce módulos.

No conoce páginas.

Todo se obtiene desde ModuleRegistry.

======================================================================
"""

from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QStackedWidget

from PySide6.QtCore import Qt

from gui.core.module_registry import module_registry


class Workspace(QWidget):

    def __init__(self):

        super().__init__()

        self.stack = QStackedWidget()

        self.pages = {}

        self.build_ui()

        self.load_modules()

    # -----------------------------------------------------

    def build_ui(self):

        layout = QVBoxLayout()

        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout.addWidget(
            self.stack
        )

        self.setLayout(layout)

    # -----------------------------------------------------

    def load_modules(self):

        try:

            module_registry.load_modules()

            pages = module_registry.get_all()

            for module_id, widget in pages.items():

                self.pages[module_id] = widget

                self.stack.addWidget(widget)

            if self.pages:

                first = next(iter(self.pages.values()))

                self.stack.setCurrentWidget(first)

        except Exception as e:

            self.show_error(str(e))

    # -----------------------------------------------------

    def show_page(self, module_id):

        if module_id not in self.pages:

            return

        self.stack.setCurrentWidget(

            self.pages[module_id]

        )

    # -----------------------------------------------------

    def reload(self):

        while self.stack.count():

            widget = self.stack.widget(0)

            self.stack.removeWidget(widget)

            widget.deleteLater()

        self.pages.clear()

        module_registry.reload()

        self.load_modules()

    # -----------------------------------------------------

    def show_error(self, message):

        label = QLabel(

            f"ERROR\n\n{message}"

        )

        label.setAlignment(

            Qt.AlignCenter

        )

        self.stack.addWidget(label)

        self.stack.setCurrentWidget(label)

    # -----------------------------------------------------

    def status(self):

        return {

            "workspace": "V5 Enterprise",

            "pages": len(self.pages),

            "modules": list(self.pages.keys())

        }


workspace = Workspace()
