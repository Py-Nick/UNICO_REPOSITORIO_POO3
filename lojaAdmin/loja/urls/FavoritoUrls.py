from django.urls import path
from loja.views.FavoritoView import list_favoritaritem_view, create_favoritaritem_view, remover_favoritaritem_view
urlpatterns = [
    path("", list_favoritaritem_view, name= 'list_favorito'),
    path('remover/<int:item_id>/', remover_favoritaritem_view, name='remover_favoritoitem'),
    path("<int:produto_id>", create_favoritaritem_view, name='favoritar_item'),
]