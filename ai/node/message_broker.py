"""
==============================================================
SYNERGIA OMEGA MESSAGE BROKER ACEA
==============================================================

Phase:
    FASE 6.13

Role:
    Distributed Cognitive Communication Layer

Architecture:
    - Node Registry
    - Message Queue
    - Message Routing
    - Priority Management
    - Distributed Communication
    - Event Bus Integration
    - Learning Layer

==============================================================
"""


from __future__ import annotations


import uuid

from datetime import (
    datetime,
    timezone
)


from typing import (
    Dict,
    List,
    Any
)



class OmegaMessageBroker:
    """
    Broker distribuido para comunicación
    entre nodos OMEGA.
    """


    def __init__(
        self,
        node: str = "OMEGA_NODE"
    ):


        self.node = node


        self.running = False


        # Registro de nodos conectados

        self.nodes: Dict[
            str,
            Dict[str, Any]
        ] = {}


        # Cola interna de mensajes

        self.queue: List[
            Dict[str, Any]
        ] = []


        # Historial de comunicación

        self.history: List[
            Dict[str, Any]
        ] = []


        # Métricas

        self.metrics = {

            "sent": 0,

            "received": 0,

            "processed": 0,

            "errors": 0

        }


    # ==========================================================
    # BROKER START
    # ==========================================================


    def start(self):


        self.running = True


        return {

            "status":
                "MESSAGE BROKER STARTED",


            "node":
                self.node

        }
    # ==========================================================
    # NODE REGISTRY
    # ==========================================================


    def register_node(
        self,
        node_id: str,
        address: str = None,
        role: str = "worker"
    ):

        """
        Registra un nodo dentro del
        cluster OMEGA.
        """


        self.nodes[node_id] = {

            "id":
                node_id,


            "address":
                address,


            "role":
                role,


            "status":
                "online",


            "registered":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }


        return {

            "status":
                "NODE_REGISTERED",


            "node":
                node_id

        }



    # ==========================================================
    # MESSAGE CREATION
    # ==========================================================


    def create_message(
        self,
        target: str,
        message_type: str,
        payload: Dict[str, Any],
        priority: str = "normal"
    ):

        """
        Construye un mensaje
        distribuido OMEGA.
        """


        return {

            "id":
                str(
                    uuid.uuid4()
                ),


            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),


            "source":
                self.node,


            "target":
                target,


            "type":
                message_type,


            "priority":
                priority,


            "payload":
                payload,


            "status":
                "created"

        }



    # ==========================================================
    # MESSAGE QUEUE
    # ==========================================================


    def enqueue(
        self,
        message: Dict[str, Any]
    ):


        if not self.running:


            return {

                "status":
                    "BROKER OFFLINE"

            }


        self.queue.append(
            message
        )


        return {

            "status":
                "MESSAGE_QUEUED",


            "message_id":
                message.get(
                    "id"
                )

        }
    # ==========================================================
    # MESSAGE ROUTING ENGINE
    # ==========================================================


    def route_message(
        self,
        message: Dict[str, Any]
    ):

        """
        Motor de direccionamiento
        entre nodos OMEGA.
        """


        target = message.get(
            "target"
        )


        if target not in self.nodes:


            return {

                "status":
                    "TARGET_NOT_FOUND",


                "target":
                    target

            }



        message["status"] = "routed"


        self.history.append(
            message
        )


        self.metrics["sent"] += 1


        return {

            "status":
                "MESSAGE_ROUTED",


            "target":
                target,


            "message_id":
                message.get(
                    "id"
                )

        }



    # ==========================================================
    # MESSAGE PROCESSING
    # ==========================================================


    def process_queue(self):

        """
        Procesa mensajes pendientes
        del broker.
        """


        processed = 0


        responses = []


        while self.queue:


            message = self.queue.pop(
                0
            )


            result = self.route_message(
                message
            )


            responses.append(
                result
            )


            processed += 1


            self.metrics["processed"] += 1



        return {

            "processed":
                processed,


            "responses":
                responses

        }



    # ==========================================================
    # PRIORITY MANAGEMENT
    # ==========================================================


    def priority_queue(self):

        """
        Ordena mensajes críticos
        antes de procesamiento.
        """


        priority_order = {

            "critical": 0,

            "high": 1,

            "normal": 2,

            "low": 3

        }



        self.queue.sort(

            key=lambda message:

            priority_order.get(

                message.get(
                    "priority",
                    "normal"
                ),

                2

            )

        )



        return {

            "status":
                "QUEUE_PRIORITIZED",


            "size":
                len(
                    self.queue
                )

        }



    # ==========================================================
    # MESSAGE RECEIVER
    # ==========================================================


    def receive(
        self,
        message: Dict[str, Any]
    ):


        message["status"] = "received"


        self.metrics["received"] += 1


        self.queue.append(
            message
        )


        return {

            "status":
                "MESSAGE_RECEIVED",


            "message_id":
                message.get(
                    "id"
                )

        }
    # ==========================================================
    # OMEGA INTEGRATION LAYER
    # ==========================================================


    def connect_event_bus(
        self,
        event_bus=None
    ):

        """
        Preparación de integración
        con EVENT BUS ACEA.
        """


        self.event_bus = event_bus


        return {

            "status":
                "EVENT BUS CONNECTED"

        }



    # ==========================================================
    # LEARNING LAYER
    # ==========================================================


    def learn_message(
        self,
        message: Dict[str, Any]
    ):


        return {

            "message_id":
                message.get(
                    "id"
                ),


            "pattern":
                message.get(
                    "type"
                ),


            "learning":
                "stored"

        }



    # ==========================================================
    # BROKER STATUS
    # ==========================================================


    def status(self):

        return {

            "node":
                self.node,


            "running":
                self.running,


            "nodes":
                len(
                    self.nodes
                ),


            "queue":
                len(
                    self.queue
                ),


            "history":
                len(
                    self.history
                ),


            "metrics":
                self.metrics

        }



# ==============================================================
# MODULE INFORMATION
# ==============================================================


def module_info():

    return {

        "name":
            "SYNERGIA OMEGA MESSAGE BROKER ACEA",


        "version":
            "V1.0",


        "phase":
            "FASE 6.13",


        "architecture":

            [

                "Node Registry",

                "Message Queue",

                "Message Routing",

                "Priority Management",

                "Distributed Communication",

                "Event Bus Integration",

                "Learning Layer"

            ]

    }



# ==============================================================
# ACEA TEST EXECUTION
# ==============================================================


if __name__ == "__main__":


    print(
        module_info()
    )


    broker = OmegaMessageBroker(
        "MAQ2_WORK_NODE"
    )


    print(
        broker.start()
    )


    print(
        broker.register_node(

            "MAQ1_HOME_NODE",

            "192.168.1.10",

            "development"

        )
    )


    print(
        broker.register_node(

            "MAQ2_WORK_NODE",

            "192.168.1.20",

            "production"

        )
    )



    message = broker.create_message(

        target=
            "MAQ1_HOME_NODE",


        message_type=
            "recovery_request",


        payload=
            {

                "component":
                    "NODE_ENGINE",


                "action":
                    "restart"

            },


        priority=
            "critical"

    )


    print(
        broker.enqueue(
            message
        )
    )


    print(
        broker.priority_queue()
    )


    print(
        broker.process_queue()
    )


    print(
        broker.learn_message(
            message
        )
    )


    print(
        broker.status()
    )
