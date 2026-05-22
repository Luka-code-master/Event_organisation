from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.cache import cache
from .models import Event, Category, Tag, Registration, Review, EventMedia
from .serializers import EventSerializer, CategorySerializer, TagSerializer, RegistrationSerializer, ReviewSerializer, EventMediaSerializer
from .permissions import Is_organizer, IsOwnerOrReadOnly, Is_confirmed_attendee
from accounts import models

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    @action(detail=False, methods=['get'])
    def stats(self, request):
        CACHE_KEY = 'events_stats'
        cached = cache.get(CACHE_KEY)
        if cached:
            return Response(cached)

        total_events = Event.objects.count()
        published_events = Event.objects.filter(status='published').count()
        total_registrations = Registration.objects.count()
        events_by_status = dict(Event.objects.values('status').annotate(count=models.Count('id')).values_list('status', 'count'))

        top_events = Event.objects.annotate(reg_count=models.Count('registrations'), avg_rating=models.Avg('reviews__rating')) \
            .order_by('-reg_count')[:5].values('id', 'title', 'reg_count', 'avg_rating')

        data = {
            "total_events": total_events,
            "published_events": published_events,
            "total_registrations": total_registrations,
            "events_by_status": events_by_status,
            "top_events": list(top_events)
        }
        cache.set(CACHE_KEY, data, timeout=300)
        return Response(data)