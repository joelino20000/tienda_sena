from django.urls import path
from .views import ProductoListApiView, ProductoDetailApiView, ProductoDetailClasificacion

urlpatterns = [
    path('', ProductoListApiView.as_view(), name="Producto_list"),
    path('<int:producto_id>/', ProductoDetailApiView.as_view(), name="Producto_detail"),
    path('<str:producto_clasif>/', ProductoDetailClasificacion.as_view(), name="prod_clasif")
]