from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class Testing(models.Model):
    title = models.CharField(
        null=True, blank=True, verbose_name=_("Title"), max_length=128
    )
    subtitle = models.CharField(
        verbose_name=_("Description"), null=True, blank=True, max_length=128
    )
    answer_time = models.PositiveIntegerField(verbose_name=_("Answer time"), default=0)
    uuid_testing = models.UUIDField(
        default=uuid4,
        editable=False,
        verbose_name=_("UUID Field"),
        db_index=True,
    )
    objects = models.Manager()

    def questions(self):
        questions = Question.objects.filter(testing=self)
        return questions

    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Test")


class Question(models.Model):
    class TypeAnswerEnum(models.TextChoices):
        CHECKBOX = "CHECKBOX", _("Checkbox")
        RADIO = "RADIO", _("Radio button")

    text = models.CharField(blank=False, verbose_name=_("Question"), max_length=200)
    image = models.FileField(
        upload_to="test_images", verbose_name=_("Test image"), blank=True, null=True
    )
    type_answer_question = models.CharField(
        max_length=30, choices=TypeAnswerEnum.choices, default=TypeAnswerEnum.CHECKBOX
    )
    testing = models.ForeignKey(
        to=Testing,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Test"),
    )
    uuid_question = models.UUIDField(
        default=uuid4,
        editable=False,
        verbose_name=_("UUID Field"),
        db_index=True,
        unique=True,
    )

    objects = models.Manager()

    def answers(self):
        answers = Answer.objects.filter(question=self)
        return answers

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Question")


class Answer(models.Model):
    text = models.CharField(blank=False, verbose_name=_("Answer"), max_length=128)
    question = models.ForeignKey(
        to=Question,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Question"),
    )
    uuid_answer = models.UUIDField(
        default=uuid4,
        editable=False,
        verbose_name=_("UUID Field"),
        db_index=True,
        unique=True,
    )
    correct_answer = models.BooleanField(
        verbose_name=_("Correct answer"), default=False
    )

    objects = models.Manager()

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answer")
