from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

class BaseModel(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
   


    class Meta:
        abstract = True


class UsuarioComum(AbstractUser, BaseModel):
    data_nasc = models.DateField(null=True)
    endereco = models.TextField(null=True)
     
    class Meta:
        verbose_name = 'Usuario-Comum'
        verbose_name_plural = 'Usuarios-Comuns'

    def get_auth_token(self):
        try:
            return Token.objects.get(user=self)
        except Token.DoesNotExist:
            return None

UsuarioComum._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
UsuarioComum._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_user_permissions'

