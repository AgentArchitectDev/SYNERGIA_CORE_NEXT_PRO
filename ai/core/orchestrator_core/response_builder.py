"""
=========================================================
SYNERGIA CORE NEXT_PRO

RESPONSE BUILDER V2

Normaliza respuestas del Orchestrator

=========================================================
"""


class ResponseBuilder:


    def build(self, context):


        if hasattr(context, "to_dict"):

            data = context.to_dict()


        else:

            data = context



        return {


            "status":
                data.get(
                    "status",
                    "unknown"
                ),


            "plan":
                data.get(
                    "plan",
                    []
                ),


            "results":
                data.get(
                    "results",
                    []

                )

        }





response_builder = ResponseBuilder()
