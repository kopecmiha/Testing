from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from testing.models import Testing, Question, Answer


class TestingSession(models.Model):
    session_uuid = models.UUIDField(
        default=uuid4,
        editable=False,
        verbose_name=_("UUID Field"),
        db_index=True,
    )
    test_started = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Started")
    )
    test_finished = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Finished")
    )
    testing = models.ForeignKey(
        to=Testing,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Test"),
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("User"),
    )
    objects = models.Manager()

    class Meta:
        verbose_name = _("Session")
        verbose_name_plural = _("Sessions")


class UserAnswers(models.Model):
    question = models.ForeignKey(
        to=Question,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Question"),
    )
    answers = models.ManyToManyField(
        to=Answer,
        verbose_name=_("Answers"),
    )
    session = models.ForeignKey(
        to=TestingSession,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Session"),
    )

    objects = models.Manager()

    class Meta:
        verbose_name = _("User answers")
        verbose_name_plural = _("User answers")
