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
    description = models.CharField(_("Title"), blank=True, unique=True, max_length=1000)
    code = models.CharField(_("Code"), blank=True, unique=True, max_length=10)
    objects = models.Manager()

    class Meta:
        verbose_name = _("Competence")
        verbose_name_plural = _("Competences")


class Discipline(models.Model):
    title = models.CharField(_("Code"), blank=True, unique=True, max_length=100)
    objects = models.Manager()

    class Meta:
        verbose_name = _("Discipline")
        verbose_name_plural = _("Disciplines")
