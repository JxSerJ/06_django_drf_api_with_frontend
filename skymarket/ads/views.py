from rest_framework import pagination, viewsets, status
from rest_framework.response import Response

from .models import Ad, Comment
from .permissions import CommentPermission, AdPermission
from .serializers import AdListSerializer, AdSerializer, CommentSerializer, CommentCreateSerializer


class AdPagination(pagination.PageNumberPagination):
    pass


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    permission_classes = [AdPermission]

    def create(self, request, *args, **kwargs):
        self.check_permissions(request)
        serializer = AdSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AdSerializer(instance, many=False)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = AdSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]

    # lookup_url_kwarg = "ad_pk"
    # lookup_field = "ad_id"

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs['ad_pk'])

    def create(self, request, *args, **kwargs):
        self.check_permissions(request)
        serializer = CommentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        ad = Ad.objects.get(pk=self.kwargs['ad_pk'])
        serializer.save(author=self.request.user, ad=ad)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = CommentSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
