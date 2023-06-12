from django.contrib import admin

from apps.Veterinaria.models import Cliente, HistoriaClinica, Mascota


# Register your models here.

admin.site.register(Cliente)

class HistoriaClinica_Inline(admin.StackedInline):
    model = HistoriaClinica
    extra = 0

class Mascota_Admin(admin.ModelAdmin):
    inlines = [
        HistoriaClinica_Inline,
    ]

admin.site.register(Mascota, Mascota_Admin)

class HistoriaClinicaAdmin(admin.ModelAdmin):
    list_display = ('fecha_consulta', 'observaciones', 'estado')
    
admin.site.register(HistoriaClinica, HistoriaClinicaAdmin)