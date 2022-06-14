from django.contrib import admin
from .models import Specialization, Competence, Discipline


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    """
    Specialization
    """

    list_display = "id", "title", "code"
    list_display_links = "id", "title", "code"
    search_fields = "id", "title", "code"


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    """
    Competence
    """

    list_display = "id", "code", "description"
    list_display_links = "id", "code", "description"
    search_fields = "id", "code", "description"


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    """
    Discipline
    """

    list_display = "id", "title"
    list_display_links = "id", "title"
    search_fields = "id", "title"

