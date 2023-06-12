from django.contrib import admin
from django.urls import path

from apps.Veterinaria.views import Login

urlpatterns = [
    # URLs para el modelo Cliente
    path('admin/',admin.site.urls),
]
