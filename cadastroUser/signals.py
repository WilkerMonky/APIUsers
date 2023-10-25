from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(m2m_changed, sender=User.groups.through)
def user_added_to_group(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == "post_add":
        for group_id in pk_set:
            group = instance.groups.filter(id=group_id).first()
            if group and group.name == "Clients":
                Token.objects.get_or_create(user=instance)
