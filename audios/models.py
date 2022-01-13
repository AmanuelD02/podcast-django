from email.policy import default
import imp
from django.db import models
from datetime import datetime
import uuid
from django.db.models.deletion import CASCADE
from users.models import User
from channels.models import Channel

def upload_to(instance, filename):
    return '{datetime}{filename}'.format(datetime=datetime.now(), filename=filename)
# Create your models here.
class Audio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=True,blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE, unique=False)
    title = models.CharField(max_length=255)
    Description = models.TextField()
    path = models.FileField(upload_to=upload_to)
    poster = models.ImageField(upload_to=upload_to,default='media\default-user.png')    