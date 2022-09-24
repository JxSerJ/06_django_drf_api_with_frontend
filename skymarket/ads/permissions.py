from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions

from users.models import UserRoles


class AdPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        # if view.action in ['list']:
        #     return True

        if view.action in ['create', 'me']:
            return request.user.is_authenticated
        else:
            return True

        # if isinstance(request.user, AnonymousUser):
        #     return False

    def has_object_permission(self, request, view, instance):
        if isinstance(request.user, AnonymousUser):
            return False

        if view.action in ['list']:
            return True

        if view.action in ['retrieve', 'update', 'partial_update', 'destroy'] and \
                (request.user.role == UserRoles.ADMIN or instance.author == request.user):
            return True
        else:
            return False


class CommentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return False

        if view.action in ['create']:
            return request.user.is_authenticated
        else:
            return True

    def has_object_permission(self, request, view, instance):
        if isinstance(request.user, AnonymousUser):
            return False

        if view.action in ['list', 'retrieve']:
            return True

        if view.action in ['update', 'partial_update', 'destroy'] and \
                (request.user.role == UserRoles.ADMIN or instance.author == request.user):
            return True
        else:
            return False
