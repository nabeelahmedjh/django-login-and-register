from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('home/', views.home, name='accounts-home'),
    path('logout/', views.logoutUser, name='logout'),
    path('update-username', views.updateUsername, name='update-username'),
    path('update-password', views.updatePassword, name='update-password'),
]