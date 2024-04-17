from . import palm
from datetime import datetime

def buscarInformacionDelTitulo(titulo):
    if not titulo:
        return "No ha insertado ningún título, por favor inserte el título de la noticia"
    
    informacionTitulo = f"Por favor, verifica si es cierto o falso y explícame este título de una noticia '{titulo}'"  
    return palm.buscarInformacion(informacionTitulo)

def buscarInformacionDelAutor(autor):
    if not autor or autor.lower() == "ninguno":
        return "Es posible que su noticia sea falsa, recomendamos verificar la veracidad de la noticia"

    informacionAutor = f"Dame información sobre este autor, empresa, escritor o periodista: {autor}"   
    return palm.buscarInformacion(informacionAutor)

def buscarinformacionDeLaFecha(fecha, titulo):
    if not fecha and not titulo:
        return "No se insertó ningún campo, por favor inserte los campos para poder analizar su noticia"
    
    if not fecha:
        return "Si no se encuentra la fecha en su noticia, posiblemente sea falsa. Por favor, verifique la noticia"

    if not titulo:
        return "Faltó insertar el título de la noticia"
    
    informacionFecha = f"¿Podrías verificar la autenticidad del siguiente evento: '{titulo}'? Además, necesito confirmar si sucedió en la fecha especificada: {fecha}. En caso de que sea verídico, ¿me proporcionarías más detalles sobre lo acontecido? Si resulta ser falso, ¿podrías explicarme las razones detrás de esta conclusión?"  
    return palm.buscarInformacion(informacionFecha)
