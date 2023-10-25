from django.contrib import admin
from .models import UsuarioComum

@admin.register(UsuarioComum)
class UsuarioComumAdmin(admin.ModelAdmin):
    list_display= ('first_name', 'email', 'data_nasc', 'get_auth_token','username','is_active')

# Register your models here.
