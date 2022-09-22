from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class UserRoles:
    ADMIN = "admin"
    USER = "user"

    ROLES = [
        (ADMIN, ADMIN),
        (USER, USER)
    ]


class User(AbstractBaseUser):
    first_name = models.CharField(_("first name"), max_length=150, null=True)
    last_name = models.CharField(_("last name"), max_length=150, null=True)
    phone = models.CharField(_("phone number"), max_length=20, null=True)
    email = models.EmailField(_("email address"), unique=True, max_length=200)
    role = models.CharField(_("user role"), max_length=5, choices=UserRoles.ROLES, default=UserRoles.USER)
    image = models.ImageField(upload_to="avatars/", null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['pk']

    def __str__(self):
        return self.email
