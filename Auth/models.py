from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# AbstractUser

# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_("email address"), unique=True)
#     text = models.CharField(max_length=25)
#     name = models.CharField(max_length=45)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ['text']

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email


# AbstractBaseUser

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['text', 'first_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
