from django.contrib import admin
from crudApp.models import Inscritos, Institucion
# Register your models here.

class InscritoAdmin(admin.ModelAdmin):
    list_display= ['nombre','institucion','estado']

admin.site.register(Inscritos, InscritoAdmin)


class InstitucionAdmin(admin.ModelAdmin):
    list_display= ['nombre','ubicacion']

admin.site.register(Institucion, InstitucionAdmin)

