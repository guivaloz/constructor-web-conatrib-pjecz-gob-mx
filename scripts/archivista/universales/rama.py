from pathlib import Path
from universales.base import Base
from universales.pagina import Pagina


class Rama(Base):
    """ Rama """

    def __init__(self, config):
        super().__init__(config, config.insumos_ruta)
        self.nivel = 0
        self.secciones = []
        self.paginas = []

    def rastrear_directorios(self, ruta):
        """ Rastrear directorios """
        for item in ruta.glob('*'):
            if item.is_dir():
                yield item
                yield from self.rastrear_directorios(item)

    def alimentar(self):
        """ Alimentar """
        super().alimentar()
        if self.ya_alimentado is False:
            # Rastrear directorios en la rama
            for directorio in self.rastrear_directorios(self.config.insumos_ruta):
                posible_md_nombre = str(directorio.parts[-1]) + '.md'
                posible_md_ruta = Path(str(directorio), posible_md_nombre)
                if posible_md_ruta.exists() and posible_md_ruta.is_file():
                    # Acumular páginas
                    pagina = Pagina(self.config, directorio, self.nivel + 1)
                    pagina.alimentar()
                    self.paginas.append(pagina)
                else:
                    # Acumular secciones de descargas
                    pass
            # Levantar bandera
            self.ya_alimentado = True

    def contenido(self):
        """ Contenido """
        pass

    def __repr__(self):
        lineas = [f'<Rama> {self.relativo}']
        if len(self.secciones) > 0:
            lineas += [repr(seccion) for seccion in self.secciones]
        if len(self.paginas) > 0:
            lineas += [repr(pagina) for pagina in self.paginas]
        return('  ' * self.nivel + '\n'.join(lineas))
