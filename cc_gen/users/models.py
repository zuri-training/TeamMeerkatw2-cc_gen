from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=400, null=True)
    image = models.ImageField(
        default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'
    