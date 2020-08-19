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
        self.archivo_nombre = None
        self.archivo_ruta = None

    def alimentar(self):
        """ Alimentar """
        if self.ya_alimentado is False:
            # Definir nombre del archivo md
            nombre = self.ruta.parts[-1] + '.md'
            ruta = Path(self.ruta, nombre)
            # ¿Hay o no hay?
            if ruta.exists() and ruta.is_file():
                self.archivo_nombre = nombre
                self.archivo_ruta = ruta
            # Levantar bandera
            self.ya_alimentado = True
        # Entregar verdadero si hay
        return(self.archivo_ruta is not None)

    def contenido(self):
        """ Contenido entrega texto markdown """
        if self.ya_alimentado and self.archivo_ruta is not None:
            with open(str(self.archivo_ruta), 'r') as puntero:
                return(puntero.read())
        else:
            return('')

    def __repr__(self):
        return('  ' * self.nivel + '<Archivo> ' + self.archivo_nombre)
