from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('specialization', SpecializationViewSet, basename='specialization')
router.register('competence', CompetenceViewSet, basename='competence')
router.register('discipline', DisciplineViewSet, basename='discipline')
urlpatterns = [
    path('', include(router.urls)),
    path('get_competences_by_specialization/<int:specialization_id>/', CompetenceSetBySpecialization.as_view()),
    path('get_disciplines_by_specialization/<int:specialization_id>/', DisciplineSetBySpecialization.as_view()),
]