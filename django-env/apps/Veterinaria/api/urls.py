from django.urls import path
from apps.Veterinaria.api.api import cliente_api_view, cliente_detail_api_view

urlpatterns = [
    path('cliente/',cliente_api_view, name = 'cliente_api'),
    path('cliente/<int:pk>/',cliente_detail_api_view, name = 'cliente_detail_api_view'),

]

