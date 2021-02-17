from django.db import models


class CPF(models.Model):
    numero = models.CharField(max_length=20)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.numero


class Cliente(models.Model):
    name = models.CharField(max_length=70, blank=False, null=False)
    endereco = models.CharField(max_length=500, blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idaide = models.IntegerField()
    email = models.EmailField()
    cpf = models.OneToOneField(CPF, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return ('Nome: '+self.name)


class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao + '-' + self.numero
