from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.

class User(AbstractUser):
    
    def upload_to(instance, filename):
        return '{datetime}{filename}'.format(datetime=datetime.now(), filename=filename)

    profile_pic = models.ImageField(
        upload_to=upload_to, default='media\user.png')
    username = None
    USERNAME_FIELD = 'email'



    
    
