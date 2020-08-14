from pathlib import Path
from universales.descargable import Descargable
from universales.seccion import Seccion
from universales.subdirectorio import Subdirectorio


class Base(object):
    """ Base """

    def __init__(self, config, ruta):
        self.config = config
        self.ruta = ruta
        self.contenidos_iniciales = []
        self.contenidos_centrales = []
        self.contenidos_finales = []
        self.ya_alimentado = False
        # Definir nombre del archivo md
        if self.ruta == self.config.insumos_ruta:
            self.archivo_md_nombre = f'{self.config.titulo}.md'
        else:
            nombre = self.ruta[len(str(self.config.insumos_ruta)) + 1:]
            self.archivo_md_nombre = f'{nombre}.md'
        # Definir la ruta al archivo md
        self.archivo_md_ruta = Path(self.ruta, self.archivo_md_nombre)

    def existe_archivo_md(self):
        """ Entrega verdadero si existe el archivo md con el mismo nombre del directorio """
        return(self.archivo_md_ruta.exists() and self.archivo_md_ruta.is_file())

    def obtener_directorios(self, ruta):
        """ Obtener los directorios en la ruta dada, entrega un listado de cadenas de texto """
        directorios = []
        for item in list(Path(self.ruta).glob('*')):
            if item.is_dir():
                directorios.append(str(item))
        return(directorios)

    def obtener_descargables(self, ruta):
        """ Obtener los descargables en una ruta dada, entrega un listado de instancias Descargable """
        ruta = Path(self.ruta)
        items = []
        for extension in self.config.descargables_extensiones:
            items.extend(list(ruta.glob(f'*.{extension}')))
        return([Descargable(self.config, str(item)) for item in items])

    def alimentar(self):
        """ Alimentar """
        if self.ya_alimentado is False:
            # Contenidos iniciales: archivo md que se llama igual al directorio
            if self.existe_archivo_md():
                self.contenidos_iniciales.append(Seccion(self.config, self.archivo_md_ruta))
            # Contenidos centrales: archivos descargables
            self.contenidos_centrales.extend(self.obtener_descargables(self.ruta))
            # Contenidos centrales: archivos descargables en subdirectorios
            for ruta3 in self.obtener_directorios(self.ruta):
                subdirectorio = Subdirectorio(self.config, ruta3)  # PENDIENTE "Descargar"
                for descargable in self.obtener_descargables(ruta3):
                    subdirectorio.agregar_descargable(descargable)
            # Contenidos finales
            # self.contenidos_finales.append()

    def __repr__(self):
        return('<Base>')
