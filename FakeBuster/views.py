from django.shortcuts import render
from django.http import HttpResponse
from . import principal, principalURL

# Create your views here.
def mostrar_valor(request):
    if request.method == 'POST':
        form_id = request.POST.get('form_id')

        if form_id == 'formularioID':
            url = request.POST.get('url')
            autor, titulo, fecha = principalURL.obtener_datos_articulo(url)
            
            if None in (autor, titulo, fecha):
                return render(request, 'index.html')
            else:
                informacionAutor = principal.buscarInformacionDelAutor(autor)
                informacionTitulo = principal.buscarInformacionDelTitulo(titulo)
                informacionFecha = principal.buscarinformacionDeLaFecha(fecha, titulo)

                return render(request, 'respuesta.html', {
                    'valorAutor': informacionAutor,
                    'valorTitulo': informacionTitulo,
                    'valorFecha': informacionFecha
                })
        else:
            autor = request.POST.get('autor')
            titulo = request.POST.get('titulo')
            fecha = request.POST.get('fecha')

            informacionAutor = principal.buscarInformacionDelAutor(autor)
            informacionTitulo = principal.buscarInformacionDelTitulo(titulo)
            informacionFecha = principal.buscarinformacionDeLaFecha(fecha, titulo)

            return render(request, 'respuesta.html', {
                'valorAutor': informacionAutor,
                'valorTitulo': informacionTitulo,
                'valorFecha': informacionFecha
            })
    return render(request, 'index.html')
