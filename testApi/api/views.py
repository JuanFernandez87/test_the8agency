from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from .models import Invited
import json

# Create your views here.

class InvitedView(View):

    # Metodo que se ejecuta cada vez que hacemos una peticion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # Metodo POST para registrar a un invitado
    # http://127.0.0.1:8000/api/invitees/
    def post(self, request):
        jd = json.loads(request.body)
        Invited.objects.create(
                        name = jd['name'], 
                        last_name = jd['last_name'],
                        email = jd['email'],
                        country = jd['country'],
                        phone = jd['phone'],
                        job = jd['job']
        )
        datos = {'message': 'Sucess'}
        return JsonResponse(datos)

def list_inviteed(request):
    """
    Función vista para la página que muestra el listado de participantes al evento
    """
    # Ordeno alfabeticamente los participantes por appelido y por nombre
    inviteeds = Invited.objects.all().order_by('last_name', 'name')
    return render(request, 'list_inviteed.html', {'inviteeds': inviteeds})
