from django.db.models import Q
from requests import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import get_object_or_404
from rest_framework import generics

from apps.chat.models import Message, Chat
from apps.chat.serializer import MessageSerializer, ChatSerializer, CreateChatSerializer, ChatDestroySerializer
from apps.chat.permissions import IsChatOwner, IsMassageToCreate, IsMessageOwner


class CreateChatView(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = CreateChatSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ChatListView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsChatOwner, )

    def get_queryset(self):
        return Chat.objects.filter(Q(owner=self.request.user) | Q(companion=self.request.user))


class ChatDetailView(generics.RetrieveDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsChatOwner, )


class CreateMessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsChatOwner,)

    def perform_create(self, serializer):
        return serializer.save(sender=self.request.user)


class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsMessageOwner, )

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        chat = get_object_or_404(Chat, pk=chat_id)
        return Message.objects.filter(chat_id=chat)


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsMessageOwner, )
