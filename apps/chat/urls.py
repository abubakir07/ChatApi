from django.urls import path

from apps.chat.views import (
    CreateMessageView,
    MessageListView,
    MessageDetailView,
    ChatListView,
    CreateChatView,
    ChatDetailView
)


urlpatterns = [
    # For Messages
    path('<int:chat_id>/messages/', MessageListView.as_view(), name='get_messages'),
    path('<int:chat_id>/message/create/', CreateMessageView.as_view(), name='create_message'),
    path('<int:chat_id>/message/<int:pk>/', MessageDetailView.as_view(), name='detail_message'),

    # For Chat
    path('list/', ChatListView.as_view(), name='get_chats'),
    path('create/', CreateChatView.as_view(), name='create_chat'),
    path('<int:pk>/', ChatDetailView.as_view(), name='detail_chat'),
]
