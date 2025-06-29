from classes.modelos.Renderable import Renderable

class Atividades(Renderable):
    def __init__(self, atividades: list[str]):
        self.atividades = atividades
    
    def render(self):
        return {
            "atividades": "\\\\\n".join(self.atividades)
        }