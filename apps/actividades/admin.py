from django.contrib import admin

from apps.actividades.models import Actividad

# Register your models here.
@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dias', 'horario')
    search_fields = ('nombre',)
    list_filter = ('dias','horario',)
    ordering = ('nombre',)