from django.db import models

# Create your models here.


class Nombre(models.Model):
    Nombre = models.CharField(max_length=40)
    dni = models.IntegerField()