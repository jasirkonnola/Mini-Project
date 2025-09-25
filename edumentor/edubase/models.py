from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    CATEGORY_CHOICES = [
        ('math', 'Mathematics'),
        ('science', 'Science'),
        ('history', 'History'),
        ('tech', 'Technology'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - Question'
    
    def get_absolute_url(self):
        return reverse('edubase:question-detail', kwargs={'pk': self.pk})