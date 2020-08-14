from pathlib import Path
from universales.descargable import Descargable


class Subdirectorio(object):
    """ Subdirectorio """

    def __init__(self, config, ruta):
        self.config = config
        self.ruta = ruta
        self.descargables = []
        self.ya_alimentado = False
        # Definir encabezado
        ruta = Path(self.ruta)
        self.encabezado = ruta.parts[-1]

    def alimentar(self):
        """ Alimentar, rastrear los descargables """
        ruta = Path(self.ruta)
        items = []
        for extension in self.config.descargables_extensiones:
            items.extend(list(ruta.glob(f'*.{extension}')))
        self.descargables = [Descargable(self.config, str(item)) for item in items]

    def contenido(self):
        return('Contenido pendiente.')

    def __repr__(self):
        if self.ya_alimentado:
            if len(self.descargables) > 0:
                lineas = [f'<Subdirectorio> {self.encabezado}']
                lineas += ['    ' + repr(descargable) for descargable in self.descargables]
                return('\n'.join(lineas))
            else:
                return(f'<Subdirectorio> {self.encabezado} No hay archivos descargables')
        else:
            return(f'<Subdirectorio> {self.encabezado} No se ha alimentado')
