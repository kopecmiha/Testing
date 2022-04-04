from uuid import uuid4
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models


class InviteCode(models.Model):
    code = models.UUIDField(
        default=uuid4, editable=False, verbose_name=_("Invite Code"), db_index=True
    )

    objects = models.Manager()

    class Meta:
        verbose_name = _("Invite Code")
        verbose_name_plural = _("Invite Code")


class User(AbstractBaseUser, PermissionsMixin):
    class StatusEnum(models.TextChoices):
        STUDENT = "STUDENT", _("Student")
        TEACHER = "TEACHER", _("Teacher")
        DEAN = "DEAN", _("Dean")
    uuid = models.UUIDField(
        default=uuid4, editable=False, verbose_name=_("UUID Field"), db_index=True
    )
    username = models.CharField(_("Username"), blank=False, unique=True, max_length=30)
    email = models.EmailField(_("Email address"), null=True, blank=True)
    first_name = models.CharField(_("First name"), max_length=30, null=True, blank=True)
    last_name = models.CharField(_("Last name"), max_length=30, null=True, blank=True)
    patronymic = models.CharField(_("Patronymic"), max_length=30, null=True, blank=True)
    is_active = models.BooleanField(_("Active"), default=True)
    is_staff = models.BooleanField(_("Is staff"), default=False)
    is_superuser = models.BooleanField(_("Is superuser"), default=False)
    avatar = models.FileField(_("Avatar"), upload_to="avatars", null=True, blank=True)
    status = models.CharField(
        _("User status"),
        max_length=10,
        choices=StatusEnum.choices,
        default=StatusEnum.STUDENT,
    )

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("User")
        db_table = "auth_user"
