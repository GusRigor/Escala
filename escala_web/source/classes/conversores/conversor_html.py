from source.classes.tipoAtividade import TipoAtividade, TipoAtividadeComplementar, TipoAtividadeVazia
from source.classes.atividade import Atividade
from source.enums import TipoMemoria, Turno
from datetime import date

class Conversor_HTML:
    def converter_para_tipo_atividade(self, nome:str, sigla:str, duracao:int, tipo:str, sigla_complementar:str=None) -> TipoAtividade:
        tipo_memoria = TipoMemoria(tipo) if tipo else TipoMemoria.VAZIA
        if tipo_memoria == TipoMemoria.VAZIA:
            return TipoAtividadeVazia()
        if sigla_complementar:
            return TipoAtividadeComplementar(sigla_complementar)
        return TipoAtividade(nome, sigla, duracao, tipo_memoria)
    
    def converter_para_atividade(self, tipo:TipoAtividade, turno:str, dia:date) -> Atividade:
        turno_enum = Turno(turno)
        return Atividade(tipo, turno_enum, dia)
        