from django.urls import path
from . import views

app_name = "app_site_cursos"

urlpatterns = [
    path('', views.home, name='home'),
    path('cursos/add_cursos', views.add_cursos, name='add_cursos'),
    path('popup/popup_content', views.popup_view, name='popup_content')
]