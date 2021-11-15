from django.db.models.signals import post_delete, post_save
from .models import User, Profile

#! when user created profile will be created automatically
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            name = user.first_name,
            email = user.email,
            new_user = True
        )


#! when profile deleted user will be deleted automatically
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)