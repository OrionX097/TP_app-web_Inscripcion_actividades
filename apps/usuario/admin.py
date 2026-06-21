from django.contrib import admin

from apps.usuario.models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','dni')
    search_fields = ('nombre',)
    list_filter = ('dni','apellido',)
    ordering = ('apellido',)