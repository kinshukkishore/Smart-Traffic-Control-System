from django.apps import AppConfig
import sim
import tc
import sys


class TcvConfig(AppConfig):
    name = 'tcv'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True
        sim.setup()
        sim.start()
        tc.setup()
        tc.start()
