from enums.tipoMemoria import TipoMemoria

class TipoAtividade:
    def __init__(self, nome, sigla, duracao, tipo:TipoMemoria):
        self.nome = nome
        self.sigla = sigla
        self.duracao = duracao
        self.tipo = tipo

    def __str__(self):
        return f"{self.sigla} - {self.nome}, tipo {self.tipo.value}  duração {self.duracao} horas"

class TipoAtividadeComplementar(TipoAtividade):
    def __init__(self, sigla_complementar):
        super().__init__("Complementação de carga horária", "CCH", 12, TipoMemoria.PRATICA)
        self.sigla_complementar = sigla_complementar

    def __str__(self):
        return f"{self.sigla} - {self.nome} ({self.sigla_complementar}), tipo {self.tipo.value}  duração {self.duracao} horas"

class TipoAtividadeVazia(TipoAtividade):
    def __init__(self):
        super().__init__("", "", 0, TipoMemoria.VAZIA)
    
    def __str__(self):
        return "Atividade Vazia (sem carga horária)"