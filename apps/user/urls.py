from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.user.views import (
        UserRegisterAPIView,
        UsersAnotherView,
        CurrentUserView
    )

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', UserRegisterAPIView.as_view(), name='register'),

    path('users-another/', UsersAnotherView.as_view(), name='users_another'),
    path('current-user/', CurrentUserView.as_view(), name='current_user'),

]
