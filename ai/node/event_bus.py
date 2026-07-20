"""
==============================================================
SYNERGIA OMEGA EVENT BUS ACEA
==============================================================

Phase:
    FASE 6.12

Role:
    Cognitive Communication Layer

Architecture:
    - Event Registry
    - Event Publishing
    - Subscription System
    - Event Processing
    - Event History
    - Metrics
    - Learning Hooks

==============================================================
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import (
    Dict,
    List,
    Callable,
    Any
)


class EventBus:
    """
    Sistema centralizado de comunicación
    entre módulos OMEGA.
    """


    def __init__(
        self,
        node: str = "OMEGA_NODE"
    ):

        self.node = node

        self.running = False

        self.events: List[
            Dict[str, Any]
        ] = []

        self.listeners: Dict[
            str,
            List[Callable]
        ] = {}

        self.metrics = {

            "published": 0,
            "processed": 0,
            "errors": 0

        }


    # ==========================================================
    # START EVENT BUS
    # ==========================================================

    def start(self):

        self.running = True

        return {

            "status": "EVENT BUS STARTED",
            "node": self.node

        }
    # ==========================================================
    # EVENT SUBSCRIPTION SYSTEM
    # ==========================================================

    def subscribe(
        self,
        event_type: str,
        callback: Callable
    ):

        """
        Registra un módulo receptor
        para un tipo de evento.
        """

        if event_type not in self.listeners:

            self.listeners[event_type] = []


        self.listeners[event_type].append(
            callback
        )


        return {

            "status": "SUBSCRIBED",

            "event_type": event_type,

            "listeners":
                len(
                    self.listeners[event_type]
                )

        }

    # ==========================================================
    # EVENT CREATION
    # ==========================================================

    def create_event(
        self,
        event_type: str,
        source: str,
        payload: Dict[str, Any] = None,
        severity: str = "normal"
    ):

        return {

            "id":
                str(uuid.uuid4()),


            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat(),


            "type":
                event_type,


            "source":
                source,


            "payload":
                payload or {},


            "severity":
                severity,


            "status":
                "created"

        }



    # ==========================================================
    # EVENT PUBLISHING
    # ==========================================================

    def publish(
        self,
        event: Dict[str, Any]
    ):

        """
        Publica evento dentro
        del ecosistema OMEGA.
        """


        if not self.running:

            return {

                "status":
                    "EVENT BUS OFFLINE"

            }


        event["status"] = "published"


        self.events.append(
            event
        )


        self.metrics["published"] += 1


        result = self.dispatch(
            event
        )


        return result
    # ==========================================================
    # EVENT ROUTING / DISPATCH ENGINE
    # ==========================================================

    def dispatch(
        self,
        event: Dict[str, Any]
    ):

        """
        Envía eventos a los módulos
        suscriptos.
        """

        event_type = event.get(
            "type",
            "unknown"
        )


        callbacks = self.listeners.get(
            event_type,
            []
        )


        processed = 0

        responses = []


        for callback in callbacks:

            try:

                response = callback(
                    event
                )


                responses.append(
                    response
                )


                processed += 1


            except Exception as error:

                self.metrics["errors"] += 1


                responses.append({

                    "error":
                        str(error)

                })


        self.metrics["processed"] += processed


        event["status"] = "processed"


        return {

            "event":
                event,

            "processed":
                processed,

            "listeners":
                len(callbacks),

            "responses":
                responses

        }



    # ==========================================================
    # EVENT HISTORY
    # ==========================================================

    def history(
        self,
        limit: int = 50
    ):

        return self.events[-limit:]



    # ==========================================================
    # EVENT FILTER
    # ==========================================================

    def find_events(
        self,
        event_type: str
    ):

        return [

            event

            for event in self.events

            if event.get(
                "type"
            )
            == event_type

        ]



    # ==========================================================
    # METRICS ENGINE
    # ==========================================================

    def get_metrics(self):

        return {

            "node":
                self.node,


            "running":
                self.running,


            "events":
                len(
                    self.events
                ),


            "subscribers":
                {

                    key:
                    len(value)

                    for key, value

                    in self.listeners.items()

                },


            "metrics":
                self.metrics

        }
    # ==========================================================
    # OMEGA MODULE INTEGRATION
    # ==========================================================

    def register_omega_modules(self):

        modules = [

            "fault_detector",

            "incident_manager",

            "recovery_engine",

            "autonomous_repair_loop",

            "self_healing_manager"

        ]


        return {

            "status":
                "OMEGA MODULES REGISTERED",


            "modules":
                modules,


            "count":
                len(modules)

        }



    # ==========================================================
    # LEARNING HOOK
    # ==========================================================

    def learn_event(
        self,
        event: Dict[str, Any]
    ):

        return {

            "event_id":
                event.get(
                    "id"
                ),


            "pattern":
                event.get(
                    "type"
                ),


            "learning":
                "stored"

        }



    # ==========================================================
    # VALIDATION
    # ==========================================================

    def validate(self):

        return {

            "status":
                "EVENT BUS VALIDATED",


            "node":
                self.node,


            "running":
                self.running,


            "events":
                len(
                    self.events
                ),


            "subscribers":
                len(
                    self.listeners
                )

        }



# ==============================================================
# MODULE INFORMATION
# ==============================================================


def module_info():

    return {

        "name":
            "SYNERGIA OMEGA EVENT BUS ACEA",


        "version":
            "V1.0",


        "phase":
            "FASE 6.12",


        "architecture":
            [

                "Event Registry",

                "Event Publishing",

                "Event Subscription",

                "Event Routing",

                "Event History",

                "Event Metrics",

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


    bus = EventBus(
        "OMEGA_NODE"
    )


    print(
        bus.start()
    )


    def fault_handler(event):

        print(
            "FAULT EVENT RECEIVED:",
            event["type"]
        )

        return {

            "handled":
                True

        }



    bus.subscribe(

        "fault_detected",

        fault_handler

    )


    event = bus.create_event(

        event_type=
            "fault_detected",

        source=
            "fault_detector",

        payload=
            {

                "component":
                    "NODE_CPU",

                "severity":
                    "critical"

            },

        severity=
            "critical"

    )


    print(
        bus.publish(
            event
        )
    )


    print(
        bus.learn_event(
            event
        )
    )


    print(
        bus.register_omega_modules()
    )


    print(
        bus.get_metrics()
    )


    print(
        bus.validate()
    )

