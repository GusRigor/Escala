from source.classes.modelos.Renderable import Renderable

class Cabecalho(Renderable):

    def __init__(self):
        self.mes = "Junho"
        self.ano = "2025"
        self.instituicao = "Maternidade Bárbara Heliodora"
        self.residente = "Milene Mendes da Silva"
        self.setores = ["PPP"]
        self.preceptores = ["Enfª Obst. Ana Cláudia"]

    def __str__(self):
        return f"Escala de {self.residente} na {self.instituicao} - {self.mes}/{self.ano}\n" \
               f"Setores: {', '.join(self.setores)}\n" \
               f"Preceptores: {', '.join(self.preceptores)}\n"
    
    def _setores_para_render_(self):
        return " ".join(self.setores) if self.setores else ""
    
    def _preceptores_para_render_(self):
        return " ".join(self.preceptores) if self.preceptores else ""

    def render(self):
        return {
            "mes": self.mes,
            "ano": self.ano,
            "instituicao": self.instituicao,
            "residente": self.residente,
            "setores": self._setores_para_render_(),
            "preceptores": self._preceptores_para_render_()
        }