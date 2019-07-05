from django.urls import path
from .views import cadastro_user,login_user, home

urlpatterns = [
    path("", home, name="home"),
    path("cadastrouser", cadastro_user, name="cadastro_user"),
    path("login", login_user, name="login_user"),
]