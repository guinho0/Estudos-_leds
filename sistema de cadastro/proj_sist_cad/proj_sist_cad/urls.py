from django.urls import path
from app_sist_cad import views

urlpatterns = [
  #rota,view responsável,nome de referencia; path=caminho
  #usuários.com
  path('',views.home,name="home"),
  #usuarios.com/usuarios
  path('usuarios/',views.usuarios,name="listagem_usuarios")

]
