from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _

from .models import BaseUser, SystemUser


class CreateUserForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = BaseUser
        fields = ('username', 'password', 'email', 'active', 'staff', 'admin')

    def clean_username(self) -> str:
        username = self.cleaned_data['username']
        try:
            BaseUser.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise ValidationError(_('Username already exists'))

    def save(self, commit=True) -> BaseUser:
        user = super(CreateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ChangeUserForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta(UserChangeForm.Meta):
        model = BaseUser
        fields = ('username', 'email', 'password', 'active', 'staff', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class SetUserRoleForm(forms.ModelForm):
    class Meta:
        model = SystemUser
        fields = ['role']
