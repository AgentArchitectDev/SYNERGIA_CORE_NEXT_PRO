class Health:

    def check(self, scheduler, modules):

        report = {}

        for name, module in modules.items():

            try:
                test = module.execute("test health check")
                report[name] = "OK"
            except Exception:
                report[name] = "FAILED"

        return report


health = Health()
