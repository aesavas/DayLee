from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True, unique=True,)
    username = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to='profiles/', default='profiles/avatar.svg')
    secret_key = models.BinaryField(max_length=256, blank=True, null=True)
    master_password = models.CharField(max_length=256, blank=True, null=True)
    new_user = models.BooleanField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return f'{self.name} --> {self.username} --> {datetime.datetime.strftime(self.created, "%d-%B-%Y %A")}'
