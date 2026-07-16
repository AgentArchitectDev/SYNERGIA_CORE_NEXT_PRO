"""
===========================================================
SYNERGIA CORE NEXT_PRO
KERNEL ADAPTER V1
===========================================================

Capa de compatibilidad hacia Kernel Core.

Mantiene una interfaz simple:

from ai.kernel.kernel import kernel

kernel.boot()

kernel.status()

===========================================================
"""


from ai.kernel.kernel_core import kernel as core_kernel



class KernelAdapter:


    def __init__(self):

        self.version = "1.0 Adapter"



    # -------------------------------------------------

    def boot(self):

        return core_kernel.boot()



    # -------------------------------------------------

    def register_service(
        self,
        name,
        service
    ):

        return core_kernel.register_service(
            name,
            service
        )



    # -------------------------------------------------

    def start_service(
        self,
        name
    ):

        return core_kernel.start_service(
            name
        )



    # -------------------------------------------------

    def shutdown(self):

        return core_kernel.shutdown()



    # -------------------------------------------------

    def status(self):

        return core_kernel.status()



    # -------------------------------------------------

    def info(self):

        return {

            "component":
                "Kernel Adapter",

            "version":
                self.version,

            "backend":
                "Kernel Core V1"

        }



# =====================================================
# SINGLETON
# =====================================================

kernel = KernelAdapter()
