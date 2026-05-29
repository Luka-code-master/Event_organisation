from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from accounts.views import RegisterView, MeView

from events.models import (
    EventViewSet,
    RegistrationViewSet,
    ReviewViewSet,
    CategoryViewSet,
    TagViewSet,
    EventMediaViewSet,
)

router = DefaultRouter()
router.register('events', EventViewSet)
router.register('categories', CategoryViewSet)
router.register('tags', TagViewSet)

nested_router = NestedDefaultRouter(router, 'events', lookup='event')
nested_router.register('registrations', RegistrationViewSet)
nested_router.register('reviews', ReviewViewSet)
nested_router.register('media', EventMediaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/register/', RegisterView.as_view()),
    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/token/refresh/', TokenRefreshView.as_view()),
    path('api/auth/me/', MeView.as_view()),

    path('api/', include(router.urls)),
    path('api/', include(nested_router.urls)),

    path('api/schema/', SpectacularAPIView.as_view()),

    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema')
    ),
]