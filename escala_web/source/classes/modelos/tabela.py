from typing import List
from datetime import date
from source.classes.modelos.Renderable import Renderable
from source.utilidades.fomate_data import eh_fim_de_semana, dia_semana_portugues

class Tabela(Renderable):
    def __init__(self, dias: List[date], manha: List[str], tarde: List[str], noite: List[str]):
        self.dias_numeros = dias.copy()
        self.dias_letras = dias.copy()
        self.manha = manha.copy()
        self.tarde = tarde.copy()
        self.noite = noite.copy()
        self._formatar_dados_(dias.copy())

    def _formatar_dados_(self, dias: List[date]):
        for i, dia in enumerate(dias):
            if eh_fim_de_semana(dia):
                self.dias_numeros[i] = r"\textbf{\cellcolor{roxo}" + f"{int(dia.strftime('%d'))}" + "}"
                self.dias_letras[i] = r"\textbf{\cellcolor{roxo}" + dia_semana_portugues(dia.strftime("%a")) + "}"
                self.manha[i] = r"\textbf{\cellcolor{roxo}" + self.manha[i] + "}"
                self.tarde[i] = r"\textbf{\cellcolor{roxo}" + self.tarde[i] + "}"
                self.noite[i] = r"\textbf{\cellcolor{roxo}" + self.noite[i] + "}"
            else:
                self.dias_numeros[i] = r"\textbf{" + f"{int(dia.strftime('%d'))}" + "}"
                self.dias_letras[i] = r"\textbf{" + dia_semana_portugues(dia.strftime("%a")) + "}"
                self.manha[i] = r"\textbf{" + self.manha[i] + "}"
                self.tarde[i] = r"\textbf{" + self.tarde[i] + "}"
                self.noite[i] = r"\textbf{" + self.noite[i] + "}"
                
    def render(self):
        return {
            "numero_colunas": len(self.dias_numeros),
            "numero_colunas_mais_um": len(self.dias_numeros) + 1,
            "dias_numeros": "\n& ".join(self.dias_numeros),
            "dias_letras": "\n& ".join(self.dias_letras),
            "manha": "\n& ".join(self.manha),
            "tarde": "\n& ".join(self.tarde),
            "noite": "\n& ".join(self.noite)
        }