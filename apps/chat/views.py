from .models import Message, Chat
from .serializer import MessageSerializer, ChatSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    get_object_or_404
)


class CreateMessageView(CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)


class MessageListView(ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        chat = get_object_or_404(Chat, pk=chat_id)
        return Message.objects.filter(chat=chat)


class MessageDetailView(RetrieveAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()


class MessageUpdateView(UpdateAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()


class MessageDestroyView(DestroyAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()


################################################################################


class CreateChatView(CreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        chat = serializer.save()
        chat.participants.add(self.request.user)
        chat.save()


class ChatListView(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Chat.objects.filter(participants=self.request.user)


class ChatDetailView(RetrieveAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Chat.objects.all()


class ChatUpdateView(UpdateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Chat.objects.all()


class ChatDestroyView(DestroyAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Chat.objects.all()
