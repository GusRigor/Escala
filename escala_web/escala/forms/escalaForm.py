from django import forms
from ..models.preceptor import Preceptor
from ..models.setor import Setor

class EscalaForm(forms.Form):
    instituicao = forms.CharField(
        label="Instituição",
        max_length=100,
        initial="Maternidade Bárbara Heliodora"
    )
    residente = forms.CharField(
        label="Residente",
        max_length=100,
        initial="Milene Mendes da Silva"
    )

    setores = forms.ModelMultipleChoiceField(
        label="Setores",
        queryset=Setor.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    preceptores = forms.ModelMultipleChoiceField(
        label="Preceptores",
        queryset=Preceptor.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    mes_ano = forms.DateField(
        label="Mês e Ano",
        widget=forms.DateInput(attrs={"type": "month"}),
        input_formats=["%Y-%m"]
    )
