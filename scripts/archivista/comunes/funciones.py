import re
import unicodedata


def cambiar_acentos(text):
    """ Cambia los caracteres acentuados a caracteres sin acentos """
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return(str(text))


def cambiar_a_ruta_segura(text):
    """ Crea una ruta segura en minúsculas, espacios a guiones y sin caracteres acentuados, pero mantiene diagonales """
    text = cambiar_acentos(text.lower())
    text = re.sub('[ ]+', '-', text)
    text = re.sub('[^0-9a-zA-Z_/-]', '', text)
    return(text)


def cambiar_a_identificador(text):
    """ Crea un identificador en minúsculas, guiones y sin caracteres acentuados """
    text = cambiar_acentos(text.lower())
    text = re.sub('[/]+', '-', text)
    text = re.sub('[ ]+', '-', text)
    text = re.sub('[^0-9a-zA-Z_-]', '', text)
    return(text)


def validar_rama(rama=''):
    """ Validar rama """
    return(rama.lower())
