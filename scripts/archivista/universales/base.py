from pathlib import Path
from universales.seccion_inicial import SeccionInicial
from universales.seccion_descargables import SeccionDescargables
from universales.seccion_subdirectorios import SeccionSubdirectorios


class Base(object):
    """ Base """

    def __init__(self, config, ruta):
        self.config = config
        if isinstance(ruta, str):
            self.ruta = Path(ruta)
        else:
            self.ruta = ruta
        self.nivel = 0
        self.ya_alimentado = False
        # Definir la ruta relativa donde estamos respecto al depósito
        self.relativo = str(self.ruta)[len(str(self.config.nextcloud_ruta)):]

    def alimentar(self):
        if self.ya_alimentado is False:
            # Sección Inicial
            seccion_inicial = SeccionInicial(self.config, self.ruta, self.nivel + 1)
            seccion_inicial.alimentar()
            if seccion_inicial.contenidos is not None:
                self.secciones.append(seccion_inicial)
            # Sección Descargables
            seccion_descargables = SeccionDescargables(self.config, self.ruta, self.nivel + 1)
            seccion_descargables.alimentar()
            if seccion_descargables.contenidos is not None:
                self.secciones.append(seccion_descargables)
            # Sección Subdirectorios
            seccion_subdirectorios = SeccionSubdirectorios(self.config, self.ruta, self.nivel + 1)
            seccion_subdirectorios.alimentar()
            if seccion_subdirectorios.contenidos is not None:
                self.secciones.append(seccion_subdirectorios)
            # Sección Final

    def __repr__(self):
        return('  ' * self.nivel + f'<Base> {self.relativo}')
