from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import AdViewSet, CommentViewSet

ads_router = SimpleRouter()

ads_router.register(prefix='ads', viewset=AdViewSet, basename='ads')
ads_router.register(prefix=r'ads/(?P<ad_pk>[0-9]+)/comments', viewset=CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(ads_router.urls)),
]
