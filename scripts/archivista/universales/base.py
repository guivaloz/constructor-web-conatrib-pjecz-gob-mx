from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from comunes.funciones import cambiar_a_ruta_segura
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
        self.plantilla = None
        # Definir la ruta relativa donde estamos respecto al depósito
        self.relativo = str(self.ruta)[len(str(self.config.nextcloud_ruta)):]

    def alimentar(self):
        """ Alimentar """
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

    def contenido(self):
        """ Contenido """
        return('Hola Mundo!')

    def preparar_plantilla(self):
        """ Preparar la plantilla Jinja2 """
        if self.plantilla is None:
            # Preparar plantilla
            plantillas_ruta = Path(self.config.plantillas_ruta)
            if not(plantillas_ruta.exists() or plantillas_ruta.is_dir()):
                raise(Exception('ERROR: No existe el directorio de plantillas'))
            plantillas_env = Environment(
                loader=FileSystemLoader(str(plantillas_ruta)),
                trim_blocks=True,
                lstrip_blocks=True,
            )
            self.plantilla = plantillas_env.get_template(self.config.plantilla)

    def crear(self):
        """ Crear archivo md """
        # Elaborar contenido con la plantilla
        if self.plantilla is None:
            self.preparar_plantilla()
        content = self.plantilla.render(
            title='Título',
            slug='slug',
            summary='resumen',
            tags='etiquetas',
            url='url',
            save_as='guardar_como_ruta',
            date='2020-08-15 12:00',
            modified='2020-08-15 12:00',
            content=self.contenido(),
        )
        # Crear directorio
        destino_directorio_ruta = Path(str(self.config.salida_ruta) + cambiar_a_ruta_segura(self.relativo))
        destino_directorio_ruta.mkdir(parents=True, exist_ok=True)
        # Escribir archivo md
        nombre = cambiar_a_ruta_segura(self.ruta.parts[-1])
        destino_md_ruta = Path(destino_directorio_ruta, f'{nombre}.md')
        with open(destino_md_ruta, 'w') as puntero:
            puntero.write(content)
        # Entregar línea para la terminal
        return(str(destino_md_ruta)[len(str(self.config.salida_ruta)):])

    def __repr__(self):
        return('  ' * self.nivel + f'<Base> {self.relativo}')
