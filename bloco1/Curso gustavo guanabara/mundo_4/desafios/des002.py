from rich import print
from rich.panel import Panel


class Produto:

  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

  def etiqueta(self):
    largura_box = 35

    nome_formatado = f"{self.nome:^{largura_box}}"

    linha_pontos = "-" * largura_box

    preco_str = f"R${self.preco:,.2f}" 

    preco_formatado = f"{preco_str:^{largura_box}}".replace(" ", ".")

    conteudo = f"{nome_formatado}\n{linha_pontos}\n{preco_formatado}"

    painel = Panel(
    
    conteudo, 
    title="Produto", 
    title_align="center", 
    expand=False, 
    border_style="blue"
    )
    print(painel)


# Exemplo de uso:
p1 = Produto("iPhone 17 Pro Max", 25000.85)
p1.etiqueta()

p2 = Produto('MOuse', 120.00)
p2.etiqueta()