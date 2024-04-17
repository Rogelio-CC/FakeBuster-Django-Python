from mtranslate import translate

# Diccionario para almacenar traducciones previas
cache_ingles = {}
cache_espanol = {}

def traducirAIngles(textoATraducir):
    if textoATraducir in cache_ingles:
        return cache_ingles[textoATraducir]
    else:
        try:
            textoTraducido = translate(textoATraducir, "en")
            cache_ingles[textoATraducir] = textoTraducido  # Almacenar la traducción en caché
            return textoTraducido
        except Exception as e:
            print(f"Error al traducir a inglés: {e}")
            return None  # Manejar el error devolviendo None o un mensaje de error

def traducirAEspañol(textoATraducir):
    if textoATraducir in cache_espanol:
        return cache_espanol[textoATraducir]
    else:
        try:
            textoTraducido = translate(textoATraducir, "es")
            cache_espanol[textoATraducir] = textoTraducido  # Almacenar la traducción en caché
            return textoTraducido
        except Exception as e:
            print(f"Error al traducir a español: {e}")
            return None  # Manejar el error devolviendo None o un mensaje de error
