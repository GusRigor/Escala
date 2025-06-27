from classes.memoriaCalculo import MemoriaCalculo
from classes.setores import Setores
from classes.calendario import Calendario

class Escala:
    def __init__(self, instituicao, residente, setores, preceptores, calendario:Calendario):
        self.instituicao = instituicao
        self.residente = residente
        self.setores = setores
        self.preceptores = preceptores
        self.calendario = calendario
        self.memoria_calculo_hospital = MemoriaCalculo('P', calendario.atividades)
        self.memoria_calculo_teorica = MemoriaCalculo('T', calendario.atividades)
        self.descritivo_setores = Setores(calendario.atividades)


    def __str__(self):
        return f"Escala de {self.residente} na {self.instituicao}:\n" \
               f"Setores: {', '.join(self.setores)}\n" \
               f"Preceptores: {', '.join(self.preceptores)}\n" \
               f"Calendário: {self.calendario}\n" \
               f"Memória de cálculo hospitalar: {self.memoria_calculo_hospital.descritivo} = {self.memoria_calculo_hospital.total}h\n" \
               f"Memória de cálculo teórica: {self.memoria_calculo_teorica.descritivo} = {self.memoria_calculo_teorica.total}h\n" \
               f"Setores:\n{self.descritivo_setores}"