"""
===========================================================

SYNERGIA CORE NEXT_PRO

OMEGA CONTROL CENTER

RUNTIME CONNECTOR V2

NODE COMMUNICATION LAYER

===========================================================

Responsabilidades:

- conectar runtime local
- identificar nodo
- registrar MAQ1 / MAQ2
- recibir tareas
- mantener cola runtime


Arquitectura:

CORE BRIDGE

      |

RUNTIME MANAGER

      |

RUNTIME CONNECTOR

      |

NODE EXECUTION


===========================================================
"""


import platform
import socket
import sys
import time



class RuntimeConnector:



    def __init__(self):


        self.connected = False


        self.node = {}


        self.tasks = []


        self.last_task = None





    # =====================================================
    # CONNECT
    # =====================================================


    def connect(self):


        self.node = {


            "id":
                socket.gethostname(),


            "platform":
                platform.system(),


            "python":
                platform.python_version(),


            "timestamp":
                time.time()

        }



        self.connected = True



        return {


            "status":
                "runtime_connected",


            "node":
                self.node

        }





    # =====================================================
    # REGISTER NODE
    # =====================================================


    def register_node(
            self,
            alias
    ):


        if not self.connected:

            self.connect()



        self.node["alias"] = alias



        return {


            "status":
                "node_registered",


            "alias":
                alias

        }





    # =====================================================
    # EXECUTE TASK
    # =====================================================


    def execute(
            self,
            task
    ):


        if not self.connected:

            self.connect()



        item = {


            "task":
                task,


            "timestamp":
                time.time()

        }



        self.tasks.append(
            item
        )


        self.last_task = item



        return {


            "status":
                "task_received",


            "task":
                task,


            "queue":
                len(self.tasks)

        }





    # =====================================================
    # STATUS
    # =====================================================


    def status(
            self
    ):


        return {


            "component":
                "OMEGA Runtime Connector V2",


            "connected":
                self.connected,


            "node":
                self.node,


            "tasks":
                len(self.tasks),


            "last_task":
                self.last_task

        }





    # =====================================================
    # SNAPSHOT
    # =====================================================


    def snapshot(
            self
    ):


        return {


            "connector":
                self.status()

        }





runtime_connector = RuntimeConnector()
