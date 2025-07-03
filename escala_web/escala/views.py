from django.shortcuts import render
from django.http import HttpResponse
from .forms import EscalaForm
from .models import TipoAtividade
import calendar

def index(request):
    if request.method == "POST":
        form = EscalaForm(request.POST)
        if form.is_valid():
            instituicao = form.cleaned_data["instituicao"]
            residente = form.cleaned_data["residente"]
            setores = form.cleaned_data["setores"]
            preceptores = form.cleaned_data["preceptores"]
            data = form.cleaned_data["mes_ano"]
            mes = data.month
            ano = data.year

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
            tipoAtividades = TipoAtividade.objects.all()

            contexto = {
                "instituicao": instituicao,
                "residente": residente,
                "setores": setores,
                "preceptores": preceptores,
                "mes": mes,
                "ano": ano,
                "semanas": semanas,
                "nome_mes": calendar.month_name[mes],
                "atividades": tipoAtividades,
            }
            return render(request, "calendario.html", contexto)

            return HttpResponse(f"Instituição: {instituicao}, Residente: {residente}, Setores: {setores}, Preceptores: {preceptores}, Mês: {mes}, Ano: {ano}, Tipo de Atividade: {tipo_atividade}")
    else:
        form = EscalaForm()

    return render(request, "index.html", {"form": form})