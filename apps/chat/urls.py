from django.urls import path

from .views import *

urlpatterns = [
    # For Messages
    path('chats/<int:chat_id>/messages/', MessageListView.as_view(), name='get_messages'),
    path('chats/<int:chat_id>/messages/create/', CreateMessageView.as_view(), name='create_message'),
    path('chats/<int:chat_id>/messages/<int:pk>/', MessageDetailView.as_view(), name='get_message'),
    path('chats/<int:chat_id>/messages/<int:pk>/update/', MessageUpdateView.as_view(), name='update_message'),
    path('chats/<int:chat_id>/messages/<int:pk>/delete/', MessageDestroyView.as_view(), name='delete_message'),

    # For Chat
    path('chats/', ChatListView.as_view(), name='get_chats'),
    path('chats/create/', CreateChatView.as_view(), name='create_chat'),
    path('chats/<int:pk>/', ChatDetailView.as_view(), name='get_chat'),
    path('chats/<int:pk>/update/', ChatUpdateView.as_view(), name='update_chat'),
    path('chats/<int:pk>/delete/', ChatDestroyView.as_view(), name='delete_chat'),
]