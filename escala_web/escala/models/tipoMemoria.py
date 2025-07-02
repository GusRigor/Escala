from django.db import models

class TipoMemoria(models.TextChoices):
    TEORICA = 'T', 'Teórica'
    PRATICA = 'P', 'Prática'
    VAZIA = '', '—'