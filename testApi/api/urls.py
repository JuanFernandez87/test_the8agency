from django.urls import path
from api import views

urlpatterns = [
    # Muestra el listado de los invitados al evento
    path('', views.inviteed_list, name='inviteed_list'),
    # Ruta para la creacion de un formulario con metodo POST
    path('inviteed/', views.InvitedView.as_view()),
]