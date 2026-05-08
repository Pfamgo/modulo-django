from django.urls import path
from . import views
#2DO PUNTO DE ENTRADA Y ACÁ SE MANEJAN TODAS LAS RUTAS(URL) DE ESTA APP
urlpatterns = [
path('', views.index, name='home_productos'),
path('login/', views.login, name='pepito'),
path('register/', views.register, name='pepito'),
path('dashboard/', views.dashboard, name='pepito'),
path('venta/', views.venta, name='pepito'),
]