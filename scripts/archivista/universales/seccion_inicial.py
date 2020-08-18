from pathlib import Path


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
            # Definir nombre del archivo md
            if self.ruta == self.config.insumos_ruta:
                archivo_md_nombre = '{}.md'.format(self.config.titulo)
            else:
                archivo_md_nombre = '{}.md'.format(self.ruta.parts[-1])
            archivo_md_ruta = Path(self.ruta, archivo_md_nombre)
            # ¿Existe o no?
            if archivo_md_ruta.exists() and archivo_md_ruta.is_file():
                self.contenidos = archivo_md_ruta
                self.mensaje = archivo_md_nombre
            else:
                self.contenidos = None
                self.mensaje = f'NO EXISTE {archivo_md_nombre}'
            # Levantar la bandera
            self.ya_alimentado = True

    def contenido(self):
        """ Entregar el contenido que es el markdown que está en el archivo """
        if self.contenidos is not None:
            with open(str(self.contenidos), 'r') as puntero:
                return(puntero.read())
        else:
            return('SIN CONTENIDO')  # Esto no debería entregarse

    def __repr__(self):
        return('  ' * self.nivel + f'<SeccionInicial> {self.mensaje}')
