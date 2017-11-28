from django.db.models.signals import post_save
from django.dispatch import receiver
from work_system.models import Personal
from django.contrib.auth.models import User
from .models import *


@receiver(post_save, sender=User)
def createHP(sender, instance, created, **kwargs):
    if created:
        HP.objects.create(user=instance)


@receiver(post_save, sender=Buff)
def increaseHP(sender, instance, created, **kwargs):
    if created:
        q = instance.key
        q.value += instance.hp_increase
        q.save()
        super(Buff, instance).save()


@receiver(post_save, sender=DeBuff)
def decreaseHP(sender, instance, created, **kwargs):
    if created:
        q = instance.key
        q.value -= instance.hp_decrease
        q.save()
        super(DeBuff, instance).save()

