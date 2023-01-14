from rest_framework import permissions

from apps.chat.models import Message, Chat


class IsChatOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsMessageOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        room = Chat.objects.get(id=obj.chat_id.id)
        if room.companion == request.user or room.owner == request.user:
            return True
        else:
            return False


class IsMassageToCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        id = view.kwargs.get('pk')
        chat = Chat.objects.get(id=id)
        return chat.owner == request.user or chat.companion == request.user
