from pathlib import Path


class SeccionInicial(object):
    """ Seccion Inicial """

    def __init__(self, config, ruta):
        self.config = config
        if isinstance(ruta, str):
            self.ruta = Path(ruta)
        else:
            self.ruta = ruta
        self.ya_alimentado = False
        self.mensaje = 'NO ALIMENTADO'
        self.contenidos = None

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
        pass

    def __repr__(self):
        return(f'<SeccionInicial> {self.mensaje}')
