from django.contrib import admin
from .models import Testing, Question, Answer


@admin.register(Testing)
class TestingAdmin(admin.ModelAdmin):
    """
    Testing
    """

    list_display = "id", "uuid_testing", "specialization"
    list_display_links = "id", "uuid_testing", "specialization"
    search_fields = "id", "specialization", "discipline"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Question
    """

    list_display = "id", "uuid_question", "text"
    list_display_links = "id", "uuid_question", "text"
    search_fields = "id", "text"


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """
    Testing
    """

    list_display = "id", "uuid_answer", "text"
    list_display_links = "id", "uuid_answer", "text"
    search_fields = "id", "uuid_answer", "text"
