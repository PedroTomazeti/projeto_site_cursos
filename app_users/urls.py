from django.urls import path
from . import views

app_name = 'app_users'

urlpatterns = [
    path('users/add_users', views.add_users, name='add_users')
]