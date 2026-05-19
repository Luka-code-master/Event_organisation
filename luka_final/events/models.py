from django.db import models
from django.conf import settings
from django.db.models import Count, Avg

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
        (CANCELLED, 'Cancelled')
    ]

    ONLINE = 'online'
    OFFLINE = 'offline'
    TYPE_CHOICES = [
        (ONLINE, 'Online'),
        (OFFLINE, 'Offline')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    event_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    max_attendees = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Registration(models.Model):
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (CANCELLED, 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user} -> {self.event}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user} review {self.event}"

class EventMedia(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='media')
    file = models.ImageField(upload_to='event_media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)