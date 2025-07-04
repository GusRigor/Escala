from typing import List
from source.classes.modelos.Renderable import Renderable

class Atividades(Renderable):
    def __init__(self, atividades: List[str]):
        self.atividades = atividades
    
    def render(self):
        return {
            "atividades": "\\\\\n".join(self.atividades)
        }