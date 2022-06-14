from django.db import models
from django.utils.translation import gettext_lazy as _


class Specialization(models.Model):
    title = models.CharField(_("Title"), blank=True, unique=True, max_length=100)
    code = models.CharField(_("Code"), blank=True, unique=True, max_length=100)
    objects = models.Manager()

    class Meta:
        verbose_name = _("Specialization")
        verbose_name_plural = _("Specializations")


class Competence(models.Model):
    code = models.CharField(_("Code"), blank=True, unique=True, max_length=10)
    description = models.TextField(verbose_name=_("Name"), blank=True)
    specialization = models.ForeignKey(
        on_delete=models.CASCADE,
        to=Specialization,
        null=True,
        blank=True,
        verbose_name=_("Specialization"),
    )
    objects = models.Manager()

    class Meta:
        verbose_name = _("Competence")
        verbose_name_plural = _("Competences")

    def __str__(self):
        return self.code


class Discipline(models.Model):
    title = models.CharField(_("Title"), blank=True, max_length=100)
    specialization = models.ForeignKey(
        on_delete=models.CASCADE,
        to=Specialization,
        null=True,
        blank=True,
        verbose_name=_("Specialization"),
    )
    competences = models.ManyToManyField(
        to=Competence,
        verbose_name=_("Competences"),
    )
    objects = models.Manager()

    class Meta:
        verbose_name = _("Discipline")
        verbose_name_plural = _("Disciplines")
