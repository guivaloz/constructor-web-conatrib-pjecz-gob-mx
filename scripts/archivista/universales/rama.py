from pathlib import Path
from universales.base import Base
from universales.pagina import Pagina


class Rama(Base):
    """ Rama """

    def __init__(self, config):
        super().__init__(config, config.insumos_ruta)
        self.nivel = 0
        self.paginas = []

    def rastrear_directorios_con_md_igual(self, ruta):
        """ Rastrear directorios con archivos.md de igual nombre que el directorio """
        for item in ruta.glob('*'):
            if item.is_dir():
                # Si tiene dentro un archivo <directorio>.md se acumula
                posible_md_nombre = item.parts[-1] + '.md'
                posible_md_ruta = Path(item, posible_md_nombre)
                if posible_md_ruta.exists() and posible_md_ruta.is_file():
                    yield item
                # Ser recursivo
                yield from self.rastrear_directorios_con_md_igual(item)

    def alimentar(self):
        """ Alimentar """
        hay_secciones = super().alimentar()
        if self.ya_alimentado is False:
            # Acumular páginas
            for directorio in self.rastrear_directorios_con_md_igual(self.config.insumos_ruta):
                pagina = Pagina(self.config, directorio, self.nivel + 1)
                if pagina.alimentar():
                    self.paginas.append(pagina)
            # Levantar bandera
            self.ya_alimentado = True
        # Entregar verdadero si hay secciones o páginas
        return(hay_secciones or len(self.paginas) > 0)

    def crear(self):
        """ Crear """
        lineas = [super().crear()]
        if len(self.paginas) > 0:
            lineas += [pagina.crear() for pagina in self.paginas]
        return('  ' * self.nivel + '\n'.join(lineas))

    def __repr__(self):
        lineas = []
        lineas.append(f'<Rama> {self.relativo}')
        if len(self.secciones) > 0:
            lineas.extend([repr(seccion) for seccion in self.secciones])
        if len(self.paginas) > 0:
            lineas.extend([repr(pagina) for pagina in self.paginas])
        return('  ' * self.nivel + '\n'.join(lineas))
