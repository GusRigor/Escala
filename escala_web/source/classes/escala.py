from source.classes.memoriaCalculo import MemoriaCalculo
from source.classes.setores import Setores
from source.classes.calendario import Calendario
from source.enums.tipoMemoria import TipoMemoria

class Escala:
    def __init__(self, instituicao, residente, setores, preceptores, calendario:Calendario):
        self.instituicao = instituicao
        self.residente = residente
        self.setores = setores
        self.preceptores = preceptores
        self.calendario = calendario
        self.memoria_calculo_hospital = MemoriaCalculo(TipoMemoria.PRATICA, calendario.atividades)
        self.memoria_calculo_teorica = MemoriaCalculo(TipoMemoria.TEORICA, calendario.atividades)
        self.descritivo_setores = Setores(calendario.atividades)


    def __str__(self):
        return f"Escala de {self.residente} na {self.instituicao}:\n" \
               f"Setores: {', '.join(self.setores)}\n" \
               f"Preceptores: {', '.join(self.preceptores)}\n" \
               f"Calendário: {self.calendario}\n" \
               f"Memória de cálculo hospitalar: {self.memoria_calculo_hospital.descritivo} = {self.memoria_calculo_hospital.total}h\n" \
               f"Memória de cálculo teórica: {self.memoria_calculo_teorica.descritivo} = {self.memoria_calculo_teorica.total}h\n" \
               f"Setores:\n{self.descritivo_setores}"