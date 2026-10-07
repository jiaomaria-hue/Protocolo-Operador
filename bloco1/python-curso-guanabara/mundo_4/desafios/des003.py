from rich import print
from rich.panel import Panel
from rich.text import Text


class Churrasco:

    def __init__(self, titulo="", quant=0):
        self.titulo = titulo
        self.quant = quant

    def analisar(self):        
        consumo_por_pessoa = 0.4  
        preco_kg = 82.40

        total_quilos = self.quant * consumo_por_pessoa
        custo_total = total_quilos * preco_kg
        valor_por_pessoa = custo_total / self.quant

        texto = Text.from_markup(
            f"Analisando [green]{self.titulo}[/green] com [blue]{self.quant} convidados[/blue]\n"
            f"Cada participante comerá {consumo_por_pessoa}Kg e cada Kg custa R${preco_kg:.2f}\n"
            f"Recomendo [blue]comprar {total_quilos:.3f}Gramas[/blue] de carne\n"
            f"O custo total será de [green]R${custo_total:.2f}[/green]\n"
            f"Cada pessoa pagará [green]R${valor_por_pessoa:.2f}[/green] para participar."
        )
        painel = Panel(
            texto,
            title=self.titulo,
            title_align="center",
            expand=False
        )
        return painel

c = Churrasco("Clevinho", 5)
resultado = c.analisar()
print(resultado)