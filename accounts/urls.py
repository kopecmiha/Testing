from django.urls import path
from .views import CreateDekan, CreateUser, GetUserProfile, ObtainToken, UpdateUserProfile

urlpatterns = [
    path('create_dekan/', CreateDekan.as_view()),
    path('create_user/', CreateUser.as_view()),
    path('obtain_token/', ObtainToken.as_view()),
    path('get_profile/', GetUserProfile.as_view()),
    path('update_profile/', UpdateUserProfile.as_view())
]