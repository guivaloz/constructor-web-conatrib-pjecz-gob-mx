from pathlib import Path
from universales.descargable import Descargable


class Subdirectorio(object):
    """ Subdirectorio """

    def __init__(self, config, ruta, nivel):
        self.config = config
        if isinstance(ruta, str):
            self.ruta = Path(ruta)
        else:
            self.ruta = ruta
        self.nivel = nivel
        self.nombre = self.ruta.parts[-1]
        self.descargables = None
        self.ya_alimentado = False

    def alimentar(self):
        """ Alimentar """
        if self.ya_alimentado is False:
            # Buscar descargables
            items = []
            for extension in self.config.descargables_extensiones:
                items.extend(list(self.ruta.glob(f'*.{extension}')))
            # ¿Hay o no hay?
            if len(items) > 0:
                self.descargables = []
                for item in items:
                    descargable = Descargable(self.config, item, self.nivel + 1)
                    descargable.alimentar()
                    self.descargables.append(descargable)
            else:
                self.descargables = None
            # Levantar la bandera
            self.ya_alimentado = True

    def contenido(self):
        """ Contenido entrega texto markdown """
        lineas = []
        lineas.append('#' * self.nivel + ' ' + self.nombre)
        lineas.append('')
        if self.descargables is not None:
            lineas.extend(descargable.contenido() for descargable in self.descargables)
            lineas.append('')
        return('\n'.join(lineas))

    def __repr__(self):
        lineas = [f'<Subdirectorio> {self.nombre}']
        if self.descargables is not None:
            lineas += [repr(descargable) for descargable in self.descargables]
        return('  ' * self.nivel + '\n'.join(lineas))
