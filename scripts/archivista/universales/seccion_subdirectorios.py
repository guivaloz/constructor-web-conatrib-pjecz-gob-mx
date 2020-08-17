from pathlib import Path
from universales.subdirectorio import Subdirectorio


class SeccionSubdirectorios(object):
    """ Seccion Subdirectorios """

    def __init__(self, config, ruta, nivel):
        self.config = config
        if isinstance(ruta, str):
            self.ruta = Path(ruta)
        else:
            self.ruta = ruta
        self.nivel = nivel
        self.ya_alimentado = False
        self.contenidos = None
        self.mensaje = 'NO ALIMENTADO'

    def rastrear_directorios(self, ruta, nivel):
        """ Rastrear directorios """
        for item in ruta.glob('*'):
            if item.is_dir():
                # Si tiene dentro un archivo <directorio>.md se omite
                nombre = item.parts[-1]
                posible_md_ruta = Path(self.ruta, nombre, f'{nombre}.md')
                if not(posible_md_ruta.exists() and posible_md_ruta.is_file()):
                    # Ser recursivo
                    yield (item, nivel)
                    yield from self.rastrear_directorios(item, nivel + 1)

    def alimentar(self):
        if self.ya_alimentado is False:
            # Rastrear subdirectorios
            subdirectorios = []
            for item, nivel in self.rastrear_directorios(self.ruta, self.nivel + 1):
                subdirectorio = Subdirectorio(self.config, item, nivel)
                subdirectorio.alimentar()
                subdirectorios.append(subdirectorio)
            # ¿Hay o no hay?
            if len(subdirectorios) > 0:
                self.contenidos = subdirectorios
                self.mensaje = ''
            else:
                self.contenidos = None
                self.mensaje = 'NO HAY SUBDIRECTORIOS'
            # Levantar la bandera
            self.ya_alimentado = True

    def contenido(self):
        return('Hola Mundo!')

    def __repr__(self):
        lineas = [f'<SeccionSubdirectorios> {self.mensaje}']
        if self.contenidos is not None:
            lineas += [repr(contenido) for contenido in self.contenidos]
        return('  ' * self.nivel + '\n'.join(lineas))
