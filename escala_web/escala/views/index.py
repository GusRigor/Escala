from django.shortcuts import render, redirect
from ..forms import EscalaForm

def index(request):
    if request.method == "POST":
        form = EscalaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            request.session['instituicao'] = cd['instituicao']
            request.session['residente'] = cd['residente']
            request.session['setores'] = [setor.id for setor in cd['setores']]
            request.session['preceptores'] = [preceptor.id for preceptor in cd['preceptores']]

            return redirect('calendario', ano=cd["mes_ano"].year, mes=cd["mes_ano"].month)
    else:
        form = EscalaForm()

    return render(request, "index.html", {"form": form})
