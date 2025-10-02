from django.urls import path
from . import views

urlpatterns = [
    path('cadastra_usuario/', views.cadastra_usuario, name='cadastrar_usuario'),
    #path('login/', views.loga_usuario, name='login'),
]