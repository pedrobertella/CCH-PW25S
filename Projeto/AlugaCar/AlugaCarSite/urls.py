from django.urls import path
from .views import cadastro_user

urlpatterns = [
    path("cadastrouser/", cadastro_user, name="cadastro_user"),
]