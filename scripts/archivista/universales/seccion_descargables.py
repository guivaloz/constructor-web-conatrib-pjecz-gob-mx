from pathlib import Path
from universales.descargable import Descargable


class SeccionDescargables(object):
    """ Seccion Descargables """

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
            # Buscar descargables
            items = []
            for extension in self.config.descargables_extensiones:
                items.extend(list(self.ruta.glob(f'*.{extension}')))
            # ¿Hay o no hay?
            if len(items) > 0:
                self.contenidos = [Descargable(self.config, item) for item in items]
                self.mensaje = 'Descargar'
            else:
                self.contenidos = None
                self.mensaje = 'NO HAY DESCARGABLES'
            # Levantar la bandera
            self.ya_alimentado = True

    def contenido(self):
        pass

    def __repr__(self):
        lineas = [f'<SeccionDescargables> {self.mensaje}']
        if self.contenidos is not None:
            lineas += ['      ' + repr(contenido) for contenido in self.contenidos]
        return('\n'.join(lineas))
