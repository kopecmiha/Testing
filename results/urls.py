from django.urls import path
from .views import StartTesting, UserAnswer, FinishTesting, GetSelfAnswers

urlpatterns = [
    path('start_testing_session/', StartTesting.as_view()),
    path('finish_testing_session/', FinishTesting.as_view()),
    path('user_answer/', UserAnswer.as_view()),
    path('get_self_answers/<str:uuid_testing>/', GetSelfAnswers.as_view()),
]