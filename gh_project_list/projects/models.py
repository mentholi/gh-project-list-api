from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.send_webhook import send_webhooks
from django.core.validators import MaxValueValidator, MinValueValidator


class Project(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link = models.CharField(max_length=2048)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


@receiver(post_save, sender=Project, dispatch_uid="send_webhooks_task")
def send_new_project_webhooks(sender, instance, **kwargs):
    """
    Trigger background tasks to send webhooks
    """
    send_webhooks.send(instance.id)
