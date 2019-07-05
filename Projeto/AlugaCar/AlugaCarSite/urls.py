from django.urls import path
from .views import cadastro_user,login_user, home,user_page,cancelar_aluguel

urlpatterns = [
    path("", home, name="home"),
    path("cadastrouser", cadastro_user, name="cadastro_user"),
    path("login", login_user,name="login_user"),
    path("user_page", user_page,name="user_page"),
    path("delete/<int:id>", cancelar_aluguel,name="cancelar_aluguel")
]