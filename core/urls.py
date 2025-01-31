from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import CoreViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'', CoreViewSet, basename='core')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]