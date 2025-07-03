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
    num_dias = calendar.monthrange(ano, mes)[1]
    dias_semana = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']

    for dia in range(1, num_dias + 1):
        weekday = date(ano, mes, dia).weekday()
        weekday = (weekday + 1) % 7
        dias_do_mes.append({
            'numero': dia,
            'nome': dias_semana[weekday]
        })

    turnos = ['M', 'T', 'N']

    if request.method == "POST":
        _calendario_post_(request, ano, mes, turnos, dias_do_mes)

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

def _calendario_post_(request, ano, mes, turnos, dias_do_mes):
    # Dados fixos do contexto
    instituicao = request.session.get('instituicao')
    residente = request.session.get('residente')
    setores = request.session.get('setores')
    preceptores = request.session.get('preceptores')

    print(f"Instituição: {instituicao}")
    print(f"Residente: {residente}")
    print(f"Setores: {setores}")
    print(f"Preceptores: {preceptores}")
    print(f"Ano/Mês: {ano}/{mes}")

        # Dados preenchidos no calendário
    for dia in dias_do_mes:
        numero = dia['numero']
        for turno in turnos:
            key = f"atividade_{numero}_{turno}"
            atividade_id = request.POST.get(key)
            if atividade_id:
                print(f"Dia {numero}, Turno {turno}: Atividade {atividade_id}")
            else:
                print(f"Dia {numero}, Turno {turno}: [vazio]")

        # Aqui você pode salvar no banco, ou gerar um PDF, etc.
        # return redirect('alguma_view_sucesso')
        # ou renderizar uma página de sucesso
    return render(request, "sucesso.html", {})

