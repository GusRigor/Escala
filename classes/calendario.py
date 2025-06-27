from datetime import date
from classes.atividade import Atividade
from classes.tipoAtividade import TipoAtividadeVazia
from enums.turno import Turno
from enums.tipoMemoria import TipoMemoria
import calendar

class Calendario:
    def __init__(self, data:date, atividades:list[Atividade]):
        self.data = data
        self.atividades_inseridas = atividades
        self.atividades = self._criar_atividades_vazias_()
        self.atividades = self._adicionar_atividades_inseridas()

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
    
    def _adicionar_atividades_inseridas(self):
        for atividade in self.atividades_inseridas:
            for i, atividade_criada in enumerate(self.atividades):
                if (atividade_criada.dia == atividade.dia and
                        atividade_criada.turno == atividade.turno):
                    self.atividades[i] = atividade
                    break
        return self.atividades
    
    def adicionar_atividade(self, atividade:Atividade):
        for i, atividade_criada in enumerate(self.atividades):
            if (atividade_criada.dia == atividade.dia and
                    atividade_criada.turno == atividade.turno and
                    atividade_criada.tipo.tipo == TipoMemoria.VAZIA):
                print(f"Substituindo atividade vazia no dia {atividade.dia} turno {atividade.turno}")
                print(f"Atividade anterior: {atividade_criada}")
                print(f"Nova atividade: {atividade}")
                self.atividades[i] = atividade
                return