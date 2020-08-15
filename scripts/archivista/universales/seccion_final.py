from pathlib import Path


class SeccionFinal(object):
    """ Seccion Final """

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
        """ Alimentar """
        if self.ya_alimentado is False:
            # Buscar archivos md
            # ¿Se encontaron o no?
            # Levantar la bandera
            self.ya_alimentado = True

    def contenido(self):
        pass

    def __repr__(self):
        lineas = ['<SeccionFinal>']
        return('\n'.join(lineas))
