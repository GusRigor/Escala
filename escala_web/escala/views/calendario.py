from django.shortcuts import render
import calendar
from datetime import date
from ..models import TipoAtividade
from source.utilidades import mes_portugues, to_date
from source.classes.conversores import Conversor_HTML
from source.classes.tipoAtividade import TipoAtividadeVazia
from source.classes.calendario import Calendario
from source.classes.escala import Escala
from source.classes.geradores.gerador import Gerador

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
        return _calendario_post_(request, ano, mes, turnos, dias_do_mes)

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
    conversor = Conversor_HTML()
    data = to_date(ano, mes)
    atividades = []

    # Dados fixos do contexto
    instituicao = request.session.get('instituicao')
    residente = request.session.get('residente')
    setores = request.session.get('setores')
    preceptores = request.session.get('preceptores')


        # Dados preenchidos no calendário
    for dia in dias_do_mes:
        numero = dia['numero']
        for turno in turnos:
            key = f"atividade_{numero}_{turno}"
            atividade_id = request.POST.get(key)
            if atividade_id:
                atividade = TipoAtividade.objects.get(id=atividade_id)
                tipoAtividade = conversor.converter_para_tipo_atividade(
                    nome=atividade.nome,
                    sigla=atividade.sigla,
                    duracao=atividade.duracao,
                    tipo=atividade.tipo,
                    sigla_complementar=atividade.sigla_complementar
                )
                atividade_model = conversor.converter_para_atividade(
                    tipo=tipoAtividade,
                    turno=turno,
                    dia=date(ano, mes, numero)
                )
                atividades.append(atividade_model)
            else:
                atividade_model = conversor.converter_para_atividade(
                    tipo=TipoAtividadeVazia(),
                    turno=turno,
                    dia=date(ano, mes, numero)
                )
                atividades.append(atividade_model)
    calendario_model = Calendario(to_date(ano, mes), atividades)
    escala = Escala(
        instituicao,
        residente,
        setores,
        preceptores,
        calendario_model
    )

    Gerador.gerar_escala(escala)

    return render(request, "sucesso.html", {})

