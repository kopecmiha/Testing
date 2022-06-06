from django.urls import path
from .views import *

urlpatterns = [
    path('create_test/', CreateTest.as_view()),
    path('update_test/', UpdateTest.as_view()),
    path('delete_test/', DeleteTest.as_view()),

    path('create_question/', CreateQuestion.as_view()),
    path('update_question/', UpdateQuestion.as_view()),
    path('delete_question/', DeleteQuestion.as_view()),

    path('create_answer/', CreateAnswer.as_view()),
    path('update_answer/', UpdateAnswer.as_view()),
    path('delete_answer/', DeleteAnswer.as_view()),

    path('get_test/<str:uuid_testing>/<int:mode>/', GetTest.as_view()),
    path('list_test/', ListOfTest.as_view()),
    path('add_questions_from_bank/', AddQuestionsFromBank.as_view()),
]
