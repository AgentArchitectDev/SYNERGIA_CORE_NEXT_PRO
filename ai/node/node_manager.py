#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================

SYNERGIA OMEGA

NODE MANAGER

CORE IA SYSTEMS

ACEA VERSION 1.0

============================================================

Administrador de nodos distribuidos.

Responsabilidades:

- Registrar nodos
- Controlar estado
- Gestionar roles
- Seleccionar nodo operativo


Futuro:

- Remote Execution
- Node Communication Bus
- Distributed Agents
- Cluster Intelligence


============================================================
"""


import time



class NodeManager:


    def __init__(self):

        self.initialized = False

        self.nodes = {}

        self.executions = 0

        self.last_selection = None



    # --------------------------------------------------

    def initialize(self):


        self.initialized = True


        return {


            "status":

            "node_manager_ready",


            "initialized":

            True

        }



    # --------------------------------------------------

    def register(

        self,

        name,

        role,

        status="online"

    ):


        node = {


            "name":

            name,


            "role":

            role,


            "status":

            status,


            "timestamp":

            time.time()

        }



        self.nodes[name] = node


        return node



    # --------------------------------------------------

    def get_nodes(self):


        return list(
            self.nodes.values()
        )



    # --------------------------------------------------

    def select_node(

        self,

        role

    ):


        self.executions += 1


        for node in self.nodes.values():


            if (

                node["role"] == role

                and

                node["status"] == "online"

            ):


                self.last_selection = node


                return {


                    "status":

                    "node_selected",


                    "node":

                    node

                }



        return {


            "status":

            "no_available_node",


            "role":

            role

        }



    # --------------------------------------------------

    def status(self):


        return {


            "component":

            "OMEGA Node Manager",


            "initialized":

            self.initialized,


            "nodes":

            len(self.nodes),


            "executions":

            self.executions,


            "last_selection":

            self.last_selection

        }




node_manager = NodeManager()
