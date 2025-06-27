from utilidades.fomate_data import dia_semana_portugues
from datetime import date
from classes.tipoAtividade import TipoAtividade

class Atividade:
    def __init__(self, tipo:TipoAtividade, turno, dia:date, dia_semana:str=None):
        self.tipo = tipo
        self.dia = dia
        self.turno = turno
        self.dia_semana = dia_semana_portugues(self.dia.strftime("%a"))

    def dia_formatado(self):
        return f'{int(self.dia.strftime("%d"))} {self.dia_semana}'
    
    def __str__(self):
        return f"Dia: {self.dia_formatado()}, {self.tipo}, turno {self.turno}"