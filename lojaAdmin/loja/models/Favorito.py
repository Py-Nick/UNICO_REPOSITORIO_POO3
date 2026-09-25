from loja.models import *

class Favorito(models.Model):
    user = models.ForeignKey(User, null=True, related_name='favorito', on_delete=models.SET_NULL)
    @property
    def total(self):
        return sum(item.quantidade * item.preco for item in self.itens.all())
    def __str__(self):
        return '{}'.format(self.user)

class FavoritoItem(models.Model):
    favorito = models.ForeignKey(Favorito, null=True, related_name='itens', on_delete=models.SET_NULL)
    produto = models.ForeignKey(Produto, null=True, related_name='favoritos', on_delete=models.SET_NULL)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    @property
    def total(self):
        return self.quantidade * self.preco
    def __str__(self):
        return '{}'.format(self.id)