from django.contrib import admin
from .models import TipoAtividade, EscalaDia, EscalaMensal
from .models.preceptor import Preceptor
from .models.setor import Setor

admin.site.register([
    TipoAtividade,
    EscalaDia,
    EscalaMensal,
    Setor,
    Preceptor
    ])
