from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class BaseUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.admin

    def has_perm(self, perm, obj=None):
        if self.is_admin and self.is_staff:
            return True
        return False

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.username


class UserRole(models.Model):
    name = models.CharField(max_length=255, unique=True)


class SystemUser(BaseUser):
    role = models.ForeignKey(
        UserRole,
        on_delete=models.PROTECT,
        related_name='users',
        related_query_name='user',
    )
