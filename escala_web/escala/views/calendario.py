from django.shortcuts import render
import calendar
from datetime import date
from ..models import TipoAtividade
from source.utilidades import mes_portugues

def calendario(request, ano, mes):
    ano = int(ano)
    mes = int(mes)

    atividades = TipoAtividade.objects.all()

    dias_do_mes = []
    num_dias = calendar.monthrange(ano, mes)[1]  # quantos dias tem o mês
    dias_semana = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']

    for dia in range(1, num_dias + 1):
        weekday = date(ano, mes, dia).weekday()  # segunda=0, domingo=6
        # ajusta para domingo como 0
        weekday = (weekday + 1) % 7
        dias_do_mes.append({
            'numero': dia,
            'nome': dias_semana[weekday]
        })

    turnos = ['M', 'T', 'N']

    contexto = {
        "instituicao": request.session.get('instituicao'),
        "residente": request.session.get('residente'),
        "setores": request.session.get('setores'),
        "preceptores": request.session.get('preceptores'),
        "mes": mes,
        "ano": ano,
        "nome_mes": mes_portugues(calendar.month_name[mes]),
        "dias_do_mes": dias_do_mes,
        "atividades": atividades,
        "turnos": turnos,
    }

    return render(request, "calendario.html", contexto)
