from classes.escala import Escala
from classes.modelos.cabecalho import Cabecalho
from classes.modelos.memoria import Memoria

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
    
    def converter_escala_para_memoria(self, escala: Escala) -> Memoria:
        memoria = Memoria(
            memoria_descritivo_hospital=escala.memoria_calculo_hospital.descritivo,
            memoria_total_horas_hospital=escala.memoria_calculo_hospital.total,
            memoria_descritivo_teorico=escala.memoria_calculo_teorica.descritivo,
            memoria_total_horas_teorico=escala.memoria_calculo_teorica.total
        )
        return memoria