class Escala:
    def __init__(self, instituicao, residente, setores, preceptores, calendario):
        self.instituicao = instituicao
        self.residente = residente
        self.setores = setores
        self.preceptores = preceptores
        self.calendario = calendario

    def __str__(self):
        return f"Escala de {self.residente} na {self.instituicao}:\n" \
               f"Setores: {', '.join(self.setores)}\n" \
               f"Preceptores: {', '.join(self.preceptores)}\n" \
               f"Calendário: {self.calendario}"