from universales.base import Base


class Pagina(Base):
    """ Pagina """

    def __init__(self, config, ruta, nivel):
        super().__init__(config, ruta)
        self.nivel = nivel

    def alimentar(self):
        """ Alimentar """
        super().alimentar()
        if self.ya_alimentado is False:
            # Levantar bandera
            self.ya_alimentado = True

    def __repr__(self):
        lineas = [f'<Pagina> {self.relativo}']
        if len(self.secciones) > 0:
            lineas += [repr(seccion) for seccion in self.secciones]
        return('  ' * self.nivel + '\n'.join(lineas))
