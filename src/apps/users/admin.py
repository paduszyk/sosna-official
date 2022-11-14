from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .forms import UserAdminChangeForm
from .models import User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    """
    Admin options for the `users.User` model.
    """

    form = UserAdminChangeForm
