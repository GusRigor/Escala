class TipoAtividade:
    def __init__(self, nome, sigla, duracao, tipo):
        self.nome = nome
        self.sigla = sigla
        self.duracao = duracao
        self.tipo = tipo

    def __str__(self):
        return f"{self.sigla} - {self.nome}, tipo {self.tipo}  duração {self.duracao} horas"

class TipoAtividadeComplementar(TipoAtividade):
            def __init__(self, sigla_complementar):
                super().__init__("Complementação de carga horária", "CCH", 12, "P")
                self.sigla_complementar = sigla_complementar

            def __str__(self):
                print(self.sigla_complementar)
                return f"{self.sigla} - {self.nome} ({self.sigla_complementar}), tipo {self.tipo}  duração {self.duracao} horas"