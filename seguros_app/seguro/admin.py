from django.contrib import admin
from seguro.models import Seguro

class SeguroAdmin(admin.ModelAdmin):
    list_display = ('poliza','client', 'date')
    readonly_fields = ('created','updated')
    list_filter = ('poliza', 'client__name')
    search_fields = ('poliza', 'client__name')
    ordering = ('created',)
    fieldsets = (
        ('Gestor y cliente', {'fields': ('client','manager')}),
        ('Datos de poliza', {'fields': ('poliza','date','expire', 'time')})
    )


admin.site.register(Seguro, SeguroAdmin)