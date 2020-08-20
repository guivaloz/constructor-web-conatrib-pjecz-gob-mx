from pathlib import Path


class Archivo(object):
    """ Archivo """

    def __init__(self, config, ruta, nivel):
        self.config = config
        if isinstance(ruta, str):
            self.ruta = Path(ruta)
        else:
            self.ruta = ruta
        self.nivel = nivel
        self.ya_alimentado = False

    def alimentar(self):
        """ Alimentar """
        return(False)

    def contenido(self):
        """ Contenido entrega texto markdown """
        return('')

    def __repr__(self):
        return('  ' * self.nivel + '<Archivo>')
