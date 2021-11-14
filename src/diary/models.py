from django.db import models
import uuid
import datetime

from users.models import Profile

class Diary(models.Model):
    MOOD_TYPE = {
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
    }
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    diary = models.TextField(null=True, blank=True)
    mood = models.CharField(max_length=200, choices=MOOD_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return datetime.datetime.strftime(self.created, "%d-%B-%Y %A")
