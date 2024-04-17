import google.generativeai as palm
from . import traductor

palm.configure(api_key='api key') #Sustituir por la verdader api key que te ofrece Google developer

generate_text_model = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods][0].name

def buscarInformacion(texto):
    textoTraducidoAlIngles = traductor.traducirAIngles(texto)
    
    prompt = textoTraducidoAlIngles

    completion = palm.generate_text(
        model=generate_text_model,
        prompt=prompt,
        temperature=0,
        max_output_tokens=800,
    )
    
    textoTraducidoAlEspañol = traductor.traducirAEspañol(completion.result)

    return textoTraducidoAlEspañol
