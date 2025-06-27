from datetime import date
from classes.atividade import Atividade
import calendar

class Calendario:
    def __init__(self, data:date, atividades:[Atividade]):
        self.data = data
        self.atividades = atividades

    def inicio_mes(self):
        return date(self.data.year, self.data.month, 1)
    
    def final_mes(self):
        return date(self.data.year, self.data.month, calendar.monthrange(self.data.year, self.data.month)[1])

    def __str__(self):
        return f"Calendário início {self.inicio_mes()}, fim {self.final_mes()}:\n" + \
               "\n".join(f"- {atividade}" for atividade in self.atividades)