
from classes.tipoAtividade import TipoAtividade, TipoAtividadeComplementar
from classes.atividade import Atividade

class Setores:
    def __init__(self, atividades: list[Atividade]):
        self.setores = []
        self._criar_setores_unicos_(atividades)

    def _criar_setores_unicos_(self, atividades: list[Atividade]):
        tipos_unicos = {atividade.tipo for atividade in atividades}
        for tipo in tipos_unicos:
            setor = Setor(tipo)
            self.setores.append(setor)

    def __str__(self):
        return "\n".join(str(setor) for setor in self.setores)

class Setor:
    def __init__(self, tipoAtividade: TipoAtividade):
        if isinstance(tipoAtividade, TipoAtividadeComplementar):
            self._init_complementar_(tipoAtividade)
        else:
            self._init_padrao_(tipoAtividade)

    def _init_padrao_(self, tipoAtividade: TipoAtividade):
        self.nome = tipoAtividade.nome
        self.sigla = tipoAtividade.sigla

    def _init_complementar_(self, tipoAtividade: TipoAtividadeComplementar):
        self.nome = f"{tipoAtividade.nome} ({tipoAtividade.sigla_complementar})"
        self.sigla = tipoAtividade.sigla

    def __str__(self):
        return f"{self.sigla} - {self.nome}"