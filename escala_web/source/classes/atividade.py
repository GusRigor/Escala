from source.utilidades.fomate_data import dia_semana_portugues
from datetime import date
from source.classes.tipoAtividade import TipoAtividade
from source.enums import Turno

class Atividade:
    def __init__(self, tipo:TipoAtividade, turno:Turno, dia:date):
        self.tipo = tipo
        self.dia = dia
        self.turno = turno
        self.dia_semana = dia_semana_portugues(self.dia.strftime("%a"))

    def dia_formatado(self):
        return f'{int(self.dia.strftime("%d"))} {self.dia_semana}'
    
    def __str__(self):
        return f"Dia: {self.dia_formatado()}, {self.tipo}, turno {self.turno.value}"