from pathlib import Path
from universales.descargable import Descargable


class SeccionDescargables(object):
    """ Seccion Descargables """

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
            # Buscar descargables
            items = []
            for extension in self.config.descargables_extensiones:
                items.extend(list(self.ruta.glob(f'*.{extension}')))
            # ¿Hay o no hay?
            if len(items) > 0:
                self.contenidos = []
                for item in items:
                    descargable = Descargable(self.config, item, self.nivel + 1)
                    if descargable.alimentar():
                        self.contenidos.append(descargable)
                self.mensaje = 'Descargar'
            else:
                self.contenidos = None
                self.mensaje = 'NO HAY DESCARGABLES'
            # Levantar la bandera
            self.ya_alimentado = True
        # Entregar verdadero si hay
        return(self.contenidos is not None)

    def contenido(self):
        """ Entregar el contenido que es texto markdown con las descargas """
        if self.contenidos is not None:
            lineas = []
            lineas.append(f'## {self.mensaje}')
            lineas.append('')
            lineas.extend(descargable.contenido() for descargable in self.contenidos)
            lineas.append('')
            return('\n'.join(lineas))
        else:
            return('SIN DESCARGABLES')  # Esto no debería entregarse

    def __repr__(self):
        lineas = []
        lineas.append(f'<SeccionDescargables> {self.mensaje}')
        if self.contenidos is not None:
            lineas.extend([repr(descargable) for descargable in self.contenidos])
        return('  ' * self.nivel + '\n'.join(lineas))
