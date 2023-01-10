from django.db import models

from apps.user.models import User


class Chat(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                              null=True, related_name="sender")
    companion = models.ForeignKey(User, on_delete=models.SET_NULL,
                                  null=True, related_name="companion")

    class Meta:
        verbose_name = 'chat'
        verbose_name_plural = 'Chats'

    def __str__(self):
        return


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True, related_name='message_sender')
    text = models.CharField(max_length=500, blank=True)
    files = models.FileField(blank=True)
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE,
                                related_name="chat_id")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'Messages'
        ordering = ('-timestamp',)

    def __str__(self):
        return f'sender: {self.sender}---message:{self.text}'
