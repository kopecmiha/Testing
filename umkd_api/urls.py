from django.urls import path
from .views import ListOfCompetences


urlpatterns = [
    path('list_competences/', ListOfCompetences.as_view()),
]