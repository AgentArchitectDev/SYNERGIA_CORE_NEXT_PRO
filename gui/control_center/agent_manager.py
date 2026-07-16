"""
===========================================================

SYNERGIA CORE NEXT_PRO

OMEGA CONTROL CENTER

AGENT MANAGER V1

MULTI AGENT ORCHESTRATOR

===========================================================

Responsabilidades:

- administrar agentes
- registrar agentes SYNERGIA
- controlar ciclo de vida
- asignar tareas
- conectar con Runtime Manager


Arquitectura:

CORE BRIDGE

      |

RUNTIME MANAGER

      |

AGENT MANAGER

      |

AGENTS


===========================================================
"""


import time


from gui.control_center.runtime_manager import (
    runtime_manager
)




class AgentManager:



    def __init__(self):


        self.initialized = False


        self.agents = {}


        self.history = []


        self.last_agent = None





    # =====================================================
    # INITIALIZE
    # =====================================================


    def initialize(
            self
    ):


        runtime_manager.initialize()


        self.initialized = True



        return {


            "status":
                "agent_manager_ready",


            "agents":
                len(self.agents)

        }





    # =====================================================
    # REGISTER AGENT
    # =====================================================


    def register(
            self,
            name,
            role="general"
    ):


        agent = {


            "name":
                name,


            "role":
                role,


            "status":
                "offline",


            "created":
                time.time(),


            "tasks":
                []

        }



        self.agents[name] = agent


        self.last_agent = name



        self.history.append(
            {
                "action":
                    "register",

                "agent":
                    name,

                "time":
                    time.time()
            }
        )



        return {


            "status":
                "agent_registered",


            "agent":
                agent

        }





    # =====================================================
    # START AGENT
    # =====================================================


    def start(
            self,
            name
    ):


        if name not in self.agents:


            return {


                "status":
                    "agent_not_found"

            }



        self.agents[name]["status"] = "online"



        return {


            "status":
                "agent_started",


            "agent":
                name

        }





    # =====================================================
    # STOP AGENT
    # =====================================================


    def stop(
            self,
            name
    ):


        if name not in self.agents:


            return {


                "status":
                    "agent_not_found"

            }



        self.agents[name]["status"] = "offline"



        return {


            "status":
                "agent_stopped",


            "agent":
                name

        }





    # =====================================================
    # SEND TASK
    # =====================================================


    def send_task(
            self,
            name,
            task
    ):


        if name not in self.agents:


            return {


                "status":
                    "agent_not_found"

            }



        self.agents[name]["tasks"].append(
            task
        )



        runtime = runtime_manager.dispatch(
            task
        )



        return {


            "status":
                "task_assigned",


            "agent":
                name,


            "task":
                task,


            "runtime":
                runtime

        }





    # =====================================================
    # STATUS
    # =====================================================


    def status(
            self
    ):


        return {


            "component":
                "OMEGA Agent Manager V1",


            "initialized":
                self.initialized,


            "agents":
                self.agents,


            "count":
                len(self.agents),


            "last_agent":
                self.last_agent

        }





    # =====================================================
    # SNAPSHOT
    # =====================================================


    def snapshot(
            self
    ):


        return {


            "manager":
                self.status(),


            "runtime":
                runtime_manager.status()

        }





agent_manager = AgentManager()
