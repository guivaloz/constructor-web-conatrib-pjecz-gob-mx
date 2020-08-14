
class Seccion(object):
    """ Seccion """

    def __init__(self, config, archivo_md_ruta):
        self.config = config
        self.archivo_md_ruta = archivo_md_ruta
        # Definir el encabezado
        self.encabezado = self.archivo_md_ruta.parts[-1]

    def contenido(self):
        lineas = []
        if self.archivo_md_ruta.exists() and self.archivo_md_ruta.is_file():
            with open(self.archivo_md_ruta, 'r') as f:
                lineas.append(f.read())
        return('\n'.join(lineas))

    def __repr__(self):
        return(f'<Seccion> {self.encabezado}')
