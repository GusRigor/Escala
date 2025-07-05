from django.contrib import admin
from .models import TipoAtividade, EscalaDia, EscalaMensal

admin.site.register(TipoAtividade)
admin.site.register(EscalaDia)
admin.site.register(EscalaMensal)