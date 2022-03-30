from django.urls import path
from .views import StartTesting, UserAnswer, FinishTesting

urlpatterns = [
    path('start_testing_session/', StartTesting.as_view()),
    path('finish_testing_session/', FinishTesting.as_view()),
    path('user_answer/', UserAnswer.as_view()),
]