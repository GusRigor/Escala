from classes.modelos.Renderable import Renderable

class Memoria(Renderable):
    def __init__(self, memoria_descritivo_hospital: list[str], memoria_total_horas_hospital: str,
                 memoria_descritivo_teorico: list[str], memoria_total_horas_teorico: str):
        self.memoria_descritivo_hospital = memoria_descritivo_hospital
        self.memoria_total_horas_hospital = memoria_total_horas_hospital
        self.memoria_descritivo_teorico = memoria_descritivo_teorico
        self.memoria_total_horas_teorico = memoria_total_horas_teorico

    def descritivo_hospital(self):
        return "\n".join(self.memoria_descritivo_hospital)
    
    def descritivo_teorico(self):
        return "\n".join(self.memoria_descritivo_teorico)

    def render(self):
        return {
            "memoria_descritivo_hospital": self.descritivo_hospital(),
            "memoria_total_horas_hospital": self.memoria_total_horas_hospital,
            "memoria_descritivo_teorico": self.descritivo_teorico(),
            "memoria_total_horas_teorico": self.memoria_total_horas_teorico
        }