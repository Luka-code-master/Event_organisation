import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from events.models import Event

User = get_user_model()


@pytest.fixture

def organizer(db):
    return User.objects.create_user(
        username='organizer1',
        password='pass1234',
        role='organizer'
    )


@pytest.fixture

def attendee(db):
    return User.objects.create_user(
        username='attendee1',
        password='pass1234',
        role='attendee'
    )


@pytest.fixture

def api_client():
    return APIClient()


@pytest.fixture

def event(db, organizer):
    return Event.objects.create(
        title='Test Event',
        description='Test',
        organizer=organizer,
        status='published',
        event_type='online',
        max_attendees=10,
        start_date='2025-12-01T10:00:00Z',
        end_date='2025-12-01T18:00:00Z'
    )