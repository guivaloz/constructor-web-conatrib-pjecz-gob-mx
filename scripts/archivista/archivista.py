import click
import sys
from comunes.config import pass_config
from comunes.funciones import validar_rama
from universales.rama import Rama


@click.group()
@click.option('--rama', default='Transparencia', type=str, help='Directorio de insumos configurado en settings.ini')
@pass_config
def cli(config, rama):
    click.echo('Hola, ¡soy Archivista!')
    try:
        config.rama = validar_rama(rama)
        config.cargar_configuraciones()
        config.validar_configuraciones()
    except Exception as e:
        click.echo(str(e))
        sys.exit(1)


@cli.command()
@pass_config
def mostrar(config):
    """ Mostrar en pantalla directorios y archivos que puede crear """
    click.echo(f'Voy a mostrar {config.insumos_ruta}')
    rama = Rama(config)
    rama.alimentar()
    click.echo(repr(rama))
    sys.exit(0)


@cli.command()
@pass_config
def crear(config):
    """ Crear directorios y archivos """
    click.echo('Voy a crear...')
    sys.exit(0)


cli.add_command(mostrar)
cli.add_command(crear)
