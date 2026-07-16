"""
===========================================================

SYNERGIA CORE NEXT_PRO

OMEGA CONTROL CENTER

RUNTIME MANAGER V1

TASK / AGENT / NODE ORCHESTRATOR

===========================================================

Responsabilidades:

- administrar tareas
- administrar agentes
- administrar nodos
- enviar comandos al Runtime Connector
- preparar MAQ1 / MAQ2


===========================================================
"""


import time


from gui.control_center.runtime_connector import (
    runtime_connector
)




class RuntimeManager:



    def __init__(self):


        self.initialized = False


        self.tasks = []


        self.completed = []


        self.agents = []


        self.nodes = []


        self.last_execution = None





    # =====================================================
    # INITIALIZE
    # =====================================================


    def initialize(
            self
    ):


        runtime_connector.connect()


        self.initialized = True



        return {


            "status":
                "runtime_manager_ready",


            "tasks":
                len(self.tasks),


            "agents":
                len(self.agents),


            "nodes":
                len(self.nodes)

        }





    # =====================================================
    # REGISTER NODE
    # =====================================================


    def register_node(
            self,
            alias
    ):


        result = runtime_connector.register_node(
            alias
        )



        node = {


            "alias":
                alias,


            "status":
                "online",


            "timestamp":
                time.time()

        }



        self.nodes.append(
            node
        )



        return {


            "status":
                "node_registered",


            "connector":
                result,


            "node":
                node

        }





    # =====================================================
    # REGISTER AGENT
    # =====================================================


    def register_agent(
            self,
            agent
    ):


        self.agents.append(
            agent
        )



        return {


            "status":
                "agent_registered",


            "agent":
                agent

        }





    # =====================================================
    # ADD TASK
    # =====================================================


    def add_task(
            self,
            task
    ):


        item = {


            "id":
                len(self.tasks)+1,


            "task":
                task,


            "status":
                "queued",


            "timestamp":
                time.time()

        }



        self.tasks.append(
            item
        )



        return {


            "status":
                "task_added",


            "task":
                item

        }





    # =====================================================
    # DISPATCH
    # =====================================================


    def dispatch(
            self,
            command
    ):


        runtime = runtime_connector.execute(
            command
        )


        task = self.add_task(
            command
        )



        return {


            "status":
                "dispatched",


            "runtime":
                runtime,


            "task":
                task

        }





    # =====================================================
    # EXECUTE NEXT
    # =====================================================


    def execute_next(
            self
    ):


        if not self.tasks:


            return {


                "status":
                    "queue_empty"

            }



        task = self.tasks.pop(0)



        task["status"] = "completed"



        self.completed.append(
            task
        )


        self.last_execution = task



        return {


            "status":
                "executed",


            "task":
                task

        }





    # =====================================================
    # STATUS
    # =====================================================


    def status(
            self
    ):


        return {


            "component":
                "OMEGA Runtime Manager V1",


            "initialized":
                self.initialized,


            "tasks":
                len(self.tasks),


            "completed":
                len(self.completed),


            "agents":
                self.agents,


            "nodes":
                self.nodes,


            "last_execution":
                self.last_execution,


            "runtime":
                runtime_connector.status()

        }





    # =====================================================
    # SNAPSHOT
    # =====================================================


    def snapshot(
            self
    ):


        return {


            "manager":
                self.status()

        }





runtime_manager = RuntimeManager()
