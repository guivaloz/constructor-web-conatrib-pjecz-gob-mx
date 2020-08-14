from pathlib import Path
from universales.base import Base
from universales.pagina import Pagina


class Rama(Base):
    """ Rama """

    def __init__(self, config):
        super().__init__(config, config.insumos_ruta)
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
            for directorio in self.rastrear_directorios(Path(self.config.insumos_ruta)):
                posible_md_nombre = str(directorio.parts[-1]) + '.md'
                posible_md_ruta = Path(str(directorio), posible_md_nombre)
                if posible_md_ruta.exists() and posible_md_ruta.is_file():
                    pagina = Pagina(self.config, str(directorio))
                    pagina.alimentar()
                    self.paginas.append(pagina)
            # Levantar la bandera
            self.ya_alimentado = True

    def contenido(self):
        """ Elaborar contenido """
        return('Contenido pendiente.')

    def __repr__(self):
        if self.ya_alimentado:
            lineas = []
            if self.existe_archivo_md():
                lineas += [f'<Rama> {self.archivo_md_nombre}']
            else:
                lineas += ['<Rama>']
            if len(self.paginas) > 0:
                lineas += ['  ' + repr(pagina) for pagina in self.paginas]
            return('\n'.join(lineas))
        else:
            return(f'<Rama> AVISO: No se ha alimentado')
