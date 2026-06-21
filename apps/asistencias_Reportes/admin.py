from django.contrib import admin

from apps.asistencias_Reportes.models import Listado

# Register your models here.
@admin.register(Listado)
class ListadoAdmin(admin.ModelAdmin):
    list_display = ('fecha_clase','asistencia')
    search_fields = ('fecha_clase',)
    list_filter = ('asistencia',)
    ordering = ('fecha_clase',)