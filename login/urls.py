from django.urls import path

from login import views

urlpatterns = [
    path('login/', views.LoginPage, name='login_page'),
    path('register/', views.RegisterPage, name='register_page'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile_page'),
]