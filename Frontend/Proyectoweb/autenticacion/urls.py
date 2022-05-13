from django.urls import path

from .views import VRegistro, cerrar_session, logear

#as_view => muestra la clase como una vista
urlpatterns = [
    path('', VRegistro.as_view(), name='Autenticacion'),
    path('cerrar_session', cerrar_session, name='cerrar_session'),
    path('logear', logear, name='logear'),
]

