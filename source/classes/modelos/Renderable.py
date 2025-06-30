from abc import ABC, abstractmethod

class Renderable(ABC):
    @abstractmethod
    def render(self):
        """Renderiza o objeto em formato LaTeX."""
        pass