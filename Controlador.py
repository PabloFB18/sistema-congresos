from Asistente import Asistente
from Congreso import Congreso

# Singleton/SingletonPattern.py


class Controlador:

    class __Controlador:

        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg):

        if not Controlador.instance:
            Controlador.instance = Controlador.__Controlador(arg)
        else:
            Controlador.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)