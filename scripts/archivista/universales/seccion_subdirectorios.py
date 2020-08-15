from pathlib import Path


class SeccionSubdirectorios(object):
    """ Seccion Subdirectorios """

    def __init__(self, config, ruta):
        self.config = config
        if isinstance(ruta, str):
            self.ruta = Path(ruta)
        else:
            self.ruta = ruta
        self.ya_alimentado = False
        self.mensaje = 'NO ALIMENTADO'
        self.contenidos = None

    def alimentar(self):
        pass

    def contenido(self):
        pass

    def __repr__(self):
        lineas = ['<SeccionSubdirectorios>']
        return('\n'.join(lineas))
