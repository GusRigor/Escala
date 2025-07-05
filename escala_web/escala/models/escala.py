from django.db import models
from .preceptor import Preceptor
from .setor import Setor
from source.utilidades import mes_portugues

class EscalaMensal(models.Model):
    instituicao = models.CharField(max_length=255)
    residente = models.CharField(max_length=255)
    setores = models.ManyToManyField(Setor, related_name='escalas')
    preceptores = models.ManyToManyField(Preceptor, related_name='escalas')
    ano = models.IntegerField()
    mes = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Escala de {mes_portugues(self.mes)} de {self.ano}"

class EscalaDia(models.Model):
    escala = models.ForeignKey(EscalaMensal, related_name='dias', on_delete=models.CASCADE)
    dia = models.IntegerField()
    turno = models.CharField(max_length=1, choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')])
    atividade = models.ForeignKey('TipoAtividade', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"Atividade: dia {self.dia} - {self.turno}"
