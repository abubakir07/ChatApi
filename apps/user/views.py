from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.serializers import UserSerializer, UsersAnotherSerializer, CurrentUserSerializer
from apps.user.models import User
from apps.chat.models import Chat


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
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UsersAnotherSerializer

    def get_queryset(self):
        user_chats = Chat.objects.filter(Q(owner=self.request.user) | Q(companion=self.request.user))
        user_ids = [c.owner_id for c in user_chats] + [c.companion_id for c in user_chats]
        queryset = User.objects.exclude(id__in=user_ids)
        queryset = queryset.exclude(id=self.request.user.id)  # exclude the authenticated user
        return queryset

    @action(detail=False, methods=['get'])
    def users_without_chat(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class CurrentUserView(APIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CurrentUserSerializer

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
