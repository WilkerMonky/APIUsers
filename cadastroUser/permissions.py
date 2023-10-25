"""
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import UsuarioComum
from django.contrib.auth.models import Group


content_type = ContentType.objects.get_for_model(UsuarioComum)
permission, created = Permission.objects.get_or_create(
    codename='can_login',
    name='Can login',
    content_type=content_type,
)


user_group, created = Group.objects.get_or_create(name='Usuário Comum')
permission = Permission.objects.get(codename='can_login')
user_group.permissions.add(permission)
"""