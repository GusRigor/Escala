from classes.atividade import Atividade
from enums.tipoMemoria import TipoMemoria

class MemoriaCalculo:
    def __init__(self, tipo, atividades:list[Atividade]):
        self.tipo = tipo
        self.total = 0
        self.descritivo = []
        self._calculo_total_(atividades)
        self._descritivo_por_tipo_atividade_(atividades)

    def _calculo_total_(self, atividades):
        for atividade in atividades:
            if atividade.tipo.tipo == self.tipo and atividade.tipo.tipo != TipoMemoria.VAZIA:
                self.total += atividade.tipo.duracao

    def _descritivo_por_tipo_atividade_(self, atividades:list[Atividade]):
        siglas = {atividade.tipo.sigla for atividade in atividades if atividade.tipo.tipo == self.tipo}
        quantidade_por_atividade = self._quantidade_por_atividade_(atividades, siglas)
        self.descritivo = self._quantidade_por_atividade_para_descritivo_(quantidade_por_atividade)
    
    def _quantidade_por_atividade_(self, atividades:list[Atividade], siglas):
        quantidade_por_atividade = []
        for sigla in siglas:
            quantidade = sum(1 for atividade in atividades if atividade.tipo.sigla == sigla)
            atividade = self._atividade_para_sigla_(atividades, sigla)
            quantidade_por_atividade.append({'atividade': atividade, 'quantidade': quantidade})

        return quantidade_por_atividade
    
    def _atividade_para_sigla_(self, atividades:list[Atividade], sigla):
        for atividade in atividades:
            if atividade.tipo.sigla == sigla:
                return atividade
            
    def _quantidade_por_atividade_para_descritivo_(self, quantidade_por_atividade):
        descritivo = []
        for item in quantidade_por_atividade:
            atividade = item['atividade']
            quantidade = item['quantidade']
            if atividade.tipo.tipo != TipoMemoria.VAZIA:
                descritivo.append(f"{atividade.tipo.sigla}-{atividade.tipo.duracao}={quantidade}x{atividade.tipo.duracao}={quantidade * atividade.tipo.duracao}h")
        return descritivo