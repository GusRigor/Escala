from datetime import date
from classes.atividade import Atividade
from classes.tipoAtividade import TipoAtividadeVazia
from enums.turno import Turno
import calendar

class Calendario:
    def __init__(self, data:date, atividades:list[Atividade]):
        self.data = data
        self.atividades_inseridas = atividades
        self.atividades = self._criar_atividades_vazias_()

    def inicio_mes(self):
        return date(self.data.year, self.data.month, 1)
    
    def final_mes(self):
        return date(self.data.year, self.data.month, calendar.monthrange(self.data.year, self.data.month)[1])

    def __str__(self):
        return f"Calendário início {self.inicio_mes()}, fim {self.final_mes()}:\n" + \
               "\n".join(f"- {atividade}" for atividade in self.atividades)
    
    def _criar_atividades_vazias_(self):
        atividades_criadas = []
        tipo_atividade_vazia = TipoAtividadeVazia()
        for dia in range(self.inicio_mes().day, self.final_mes().day + 1):
            dia_atual = date(self.data.year, self.data.month, dia)
            for turno in [Turno.MANHA, Turno.TARDE, Turno.NOITE]:
                atividade = Atividade(tipo_atividade_vazia, turno, dia_atual)
                atividades_criadas.append(atividade)
        return atividades_criadas