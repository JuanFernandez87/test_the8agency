from django.db import models

# Create your models here.

class Invited(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    country = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    job = models.CharField(max_length=30)
