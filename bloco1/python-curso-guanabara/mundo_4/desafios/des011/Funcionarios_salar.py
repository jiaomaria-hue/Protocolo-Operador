from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    sal_min: float = 1612.0
    inss: float = 7.5

    def __init__(self, nome: str, sal_bruto: float = 0.0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = 0.0

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

    def analisar_salario(self):
        # Garante que o salário já foi calculado
        if self.salario == 0.0:
            self.calcular_salario()

        qtd_minimos = self.salario / Funcionario.sal_min
        
        # Formatação do texto usando tags de cor do Rich
        texto = (
            f"O salário de [blue]{self.nome}[/blue]"
            f"([purple]{self.__class__.__name__}[/purple]) é de\n "
            f"[green]R${self.salario:.2f}[/green] e corresponde a"
            f"[yellow]{qtd_minimos:.1f} salários mínimos[/yellow]."
        )

        # Imprime o texto encapsulado dentro do Panel com título
        print(Panel(texto, title="Análise de Salário", expand=False))


class FuncionarioHorista(Funcionario):
    def __init__(self, nome: str, valor_hora: float, horas_trab: float):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calcular_salario(self) -> float:
        self.sal_bruto = self.valor_hora * self.horas_trab
        self.salario = self.sal_bruto * (1 - Funcionario.inss / 100)
        return self.salario


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome: str, sal_bruto: float):
        super().__init__(nome, sal_bruto)

    def calcular_salario(self) -> float:
        self.salario = self.sal_bruto * (1 - Funcionario.inss / 100)
        return self.salario