from django.urls import path
from .views import cadastro_user,login_user, home,user_page,cancelar_aluguel,home_deslog,alugar_confirm,alugar, admin_page, cancelar_aluguel_admin, apaga_user_admin, new_marca, apaga_marca, new_modelo, apaga_modelo, new_carro, alt_carro, apaga_carro

urlpatterns = [
    path("", home, name="home"),
    path("cadastrouser", cadastro_user, name="cadastro_user"),
    path("login", login_user,name="login_user"),
    path("user_page", user_page,name="user_page"),
    path("administrador", admin_page ,name="admin_page"),
    path("delete/<int:id>", cancelar_aluguel,name="cancelar_aluguel"),
    path("cancel/<int:id>", cancelar_aluguel_admin,name="cancelar_aluguel_admin"),
    path("deslog",home_deslog,name="home_deslog"),
    path("alugar/<int:id>/<str:dat>", alugar_confirm,name="confirmar_aluguel"),
    path("alugado/<int:id>", alugar,name="alugar"),
    path("apagauser/<int:id>", apaga_user_admin,name="apaga_user_admin"),
    path("novo/marca", new_marca, name="new_marca"),
    path("novo/modelo", new_modelo, name="new_modelo"),
    path("novo/carro", new_carro, name="new_carro"),
    path("novo/carro/<int:id>", alt_carro, name="alt_carro"),
    path("apaga/marca/<int:id>", apaga_marca, name="apaga_marca"),
    path("apaga/modelo/<int:id>", apaga_modelo, name="apaga_modelo"),
    path("apaga/carro/<int:id>", apaga_carro, name="apaga_carro"),
]