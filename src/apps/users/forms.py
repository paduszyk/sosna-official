from django import forms
from django.contrib.auth.forms import UserChangeForm as AuthUserChangeForm
from django.contrib.auth.models import Group

from .models import User


class UserAdminChangeForm(AuthUserChangeForm):
    """
    Admin change form of the `users.User` model.
    """

    class Meta:
        model = User
        exclude = ()


class GroupAdminChangeForm(forms.ModelForm):
    """
    Admin change form of the `auth.Group` model.
    """

    class Meta:
        model = Group
        exclude = ()
