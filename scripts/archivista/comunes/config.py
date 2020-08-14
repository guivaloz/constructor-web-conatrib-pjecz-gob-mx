import click
import configparser
from pathlib import Path


class Config(object):

    def __init__(self):
        self.rama = ''
        self.almacen_frio_url = ''
        self.descargables_extensiones = []
        self.fecha_por_defecto = ''
        self.imagenes_extensiones = []
        self.pelican_ruta = ''
        self.nextcloud_ruta = ''
        self.titulo = ''
        self.insumos_ruta = ''
        self.salida_ruta = ''

    def cargar_configuraciones(self):
        """ Cargar configuraciones en settings.ini """
        if self.rama == '':
            raise Exception('ERROR: Faltó definir la rama.')
        settings = configparser.ConfigParser()
        settings.read('settings.ini')
        try:
            self.almacen_frio_url = settings['global']['almacen_frio']
            self.descargables_extensiones = settings['global']['descargables_extensiones'].split(',')
            self.fecha_por_defecto = settings['global']['fecha_por_defecto']
            self.imagenes_extensiones = settings['global']['imagenes_extensiones'].split(',')
            self.pelican_ruta = settings['global']['pelican_ruta']
            self.nextcloud_ruta = settings['global']['nextcloud_ruta']
            self.titulo = settings[self.rama]['titulo']
        except KeyError:
            raise Exception(f'ERROR: Falta configuración en settings.ini para la rama {self.rama}')

    def validar_configuraciones(self):
        """ Validar configuraciones """
        # Validar la ruta de insumos desde Archivista
        self.insumos_ruta = Path(f'{self.nextcloud_ruta}/{self.titulo}')
        if not self.insumos_ruta.exists() or not self.insumos_ruta.is_dir():
            raise Exception('ERROR: No existe el directorio de insumos {}'.format(str(self.insumos_ruta)))
        # Validar la ruta contents donde se crearán los archivos que usará Pelican
        self.salida_ruta = Path(f'{self.pelican_ruta}/content')
        if not self.salida_ruta.exists() or not self.salida_ruta.is_dir():
            raise Exception('ERROR: No existe el directorio de salida {}'.format(str(self.salida_ruta)))


pass_config = click.make_pass_decorator(Config, ensure=True)
