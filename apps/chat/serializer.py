from rest_framework import serializers

from .models import Message, Chat
from ..user.models import User


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'chat_id', 'sender', 'text', 'files', 'timestamp']
        read_only_fields = ('id', 'timestamp', 'sender', )


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name', 'owner', 'companion']
        read_only_fields = ('owner', 'name', )


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'age', 'bio', 'avatar', 'last_activity')
