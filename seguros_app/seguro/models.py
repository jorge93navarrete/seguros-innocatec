from django.db import models
from cliente.models import Client, Manager

# Create your models here.

class Seguro(models.Model):
    client = models.ForeignKey(Client, related_name='cliente', blank=True, null=True, on_delete=models.SET_NULL)
    manager = models.ForeignKey(Manager, related_name='gestor',blank=True, null=True, on_delete=models.SET_NULL)
    poliza = models.IntegerField(verbose_name="Numero de poliza")
    date = models.DateTimeField(verbose_name="Vigencia - Inicia")
    expire = models.DateTimeField(verbose_name="Vigente - Finaliza")
    time = models.TimeField(verbose_name="Hora")
    
    
    created = models.DateTimeField(auto_now_add=True,  verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")