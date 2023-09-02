from django.urls import path,include
from . import views
from knox import views as knox_views

urlpatterns = [
 
   
    path('create-user/',views.CreateUserAPI.as_view()),
    path('list-user/',views.ListUserAPIView.as_view()),
    path('update-user/<int:pk>/',views.UpdateUserAPI.as_view()),
    path('delete-user/<int:pk>/',views.DeleteUserAPIView.as_view()),

   

]
