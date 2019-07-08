from django.urls import path
from .views import cadastro_user,login_user, home,user_page,cancelar_aluguel,home_deslog,alugar_confirm,alugar, admin_page, cancelar_aluguel_admin, apaga_user_admin

urlpatterns = [
    path("", home, name="home"),
    path("cadastrouser", cadastro_user, name="cadastro_user"),
    path("login", login_user,name="login_user"),
    path("user_page", user_page,name="user_page"),
    path("administrador", admin_page ,name="admin_page"),
    path("delete/<int:id>", cancelar_aluguel,name="cancelar_aluguel"),
    path("cancel/<int:id>", cancelar_aluguel_admin,name="cancelar_aluguel_admin"),
    path("deslog",home_deslog,name="home_deslog"),
    path("alugar/<int:id>", alugar_confirm,name="confirmar_aluguel"),
    path("alugado/<int:id>", alugar,name="alugar"),
    path("apagauser/<int:id>", apaga_user_admin,name="apaga_user_admin"),
]