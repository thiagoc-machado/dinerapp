from django.db import models


class movimentos(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.FloatField()
    categoria = models.ForeignKey('categorias', on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    descr = models.CharField(max_length=500, blank=True, null=True)
    in_out = models.BooleanField()

    def __str__(self):
        return self.nome
    
class categorias(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
