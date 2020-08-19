from pathlib import Path


class SeccionFinal(object):
    """ Seccion Final """

    def __init__(self, config, ruta, nivel):
        self.config = config
        if isinstance(ruta, str):
            self.ruta = Path(ruta)
        else:
            self.ruta = ruta
        self.nivel = nivel
        self.ya_alimentado = False
        self.contenidos = None
        self.mensaje = 'NO ALIMENTADO'

    def alimentar(self):
        """ Alimentar """
        if self.ya_alimentado is False:
            # Buscar archivos md
            # ¿Hay o no hay?
            # Levantar la bandera
            self.ya_alimentado = True
        # Entregar verdadero si hay
        return(self.contenidos is not None)

    def contenido(self):
        return('Hola Mundo!')

    def __repr__(self):
        lineas = ['<SeccionFinal>']
        return('  ' * self.nivel + '\n'.join(lineas))
