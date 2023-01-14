from rest_framework import serializers

from .models import Message, Chat


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'chat_id', 'sender', 'text', 'files', 'create_at']
        read_only_friends = ('id', 'create_at', 'sender',)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'chat_id', 'sender', 'text', 'files', 'create_at']
        read_only_fields = ('id', 'create_at', 'chat_id', 'sender',)


class CreateChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'owner', 'companion')
        read_only_fields = ('owner',)

    def create(self, validated_data):
        companion = validated_data['companion']
        if Chat.objects.filter(owner=self.context['request'].user, companion=companion).exists():
            raise serializers.ValidationError("Chat already exists.")
        return Chat.objects.create(**validated_data)


class ChatDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'owner', 'companion']
        read_only_fields = ('owner',)


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'owner', 'companion']
        read_only_fields = ('owner',)

    def validate(self, data):
        owner = data['owner']
        request_user = self.context['request'].user
        if owner != request_user and not request_user.is_staff:
            raise
