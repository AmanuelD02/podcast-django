from datetime import datetime
from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 



def upload_to(instance, filename):
    return '{datetime}{filename}'.format(datetime=datetime.now(), filename=filename)

# Create your models here.
class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    channel_name = models.CharField(max_length=255)
    description = models.TextField()

    profile_pic = models.ImageField(
        upload_to=upload_to, default='media\channel.png')
    rate = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)

class Subscribe(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    channel_id = models.ForeignKey(Channel,on_delete=models.CASCADE)
    notification = models.BooleanField(null=True, default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['channel_id', 'user_id'], name='Subscribe')
        ]





