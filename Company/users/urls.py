
from django.urls import path,include
from users.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('create_user/',CreateUser.as_view()),
    path('login_user/',Login.as_view()),
    path('logout_user/',Logoutview.as_view()),
    path('getusers/',GetUsersData.as_view(), name = 'crud_user'),
    
]
