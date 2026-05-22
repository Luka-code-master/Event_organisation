from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ORGANIZER = 'organizer'
    ATTENDEE = 'attendee'
    ROLE_CHOICES = [
        (ORGANIZER, 'Organizer'),
        (ATTENDEE, 'Attendee'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.username