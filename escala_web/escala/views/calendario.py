from django.shortcuts import render
from django.urls import reverse
import calendar
from datetime import date
from ..models import TipoAtividade, EscalaDia, EscalaMensal
from source.utilidades import mes_portugues, to_date
from source.classes.conversores import Conversor_HTML
from source.classes.tipoAtividade import TipoAtividadeVazia
from source.classes.calendario import Calendario
from source.classes.escala import Escala
from source.classes.geradores.gerador import Gerador
from ..models.setor import Setor
from ..models.preceptor import Preceptor

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
    setores_ids = request.session.get('setores', [])
    preceptores_ids = request.session.get('preceptores', [])

    setores = Setor.objects.filter(id__in=setores_ids)
    preceptores = Preceptor.objects.filter(id__in=preceptores_ids)

    if request.method == "POST":
        return _calendario_post_(request, ano, mes, turnos, dias_do_mes)

    contexto = {
        "instituicao": request.session.get('instituicao'),
        "residente": request.session.get('residente'),
        "setores": setores,
        "preceptores": preceptores,
        "mes": mes,
        "ano": ano,
        "nome_mes": mes_portugues(calendar.month_name[mes]),
        "dias_do_mes": dias_do_mes,
        "atividades": atividades,
        "turnos": turnos,
    }
    
    _resgata_escala_(
        request=request,
        ano=ano,
        mes=mes,
        contexto=contexto
    )

    return render(request, "calendario.html", contexto)

def _calendario_post_(request, ano, mes, turnos, dias_do_mes):
    conversor = Conversor_HTML()
    data = to_date(ano, mes)
    atividades = []

    # Dados fixos do contexto
    instituicao = request.session.get('instituicao')
    residente = request.session.get('residente')
    setores_ids = request.session.get('setores', [])
    preceptores_ids = request.session.get('preceptores', [])

    setores = Setor.objects.filter(id__in=setores_ids)
    preceptores = Preceptor.objects.filter(id__in=preceptores_ids)


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
    
    _salva_escala_(
        request=request,
        instituicao=instituicao,
        residente=residente,
        setores=setores,
        preceptores=preceptores,
        ano=ano,
        mes=mes,
        dias_do_mes=dias_do_mes,
        turnos=turnos
    )

    Gerador.gerar_escala(escala)

    contexto = {
        "link_pdf": reverse('download_pdf')
    }
    return render(request, "sucesso.html", contexto)

def _salva_escala_(request, instituicao, residente, setores, preceptores, ano, mes, dias_do_mes, turnos):
    # cria ou atualiza a escala do mês
    escala_db, created = EscalaMensal.objects.update_or_create(
        instituicao=instituicao,
        residente=residente,
        ano=ano,
        mes=mes,
        defaults={}
    )

    escala_db.setores.set(setores)
    escala_db.preceptores.set(preceptores)

    # limpa os dias anteriores caso esteja atualizando
    if not created:
        escala_db.dias.all().delete()

    # salva os dias/turnos
    for dia in dias_do_mes:
        numero = dia['numero']
        for turno in turnos:
            key = f"atividade_{numero}_{turno}"
            atividade_id = request.POST.get(key)
            atividade = TipoAtividade.objects.filter(id=atividade_id).first() if atividade_id else None

            EscalaDia.objects.create(
                escala=escala_db,
                dia=numero,
                turno=turno,
                atividade=atividade
            )

def _resgata_escala_(request, ano, mes, contexto):
    escala_salva = EscalaMensal.objects.filter(
        ano=ano,
        mes=mes
    ).prefetch_related('dias').first()

    atividades_pre_selecionadas = {}
    if escala_salva:
        for dia in escala_salva.dias.all():
            atividades_pre_selecionadas[f"{dia.dia}_{dia.turno}"] = str(dia.atividade_id) if dia.atividade_id else ""

    contexto.update({
        "atividades_pre_selecionadas": atividades_pre_selecionadas
    })