from datetime import datetime
from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
import uuid

def upload_to(instance, filename):
    return '{datetime}{filename}'.format(datetime=datetime.now(), filename=filename)

# Create your models here.
class Channel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    channel_name = models.CharField(max_length=255)
    description = models.TextField()
    subscriber = models.PositiveIntegerField(validators=[MinValueValidator(0)], default=0)
    profile_pic = models.ImageField(
        upload_to=upload_to, default='media\channel.png')
    rate = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)

class Subscribe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    channel_id = models.ForeignKey(Channel,on_delete=models.CASCADE)
    notification = models.BooleanField(null=True, default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['channel_id', 'user_id'], name='Subscribe')
        ]



@receiver(post_save, sender=Subscribe)
def calculate_subscriber(sender, instance, **kwargs):
    """
    This Function is called everytime there is a change in Rating table
    """
    channel_id = instance.channel_id
    total =  Subscribe.objects.filter(channel_id=channel_id).count()

    channel = Channel.objects.filter(id=channel_id.id).first()

    channel.subscriber = total
    channel.save()
