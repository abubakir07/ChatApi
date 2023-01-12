from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework.decorators import api_view, permission_classes

from .serializers import UserSerializer, UsersAnotherSerializer
from .models import User
from ..chat.models import Chat


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.pk
        })


class UsersAnotherView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UsersAnotherSerializer

    def get(self, request):
        chats = Chat.objects.filter(sender=request.user) | Chat.objects.filter(receiver=request.user)
        user_ids = list(chats.values_list('sender', flat=True)) + list(chats.values_list('receiver', flat=True))
        user_ids.append(request.user.id)
        users = User.objects.exclude(id__in=user_ids)
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)
