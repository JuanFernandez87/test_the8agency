from django.contrib import admin
from .models import Invited

# Register your models here.

admin.site.register(Invited)

# @admin.register(Invited)
# class InvitedAdmin(admin.ModelAdmin):
#       # pagino la lista
#     list_per_page = 10
