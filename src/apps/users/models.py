from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    A class to represent the `users.User` model.
    """

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


for field, verbose_name in {
    "username": _("login"),
    "email": _("e-mail"),
    "is_active": _("active"),
    "is_staff": _("admin"),
    "is_superuser": _("superuser"),
}.items():
    User._meta.get_field(field).verbose_name = verbose_name
