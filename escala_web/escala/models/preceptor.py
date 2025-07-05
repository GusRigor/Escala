from django.db import models

class Preceptor(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.nome}'