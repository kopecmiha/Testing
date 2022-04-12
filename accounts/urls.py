from django.urls import path
from .views import CreateDekan, CreateUser, GetUserProfile, ObtainToken, UpdateUserProfile, GetStudents, GetTeachers, DeleteUser

urlpatterns = [
    path('create_dekan/', CreateDekan.as_view()),
    path('create_user/', CreateUser.as_view()),
    path('delete_user/', DeleteUser.as_view()),
    path('obtain_token/', ObtainToken.as_view()),
    path('get_profile/', GetUserProfile.as_view()),
    path('update_profile/', UpdateUserProfile.as_view()),
    path('get_students_list/', GetStudents.as_view()),
    path('get_techers_list/', GetTeachers.as_view())
]