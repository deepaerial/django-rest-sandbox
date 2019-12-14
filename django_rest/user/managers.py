from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(
        self,
        username,
        password,
        email=None,
        is_active=True,
        is_staff=False,
        is_admin=False,
        auto_save=True,
    ):
        if not username:
            raise ValueError(_('Username is empty: '), username)
        if not password:
            raise ValueError(_('Password is empty: '), password)
        user = self.model(username=username)
        user.set_password(password)
        if email:
            user.email = self.normalize_email(email)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password, email=None, auto_save=True):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
            is_staff=True,
            auto_save=auto_save,
        )
        return user

    def create_superuser(self, username, password, email=None, auto_save=True):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
            is_staff=True,
            is_admin=True,
            auto_save=auto_save,
        )
        return user
