from django.db import models
from .tipoMemoria import TipoMemoria

class TipoAtividade(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    sigla = models.CharField(max_length=4, unique=False)
    sigla_complementar = models.CharField(max_length=4, default='',blank=True, null=True)  # Para atividades complementares
    duracao = models.IntegerField(default=0)  # Duração em horas
    tipo =  models.CharField(
        max_length=2,
        choices=TipoMemoria.choices,
        default=TipoMemoria.VAZIA,
        blank=True
    )

    def __str__(self):
        if self.sigla_complementar != '':
            return f"{self.sigla} - {self.nome} ({self.sigla_complementar}), tipo {self.tipo}  duração {self.duracao} horas"
        return f"{self.sigla} - {self.nome}, tipo {self.tipo}  duração {self.duracao} horas"