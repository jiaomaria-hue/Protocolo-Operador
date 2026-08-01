from abc import ABC, abstractmethod
from rich import print
from rich.table import Table


class Transporte(ABC):
    def __init__(self, distancia: float):
        self.distancia = distancia
        self.frete = 0.0

    @abstractmethod
    def calcular_frete(self) -> str:
        """Método abstrato que retorna o valor do frete ou mensagem de restrição em formato de texto."""
        pass


class Moto(Transporte):
    fator = 0.5  # Atributo de classe

    def calcular_frete(self) -> str:
        self.frete = self.distancia * self.fator
        return f"R${self.frete:.2f}"


class Caminhao(Transporte):
    fator = 1.2  # Atributo de classe

    def calcular_frete(self) -> str:
        if self.distancia < 50:
            return "Distância mínima de 50Km"
        
        self.frete = self.distancia * self.fator
        return f"R${self.frete:.2f}"


class Drone(Transporte):
    fator = 9.5  # Atributo de classe

    def calcular_frete(self) -> str:
        if self.distancia > 10:
            return "Raio máximo de 10Km"
        
        self.frete = self.distancia * self.fator
        return f"R${self.frete:.2f}"


def mostrar_tabela_fretes(distancia: float):
    """Função responsável por instanciar os transportes e exibir a tabela Rich."""
    transportes = [
        Moto(distancia),
        Caminhao(distancia),
        Drone(distancia)
    ]

    tabela = Table(title="Tabela de Fretes")

    tabela.add_column("Distância", justify="left")
    tabela.add_column("Tipo", justify="left")
    tabela.add_column("Frete", justify="left")

    for t in transportes:
        tabela.add_row(
            f"{t.distancia}Km",
            t.__class__.__name__,
            str(t.calcular_frete())  # Retorna a string para a célula da tabela
        )

    print(tabela)