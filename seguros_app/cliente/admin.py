from django.contrib import admin
from cliente.models import Manager, Client
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','doc_id', 'phone')
    readonly_fields = ('created','updated')
    ordering = ('name',)

class ManagerAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('name','doc_id')

admin.site.register(Manager, ManagerAdmin)
admin.site.register(Client, ClientAdmin)
