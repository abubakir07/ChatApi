from .models import Message, Chat
from .serializer import MessageSerializer, ChatSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

class CreateMessageView(CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)


from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

class MessageListView(ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        chat = get_object_or_404(Chat, pk=chat_id)
        return Message.objects.filter(chat=chat)
    

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

class MessageDetailView(RetrieveAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()


from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

class MessageUpdateView(UpdateAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()


from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

class MessageDestroyView(DestroyAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()






################################################################################


from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

class CreateChatView(CreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        chat = serializer.save()
        chat.participants.add(self.request.user)
        chat.save()


from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

class ChatListView(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Chat.objects.filter(participants=self.request.user)
    
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

class ChatDetailView(RetrieveAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Chat.objects.all()

from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

class ChatUpdateView(UpdateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Chat.objects.all()

from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

class ChatDestroyView(DestroyAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Chat.objects.all()