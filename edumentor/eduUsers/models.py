from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone = models.IntegerField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')
    background_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

