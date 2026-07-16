"""
===========================================================
SYNERGIA CORE NEXT_PRO
OMEGA CONTROL CENTER
MAIN WINDOW V2
===========================================================

Ventana principal completa.

Integra:

- TopBar
- SideBar
- Workspace OMEGA
- StatusBar


Arquitectura:

             MainWindow

                  |

       +----------+----------+

       |                     |

    Sidebar              Workspace

       |

    Navigation V6


                  |

              StatusBar


===========================================================
"""


from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)



from gui.control_center.top_bar import (
    top_bar
)


from gui.control_center.side_bar import (
    side_bar
)


from gui.control_center.status_bar import (
    status_bar
)



from gui.workspace.workspace_layout import (
    workspace_layout
)




class MainWindow(QMainWindow):


    """
    SYNERGIA OMEGA Main Window V2
    """



    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "SYNERGIA OMEGA CONTROL CENTER"
        )


        self.resize(
            1400,
            900
        )


        self.initialized = False



        self._build_ui()



    # -------------------------------------------------
    # BUILD UI
    # -------------------------------------------------


    def _build_ui(self):


        container = QWidget()


        main_layout = QVBoxLayout()



        # TOP BAR

        main_layout.addWidget(
            top_bar
        )



        # CENTER AREA


        center = QHBoxLayout()



        center.addWidget(
            side_bar
        )



        center.addWidget(
            workspace_layout
        )



        main_layout.addLayout(
            center
        )



        # STATUS BAR


        main_layout.addWidget(
            status_bar
        )



        container.setLayout(
            main_layout
        )


        self.setCentralWidget(
            container
        )


        self.initialized = True




    # -------------------------------------------------
    # STATUS
    # -------------------------------------------------


    def status(self):


        return {


            "component":
                "OMEGA Main Window V2",


            "title":
                self.windowTitle(),


            "size":
                {

                "width":
                    self.width(),

                "height":
                    self.height()

                },


            "initialized":
                self.initialized,


            "layout":
                [

                "TopBar",

                "SideBar",

                "Workspace",

                "StatusBar"

                ]

        }




main_window = MainWindow()
