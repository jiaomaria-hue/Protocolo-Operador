from abc import ABC, abstractmethod
from rich import print
class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def area(self):
        pass

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0) 
        self.raio = raio

    def perimetro(self):
        tot = 2 * 3.14 * self.raio
        return f'[black]{tot}[/]'
    
    def area(self):
        tot = 3.14 * (self.raio * self.raio)
        return f'[white]{tot}[/]'

class Quadrado(Poligono):
    def __init__(self, lados):
        super().__init__(4) 
        self.lados = lados
        
    def perimetro(self):
        tot = self.lados * 4
        return f'[blue]{tot}[/]'
    
    def area(self):
        tot = self.lados * self.lados
        return tot 