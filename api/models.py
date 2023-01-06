from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField()
    email = models.EmailField()


class Note(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)