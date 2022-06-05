from uuid import uuid4

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _

from features.models import Specialization, Discipline, Competence


class Testing(models.Model):
    title = models.CharField(blank=True, null=True, verbose_name=_("Title"), max_length=200)
    specialization = models.ForeignKey(
        to=Specialization,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Specialization"),
    )
    discipline = models.ForeignKey(
        to=Discipline,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Discipline"),
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
        questions = Question.objects.filter(testing_array__icontains=self.uuid_testing)
        return questions

    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Test")


class Question(models.Model):
    text = models.CharField(blank=True, null=True, verbose_name=_("Question"), max_length=200)
    image = models.FileField(
        upload_to="test_images", verbose_name=_("Test image"), blank=True, null=True
    )
    type_answer_question = models.BooleanField(default=False)
    testing_array = ArrayField(
        default=list,
        base_field=models.UUIDField(),
        verbose_name=_("Test"),
    )
    competence = models.ForeignKey(
        to=Competence,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Competence"),
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
    text = models.CharField(blank=True, null=True, verbose_name=_("Answer"), max_length=128)
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
