from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name = "users" ),
    path('login/', views.login_view,  name='login'),
    path('signup/', views.signup_view,  name='signup'),
]