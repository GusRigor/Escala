from django import forms
from .models import TipoAtividade

class EscalaForm(forms.Form):
    instituicao = forms.CharField(label="Instituição", max_length=100, initial="Maternidade Bárbara Heliodora")
    residente = forms.CharField(label="Residente", max_length=100, initial="Milene Mendes da Silva")
    setores = forms.CharField(label="Setores", widget=forms.Textarea)
    preceptores = forms.CharField(label="Preceptores", widget=forms.Textarea)
    mes_ano = forms.DateField(
        label="Mês e Ano",
        widget=forms.DateInput(attrs={"type": "month"}),
        input_formats=["%Y-%m"]
    )
    # tipoAtividade = forms.ModelChoiceField(
    #     queryset=TipoAtividade.objects.all(),
    #     empty_label="Selecione um tipo de atividade",
    #     widget=forms.Select,
    #     label="Tipo de Atividade")