from django.urls import path
from .views import InvitedView

urlpatterns = [
    path('invitees/', InvitedView.as_view(), name='invitees'),
    path('invitees/<int:id>', InvitedView.as_view(), name='invitees_process')    
]