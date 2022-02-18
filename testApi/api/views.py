from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Invited
import json

# Create your views here.

class InvitedView(View):

    # Metodo que se ejecuta cada vez que hacemos una peticion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # Metodo GET que devuelve la lista de invitados en formato JSON
    # http://127.0.0.1:8000/api/invitees/id
    def get(self, request, id=0):
        if id > 0:
            invited = list(Invited.objects.filter(id=id).values())
            if invited:
                datos = {'message': 'Sucess', 'invited': invited}
            else:
                datos = {'message': 'Invited not found for id...'}
            return JsonResponse(datos)        
        else:
            invitees = list(Invited.objects.values())
            if len(invitees) > 0:
                datos = {'message': 'Sucess', 'guests': invitees}
            else:   
                datos = {'message': 'Invitees not found...'}
            return JsonResponse(datos)

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

    # Metodo PUT para actualizar lo informacion de un invitado
    # http://127.0.0.1:8000/api/invitees/
    def put(self, request, id):
        jd = json.loads(request.body)
        invitees = list(Invited.objects.filter(id=id).values())
        if len(invitees) > 0:
            invited = Invited.objects.get(id=id)
            invited.name = jd['name'], 
            invited.last_name = jd['last_name'],
            invited.email = jd['email'],
            invited.country = jd['country'],
            invited.phone = jd['phone'],
            invited.job = jd['job']            
        else:
            datos = {'message': 'Invited not found...'}
        return JsonResponse(datos)

    # Metodo DELETE para eliminar a un invitado
    # http://127.0.0.1:8000/api/invitees/id
    def delete(self, request, id):
        invitees = list(Invited.objects.filter(id=id).values())
        if len(invitees) > 0:
            Invited.objects.get(id=id).delete()
            datos = {'message': 'Sucess'}
        else:            
            datos = {'message': 'Invited not found...'}
        return JsonResponse(datos)
