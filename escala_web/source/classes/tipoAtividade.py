from source.enums.tipoMemoria import TipoMemoria

class TipoAtividade:
    def __init__(self, nome, sigla, duracao, tipo:TipoMemoria):
        self.nome = nome
        self.sigla = sigla
        self.duracao = duracao
        self.tipo = tipo

    def __str__(self):
        return f"{self.sigla} - {self.nome}, tipo {self.tipo.value}  duração {self.duracao} horas"
    
    def __eq__(self, other):
        if not isinstance(other, TipoAtividade):
            return False
        return (self.nome, self.sigla, self.tipo) == (other.nome, other.sigla, other.tipo)

    def __hash__(self):
        return hash((self.nome, self.sigla, self.tipo))

class TipoAtividadeComplementar(TipoAtividade):
    def __init__(self, sigla_complementar):
        super().__init__("Complementação de carga horária", "CCH", 12, TipoMemoria.PRATICA)
        self.sigla_complementar = sigla_complementar

    def __str__(self):
        return f"{self.sigla} - {self.nome} ({self.sigla_complementar}), tipo {self.tipo.value}  duração {self.duracao} horas"
    
    def __eq__(self, other):
        if not isinstance(other, TipoAtividadeComplementar):
            return False
        return (self.nome, self.sigla, self.tipo, self.sigla_complementar) == (other.nome, other.sigla, other.tipo, other.sigla_complementar)

    def __hash__(self):
        return hash((self.nome, self.sigla, self.tipo, self.sigla_complementar))

class TipoAtividadeVazia(TipoAtividade):
    def __init__(self):
        super().__init__("", "", 0, TipoMemoria.VAZIA)
    
    def __str__(self):
        return "Atividade Vazia (sem carga horária)"