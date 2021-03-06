from pathlib import Path
from universales.archivo_md_inicial import ArchivoMdInicial
from universales.indice import Indice


class SeccionInicial(object):
    """ Seccion Inicial """

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

    def alimentar(self):
        """ Alimentar """
        if self.ya_alimentado is False:
            # Intentar encontrar archivo md inicial
            archivo = ArchivoMdInicial(self.config, self.ruta, self.nivel + 1)
            if archivo.alimentar():
                # Contenido es el archivo.md
                self.contenidos = archivo
                self.mensaje = archivo.archivo_md_nombre
            else:
                # Intentar crear un índice de los archivos.md en los subdirectorios
                indice = Indice(self.config, self.ruta, self.nivel + 1)
                if indice.alimentar():
                    # Contenido es el índice
                    self.contenidos = indice
                    self.mensaje = 'Índice con {} vínculos'.format(len(indice.vinculos))
                else:
                    # No hay contenido :(
                    self.contenidos = None
                    self.mensaje = f'NO EXISTE ARCHIVO MD'
            # Levantar la bandera
            self.ya_alimentado = True
        # Entregar verdadero si hay
        return(self.contenidos is not None)

    def contenido(self):
        """ Entregar el contenido que es el markdown que está en el archivo """
        if self.contenidos is not None:
            return(self.contenidos.contenido())
        else:
            return('SIN CONTENIDO')  # Esto no debería entregarse

    def __repr__(self):
        lineas = []
        lineas.append(f'<SeccionInicial> {self.mensaje}')
        if self.contenidos is not None:
            lineas.append(repr(self.contenidos))
        return('  ' * self.nivel + '\n'.join(lineas))
