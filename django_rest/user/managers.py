from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(
        self,
        username: str,
        password: str,
        email: str = None,
        active: bool = True,
        staff: bool = False,
        admin: bool = False,
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
        user.active = active
        user.staff = staff
        user.admin = admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password, email=None, auto_save=True):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
            staff=True,
            auto_save=auto_save,
        )
        return user

    def create_superuser(self, username, password, email=None, auto_save=True):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
            staff=True,
            admin=True,
            auto_save=auto_save,
        )
        return user
