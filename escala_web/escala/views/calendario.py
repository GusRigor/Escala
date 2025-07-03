from django.shortcuts import render
from ..models import TipoAtividade
import calendar

def calendario(request, ano, mes):
    ano = int(ano)
    mes = int(mes)

    calendario = calendar.Calendar()
    dias_mes = list(calendario.itermonthdays(ano, mes))

    semanas = []
    semana = []
    for dia in dias_mes:
        if dia == 0:
            semana.append('')
        else:
            semana.append(dia)
        if len(semana) == 7:
            semanas.append(semana)
            semana = []
    if semana:
        while len(semana) < 7:
            semana.append('')
        semanas.append(semana)

    atividades = TipoAtividade.objects.all()

    contexto = {
        "instituicao": request.session.get('instituicao'),
        "residente": request.session.get('residente'),
        "setores": request.session.get('setores'),
        "preceptores": request.session.get('preceptores'),
        "mes": mes,
        "ano": ano,
        "semanas": semanas,
        "nome_mes": calendar.month_name[mes],
        "atividades": atividades,
    }

    return render(request, "calendario.html", contexto)
