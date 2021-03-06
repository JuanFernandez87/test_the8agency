from django.db import models

# Create your models here.

class Invited(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    country = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    job = models.CharField(max_length=30)

    def __str__(self):
        return self.email