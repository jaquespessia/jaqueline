from django.db import models

# Create your models here.
class Projeto (models.Model):

    nome = models.CharField (max_length = 200)
    descricao = models.TextField (blank=True, null=True) 
    data_criacao = models.DateTimeField (auto_now_add=True)  


    #exibir titulo por padrão
    def __str__(self):
        return self.nome