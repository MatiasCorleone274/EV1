from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.vista_inicio, name='inicio'),
    path('detalle/', views.vista_detalle, name='detalle'),
]