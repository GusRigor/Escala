from django.db import models

class Setor(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.nome}'