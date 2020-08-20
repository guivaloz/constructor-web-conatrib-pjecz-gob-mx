from pathlib import Path
from universales.descargable import Descargable
from universales.vinculo_relativo import VinculoRelativo


class Subdirectorio(object):
    """ Subdirectorio """

    def __init__(self, config, ruta, nivel):
        self.config = config
        if isinstance(ruta, str):
            self.ruta = Path(ruta)
        else:
            self.ruta = ruta
        self.nivel = nivel
        self.ya_alimentado = False
        self.nombre = self.ruta.parts[-1]
        self.contenidos = None

    def alimentar(self):
        """ Alimentar """
        if self.ya_alimentado is False:
            # Buscar archivo md que se llame igual que el directorio
            vinculo_relativo = VinculoRelativo(self.config, self.ruta, self.nivel + 1)
            if vinculo_relativo.alimentar():
                self.contenidos = [vinculo_relativo]
            else:
                # No hay, entonces buscar descargables
                items = []
                for extension in self.config.descargables_extensiones:
                    items.extend(list(self.ruta.glob(f'*.{extension}')))
                # ¿Hay o no hay?
                if len(items) > 0:
                    self.contenidos = []
                    for item in items:
                        descargable = Descargable(self.config, item, self.nivel + 1)
                        descargable.alimentar()
                        self.contenidos.append(descargable)
            # Levantar la bandera
            self.ya_alimentado = True
        # Entregar verdadero si hay
        return(self.contenidos is not None)

    def contenido(self):
        """ Contenido entrega texto markdown """
        if self.ya_alimentado:
            lineas = []
            lineas.append('#' * self.nivel + ' ' + self.nombre)
            lineas.append('')
            if self.contenidos is not None:
                lineas.extend(item.contenido() for item in self.contenidos)
                lineas.append('')
            return('\n'.join(lineas))
        else:
            return('')

    def __repr__(self):
        lineas = []
        lineas.append(f'<Subdirectorio> {self.nombre}')
        if self.contenidos is not None:
            lineas.extend([repr(item) for item in self.contenidos])
        return('  ' * self.nivel + '\n'.join(lineas))
