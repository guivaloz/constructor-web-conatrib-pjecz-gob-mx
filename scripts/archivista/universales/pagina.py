from universales.base import Base


class Pagina(Base):
    """ Pagina """

    def __init__(self, config, ruta):
        super().__init__(config, ruta)

    def alimentar(self):
        """ Alimentar """
        super().alimentar()
        if self.ya_alimentado is False:
            # Levantar la bandera
            self.ya_alimentado = True

    def contenido(self):
        """ Elaborar contenido """
        return('Contenido pendiente.')

    def __repr__(self):
        if self.ya_alimentado:
            lineas = []
            if self.existe_archivo_md():
                lineas += [f'<Pagina> {self.archivo_md_nombre}']
            else:
                lineas += ['<Pagina>']
            if len(self.contenidos_iniciales) > 0:
                lineas += ['    ' + repr(contenido) for contenido in self.contenidos_iniciales]
            if len(self.contenidos_centrales) > 0:
                lineas += ['    ' + repr(contenido) for contenido in self.contenidos_centrales]
            return('\n'.join(lineas))
        else:
            return('<Pagina> No se ha alimentado')
