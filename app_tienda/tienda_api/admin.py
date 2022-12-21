from django.contrib import admin
from .models import Producto


# Register your models here.


#MotoAdmin
class ProductoAdmin(admin.ModelAdmin):
    list_display = [
        "reference",
        "marca",
        "precio",
        "clasificacion",
        "imagen"
    ]

admin.site.register(Producto, ProductoAdmin)