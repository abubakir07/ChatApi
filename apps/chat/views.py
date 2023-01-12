from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Message, Chat
from .serializer import MessageSerializer, ChatSerializer, CurrentUserSerializer
from .permissions import IsOwner, IsOwnerOrReadOnly
from ..user.models import User


class CreateMessageView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)


class MessageListView(ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        chat = get_object_or_404(Chat, pk=chat_id)
        return Message.objects.filter(chat=chat)


class MessageDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Message.objects.all()


class MessageUpdateView(UpdateAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    queryset = Message.objects.all()


class MessageDestroyView(DestroyAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    queryset = Message.objects.all()


class CreateChatView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        if not isinstance(self.get_serializer_class(), ChatSerializer):
            raise ValueError("Incorrect serializer class specified")
        chat = serializer.save()
        chat.companion = self.request.user
        chat.save()


class ChatListView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Chat.objects.filter(participants=self.request.user)


class ChatDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class ChatDestroyView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class CurrentUserView(APIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CurrentUserSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
