from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.SlugField(verbose_name="Nombre", max_length=100)
    doc_id = models.CharField(verbose_name="Cedula", max_length=14)
    phone = models.CharField(verbose_name="Telefono", max_length=11)
    address = models.CharField(verbose_name="Direccion", max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        ordering = ["created"]
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name

class Manager(models.Model):
    name = models.SlugField(verbose_name="Gestor" )
    doc_id = models.CharField(verbose_name="Cedula", max_length=14)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        ordering = ["created"]
        verbose_name_plural = "Gestores"   
    
    def __str__(self):
        return self.name

