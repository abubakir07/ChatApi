from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    username = models.CharField(
        verbose_name='username',
        unique=True,
        max_length=255
    )
    image = models.ImageField(
        upload_to='user_image/',
        verbose_name='User_image',
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name="email",
        unique=True
    )
    phone_regex = RegexValidator(
        regex=r"^\+996\d{9}$",
        message="Phone number must be entered in the format: '+996123456789'."
    )
    phone_number = models.CharField(
        verbose_name="phone_number",
        validators=[phone_regex],
        max_length=17,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name="created_at",
        auto_now_add=True
    )
    age = models.PositiveIntegerField(
        verbose_name='age',
        blank=True,
        null=True
    )
    bio = models.TextField(
        verbose_name="bio"
    )
    last_activity = models.DateTimeField(
        default=timezone.now,
        verbose_name="last_activity",
    )

    class Meta:
        verbose_name = "user"
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'Nickname: {self.username}'
