from pathlib import Path


class Descargable(object):
    """ Descargable """

    def __init__(self, config, ruta):
        self.config = config
        self.ruta = ruta
        # Definir nombre del descargable
        descargable_ruta = Path(self.ruta)
        self.nombre = descargable_ruta.name

    def vinculo(self):
        """ Entregar el vínculo de este descargable en Google Cloud """
        relativo = self.ruta[len(self.config.nextcloud_ruta):]
        url = self.config.almacen_frio_url + relativo
        return(url)

    def __repr__(self):
        return(f'<Descargable> {self.nombre}')
