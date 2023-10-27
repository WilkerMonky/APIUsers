from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save

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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

UsuarioComum._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
UsuarioComum._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_user_permissions'

