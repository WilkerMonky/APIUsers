from django.contrib import admin
from .models import UsuarioComum

from rest_framework.authtoken.models import Token
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext as _



def user_auth_token(obj):
    # Obtém o token de autenticação do usuário, se existir
    token = Token.objects.filter(user=obj).first()
    if token:
        return token.key
    return "N/A"

user_auth_token.short_description = 'Auth Token'

@admin.register(UsuarioComum)
class UsuarioComumAdmin(UserAdmin):
    
    list_display= ('username','first_name', 'email', 'data_nasc', user_auth_token,'is_active')

# Register your models here.
