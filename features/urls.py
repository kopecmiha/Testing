from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SpecializationViewSet, CompetenceViewSet, DisciplineViewSet
router = DefaultRouter()
router.register('specialization', SpecializationViewSet, basename='specialization')
router.register('competence', CompetenceViewSet, basename='competence')
router.register('discipline', DisciplineViewSet, basename='discipline')
urlpatterns = [
    path('', include(router.urls)),
]