class TipoAtividade:
    def __init__(self, nome, sigla, duracao, tipo):
        self.nome = nome
        self.sigla = sigla
        self.duracao = duracao
        self.tipo = tipo

    def __str__(self):
        return f"{self.sigla} - {self.nome}, tipo {self.tipo}  duração {self.duracao} horas"