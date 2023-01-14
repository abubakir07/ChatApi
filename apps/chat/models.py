from django.db import models

from apps.user.models import User


class Chat(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="sender"
    )
    companion = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="companion"
    )

    class Meta:
        verbose_name = 'chat'
        verbose_name_plural = 'Chats'

    def __str__(self):
        return f'owner: {self.owner}---companion: {self.companion}'


class Message(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='sender',
        related_name='message_sender',
        null=True,
    )
    text = models.CharField(
        max_length=500,
        blank=True
    )
    files = models.FileField(
        verbose_name='files',
        blank=True
    )
    chat_id = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        verbose_name='chat id',
        related_name="chats"
    )
    create_at = models.DateTimeField(
        verbose_name='create_at',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'Messages'
        ordering = ('-create_at',)

    def __str__(self):
        return f'sender: {self.sender}---message:{self.text}'
