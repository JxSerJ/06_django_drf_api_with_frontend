from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import AdViewSet

ads_router = SimpleRouter()

ads_router.register(prefix='ads', viewset=AdViewSet, basename='ads')

urlpatterns = [
    path('', include(ads_router.urls)),
]
