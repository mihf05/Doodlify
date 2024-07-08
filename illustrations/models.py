from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostDoodle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/', blank=False, null=False)
    text = models.TextField(max_length=40)

def __str__(self):
    return f'{self.user.username} - {self.text[:10]}'
