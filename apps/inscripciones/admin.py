from django.contrib import admin

from apps.inscripciones.models import Inscripcion

# Register your models here.
@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('fecha_inscripcion', 'estado')
    search_fields = ('fecha_inscripcion',)
    list_filter = ('estado',)
    ordering = ('fecha_inscripcion',)