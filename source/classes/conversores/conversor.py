from classes.escala import Escala
from classes.calendario import Calendario
from classes.modelos.cabecalho import Cabecalho
from classes.modelos.memoria import Memoria
from classes.modelos.atividades import Atividades
from classes.modelos.tabela import Tabela
from enums.turno import Turno

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
    
    def converter_escala_para_atividades(self, escala: Escala) -> Atividades:
        setores = [str(setor) for setor in escala.descritivo_setores.setores if len(str(setor)) > 3]
        atividades = Atividades(setores)
        return atividades
    
    def converter_calendario_para_tabela(self, calendario: Calendario) -> Tabela:
        dias = sorted(list({atividade.dia for atividade in calendario.atividades}))
        manha = [atividade.tipo.sigla for atividade in calendario.atividades if atividade.turno == Turno.MANHA]
        tarde = [atividade.tipo.sigla for atividade in calendario.atividades if atividade.turno == Turno.TARDE]
        noite = [atividade.tipo.sigla for atividade in calendario.atividades if atividade.turno == Turno.NOITE]
        
        tabela = Tabela(dias, manha, tarde, noite)
        return tabela