from django.urls import path
from . import views

app_name = "FakeBuster"
urlpatterns = [
    path('', views.mostrar_valor, name='mostrar_valor')
]