from classes.escala import Escala
from classes.modelos.cabecalho import Cabecalho

class Conversor:
    def converter_escala_para_cabecalho(self, escala: Escala) -> Cabecalho:
        cabecalho = Cabecalho()
        cabecalho.mes = escala.calendario.mes()
        cabecalho.ano = escala.calendario.ano()
        cabecalho.instituicao = escala.instituicao
        cabecalho.residente = escala.residente
        cabecalho.setores = escala.setores
        cabecalho.preceptores = escala.preceptores
        
        return cabecalho