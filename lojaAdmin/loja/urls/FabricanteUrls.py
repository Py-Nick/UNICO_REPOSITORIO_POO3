from django.urls import path
from loja.views.FabricanteView import list_fabricante_view, edit_fabricante_view
urlpatterns = [
    path("", list_fabricante_view, name='fabricante'),
    path("edit/<int:id>", edit_fabricante_view, name='edit_fabricante'),
]