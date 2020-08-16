from pathlib import Path


class Descargable(object):
    """ Descargable """

    def __init__(self, config, ruta, nivel):
        self.config = config
        if isinstance(ruta, str):
            self.ruta = Path(ruta)
        else:
            self.ruta = ruta
        self.nivel = nivel
        self.nombre = self.ruta.name  # Definir nombre del descargable
        self.ya_alimentado = False

    def alimentar(self):
        """ Alimentar """
        if self.ya_alimentado is False:
            self.ya_alimentado = True  # Levantar la bandera

    def __repr__(self):
        return('  ' * self.nivel + f'<Descargable> {self.nombre}')
