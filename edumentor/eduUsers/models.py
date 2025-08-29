from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone = models.IntegerField(null=True, blank=True)

    # Profile picture (stored inside "media/profile_pic/")
    image = models.ImageField(
        upload_to='profile_pic/',
        default='profile_pic/default.jpg'
    )

    # Optional background image (stored inside "media/backgrounds/")
    background_image = models.ImageField(
        upload_to='backgrounds/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """
        Override save method to resize images after saving.
        Prevents errors if default.jpg is missing.
        """
        super().save(*args, **kwargs)

        # Resize profile picture if it exists and is not missing
        if self.image and os.path.exists(self.image.path):
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

        # Resize background image if it exists and is not missing
        if self.background_image and os.path.exists(self.background_image.path):
            bg_img = Image.open(self.background_image.path)
            if bg_img.height > 800 or bg_img.width > 1200:
                output_size = (1200, 800)
                bg_img.thumbnail(output_size)
                bg_img.save(self.background_image.path)
